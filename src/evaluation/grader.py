import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from tqdm.auto import tqdm

from .prompts import LEGIBILITY_GRADING_PROMPT, CORRECTNESS_GRADING_PROMPT
from ..inference.providers import get_provider
from ..utils.io import read_json, write_json
from ..utils.models import get_model_config


def parse_json_response(response_text: str) -> dict:
    if "```json" in response_text:
        json_str = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        json_str = response_text.split("```")[1].strip()
    else:
        json_str = response_text.strip()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        try:
            json_str_fixed = re.sub(r'\\([^"\\\/bfnrtu])', r'\\\\\1', json_str)
            return json.loads(json_str_fixed)
        except json.JSONDecodeError:
            raise ValueError(f"Failed to parse JSON response: {e}\nResponse: {json_str[:500]}")


class Grader:
    def __init__(self, model_name: str = "claude-3-7-sonnet-latest"):
        config = get_model_config(model_name)
        self.provider = get_provider(config["provider"])
        self.model_config = config
        self.model_name = model_name

    def grade_legibility(self, text: str, max_chars: int = 5000) -> dict:
        if not text or not text.strip():
            raise ValueError("Cannot grade empty or whitespace-only text")

        if len(text) > max_chars:
            text = text[-max_chars:]
            context_note = f"(Note: This is the last {max_chars} characters of a longer text)"
        else:
            context_note = ""

        prompt = f"{LEGIBILITY_GRADING_PROMPT}\n\nTEXT TO GRADE:\n{text}\n{context_note}"

        grading_config = {**self.model_config, "temperature": 0.0}
        result = self.provider.generate(prompt, grading_config)
        return parse_json_response(result["answer"])

    def grade_legibility_chunks(self, text: str, chunk_size: int = 5000) -> list[dict]:
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunk_text = text[i:i + chunk_size]
            if not chunk_text.strip():
                continue
            try:
                grade = self.grade_legibility(chunk_text, max_chars=chunk_size)
                chunks.append({
                    "start_pos": i,
                    "end_pos": min(i + chunk_size, len(text)),
                    **grade
                })
            except Exception as e:
                chunks.append({
                    "start_pos": i,
                    "end_pos": min(i + chunk_size, len(text)),
                    "error": str(e),
                    "score": None
                })
        return chunks

    def grade_correctness(self, predicted: str, actual: str, question: str) -> dict:
        grading_text = f"QUESTION: {question}\n\nPREDICTED ANSWER: {predicted}\n\nACTUAL ANSWER: {actual}"
        prompt = f"{CORRECTNESS_GRADING_PROMPT}\n\n{grading_text}"

        grading_config = {**self.model_config, "temperature": 0.0}
        result = self.provider.generate(prompt, grading_config)
        return parse_json_response(result["answer"])


def grade_item(item: dict, grader: Grader, config: dict) -> dict:
    result = {
        "question_id": item["question_id"],
        "sample_index": item.get("sample_index", 0),
        "question": item["question"],
        "answer": item.get("answer"),
        "correct_answer": item.get("correct_answer"),
        "dataset": item.get("dataset"),
        "model": item.get("model"),
        "temperature": item.get("temperature"),
        "timestamp": item.get("timestamp"),
        "metadata": item.get("metadata"),
        "errors": []
    }

    reasoning = item.get("reasoning")
    if reasoning:
        result["reasoning_excerpt"] = reasoning[-500:]

    if config.get("grade_legibility"):
        answer_text = item.get("answer", "")

        if config.get("grade_response_reasoning_separately", False):
            if reasoning:
                try:
                    result["legibility_reasoning"] = grader.grade_legibility(reasoning, config.get("max_chars_legibility", 5000))
                except Exception as e:
                    result["errors"].append(f"legibility_reasoning: {str(e)}")
            if answer_text:
                try:
                    result["legibility_response"] = grader.grade_legibility(answer_text, config.get("max_chars_legibility", 5000))
                except Exception as e:
                    result["errors"].append(f"legibility_response: {str(e)}")
        else:
            text_to_grade = reasoning if reasoning else answer_text
            if text_to_grade:
                try:
                    legibility = grader.grade_legibility(text_to_grade, config.get("max_chars_legibility", 5000))
                    result["legibility"] = legibility
                except Exception as e:
                    result["errors"].append(f"legibility: {str(e)}")

        if config.get("grade_legibility_chunks", False) and reasoning:
            chunk_size = config.get("chunk_size", 5000)
            try:
                result["legibility_chunks"] = grader.grade_legibility_chunks(reasoning, chunk_size)
            except Exception as e:
                result["errors"].append(f"legibility_chunks: {str(e)}")

    if config.get("grade_correctness"):
        predicted = item.get("answer", "")
        actual = item.get("correct_answer", "")
        if predicted and actual:
            try:
                correctness = grader.grade_correctness(predicted, actual, item["question"])
                result["correctness"] = correctness
            except Exception as e:
                result["errors"].append(f"correctness: {str(e)}")

    if not result["errors"]:
        del result["errors"]

    return result


