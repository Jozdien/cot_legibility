import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from tqdm.auto import tqdm
import anthropic

from .prompts import LEGIBILITY_GRADING_PROMPT, CORRECTNESS_GRADING_PROMPT
from ..utils.io import read_jsonl, write_json


class Grader:
    def __init__(self, model: str = "claude-3-7-sonnet-latest"):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def grade_legibility(self, text: str, max_chars: int = 5000) -> dict:
        if len(text) > max_chars:
            text = text[-max_chars:]
            context_note = f"(Note: This is the last {max_chars} characters of a longer text)"
        else:
            context_note = ""

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": LEGIBILITY_GRADING_PROMPT, "cache_control": {"type": "ephemeral"}},
                    {"type": "text", "text": f"TEXT TO GRADE:\n{text}\n{context_note}"},
                ],
            }
        ]

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that grades text legibility. Always respond with valid JSON.",
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
        )

        response_text = response.content[0].text
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()

        return json.loads(json_str)

    def grade_correctness(self, predicted: str, actual: str, question: str) -> dict:
        grading_text = f"QUESTION: {question}\n\nPREDICTED ANSWER: {predicted}\n\nACTUAL ANSWER: {actual}"

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": CORRECTNESS_GRADING_PROMPT, "cache_control": {"type": "ephemeral"}},
                    {"type": "text", "text": grading_text},
                ],
            }
        ]

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that grades answer correctness. Always respond with valid JSON.",
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
        )

        response_text = response.content[0].text
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()

        return json.loads(json_str)


def grade_item(item: dict, grader: Grader, config: dict) -> dict:
    result = {"question_id": item["question_id"], "question": item["question"], "answer": item.get("answer")}

    if config.get("grade_legibility"):
        text_to_grade = item.get("reasoning") if item.get("reasoning") else item.get("answer", "")
        if text_to_grade:
            legibility = grader.grade_legibility(text_to_grade, config.get("max_chars_legibility", 5000))
            result["legibility"] = legibility

    if config.get("grade_correctness"):
        predicted = item.get("answer", "")
        actual = item.get("correct_answer", "")
        if predicted and actual:
            correctness = grader.grade_correctness(predicted, actual, item["question"])
            result["correctness"] = correctness

    return result


def compute_statistics(results: list[dict]) -> dict:
    stats = {"legibility": {}, "correctness": {}}

    if any("legibility" in r for r in results):
        scores = [r["legibility"]["score"] for r in results if "legibility" in r and isinstance(r["legibility"].get("score"), (int, float))]
        if scores:
            import numpy as np

            stats["legibility"] = {
                "mean": float(np.mean(scores)),
                "std": float(np.std(scores)),
                "median": float(np.median(scores)),
                "min": float(np.min(scores)),
                "max": float(np.max(scores)),
                "count": len(scores),
            }

    if any("correctness" in r for r in results):
        grades = [r["correctness"]["correctness"] for r in results if "correctness" in r]
        correct = grades.count("correct")
        partial = grades.count("partially_correct")
        incorrect = grades.count("incorrect")
        total = len(grades)

        stats["correctness"] = {
            "correct": correct,
            "partially_correct": partial,
            "incorrect": incorrect,
            "total": total,
            "correct_pct": round(correct / total * 100, 1) if total > 0 else 0,
            "partially_pct": round(partial / total * 100, 1) if total > 0 else 0,
            "incorrect_pct": round(incorrect / total * 100, 1) if total > 0 else 0,
        }

    return stats


def run_evaluation_stage(config: dict, output_dir: Path, logger) -> None:
    inference_file = config.get("inference_file")
    if not inference_file:
        inference_file = output_dir / "inference.jsonl"

    if not Path(inference_file).exists():
        raise FileNotFoundError(f"Inference file not found: {inference_file}")

    logger.info(f"Loading inference results from {inference_file}")
    items = list(read_jsonl(inference_file))
    logger.info(f"Loaded {len(items)} items")

    logger.info(f"Initializing grader with model: {config['grader_model']}")
    grader = Grader(config["grader_model"])

    max_workers = config["max_workers"]
    logger.info(f"Grading with {max_workers} workers")

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(grade_item, item, grader, config) for item in items]

        for future in tqdm(as_completed(futures), total=len(items), desc="Grading"):
            results.append(future.result())

    logger.info("Computing statistics")
    statistics = compute_statistics(results)

    evaluation_output = {
        "metadata": {
            "inference_file": str(inference_file),
            "grader_model": config["grader_model"],
            "timestamp": datetime.utcnow().isoformat() + "Z",
        },
        "results": results,
        "statistics": statistics,
    }

    evaluation_file = output_dir / "evaluation.json"
    write_json(evaluation_file, evaluation_output)
    logger.info(f"Evaluation complete. Results written to {evaluation_file}")

    logger.info("\nEvaluation Summary:")
    if statistics.get("legibility"):
        leg = statistics["legibility"]
        logger.info(f"  Legibility: mean={leg['mean']:.2f}, std={leg['std']:.2f}, median={leg['median']:.2f}")
    if statistics.get("correctness"):
        cor = statistics["correctness"]
        logger.info(f"  Correctness: {cor['correct_pct']:.1f}% correct, {cor['partially_pct']:.1f}% partial, {cor['incorrect_pct']:.1f}% incorrect")