def compute_statistics(results: list[dict]) -> dict:
    stats = {"legibility": {}, "correctness": {}}

    import numpy as np

    for key in ["legibility", "legibility_reasoning", "legibility_response"]:
        if any(key in r for r in results):
            scores = [r[key]["score"] for r in results if key in r and isinstance(r[key].get("score"), (int, float))]
            if scores:
                stats[key] = {
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
        inference_file = output_dir / "inference.json"

    if not Path(inference_file).exists():
        raise FileNotFoundError(f"Inference file not found: {inference_file}")

    logger.info(f"Loading inference results from {inference_file}")
    items = read_json(inference_file)
    logger.info(f"Loaded {len(items)} items")

    checkpoint_file = output_dir / "evaluation_checkpoint.json"
    completed_ids = set()
    results = []

    if checkpoint_file.exists():
        logger.info(f"Found checkpoint file, resuming from {checkpoint_file}")
        checkpoint_data = read_json(checkpoint_file)
        results = checkpoint_data.get("results", [])
        completed_ids = {(r["question_id"], r["sample_index"]) for r in results}
        logger.info(f"Resuming: {len(completed_ids)} items already completed")

    items_to_process = [
        item for item in items
        if (item["question_id"], item.get("sample_index", 0)) not in completed_ids
    ]

    if not items_to_process:
        logger.info("All items already processed, skipping to statistics")
    else:
        logger.info(f"Initializing grader with model: {config['grader_model']}")
        grader = Grader(config["grader_model"])

        max_workers = config["max_workers"]
        logger.info(f"Grading {len(items_to_process)} items with {max_workers} workers")

        checkpoint_interval = 50
        item_futures = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for item in items_to_process:
                future = executor.submit(grade_item, item, grader, config)
                item_futures[future] = item

            for idx, future in enumerate(tqdm(as_completed(item_futures), total=len(items_to_process), desc="Grading"), 1):
                try:
                    result = future.result()
                    results.append(result)

                    if "errors" in result and result["errors"]:
                        logger.warning(f"Errors in grading question {result['question_id']}: {result['errors']}")

                    if idx % checkpoint_interval == 0:
                        write_json(checkpoint_file, {"results": results})
                        logger.debug(f"Checkpoint saved at {idx} items")

                except Exception as e:
                    item = item_futures[future]
                    logger.error(f"Failed to grade question {item['question_id']}: {str(e)}")
                    results.append({
                        "question_id": item["question_id"],
                        "sample_index": item.get("sample_index", 0),
                        "question": item["question"],
                        "errors": [f"Fatal error: {str(e)}"]
                    })

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

    if checkpoint_file.exists():
        checkpoint_file.unlink()
        logger.info("Checkpoint file removed")

    error_count = sum(1 for r in results if "errors" in r and r["errors"])
    if error_count > 0:
        logger.warning(f"Completed with {error_count} items containing errors")

    logger.info("\nEvaluation Summary:")
    if statistics.get("legibility"):
        leg = statistics["legibility"]
        logger.info(f"  Legibility: mean={leg['mean']:.2f}, std={leg['std']:.2f}, median={leg['median']:.2f}")
    if statistics.get("correctness"):
        cor = statistics["correctness"]
        logger.info(f"  Correctness: {cor['correct_pct']:.1f}% correct, {cor['partially_pct']:.1f}% partial, {cor['incorrect_pct']:.1f}% incorrect")
