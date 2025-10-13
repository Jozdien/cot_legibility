from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from tqdm.auto import tqdm

from .datasets import Dataset
from .providers import get_provider
from ..utils.io import append_jsonl, read_jsonl, write_json


def process_question(question_data: dict, model_config: dict, provider) -> dict:
    try:
        result = provider.generate(question_data["question"], model_config)

        metadata = {
            "duration_ms": result["duration_ms"],
            "tokens": result.get("tokens"),
        }
        if "provider_model" in result:
            metadata["provider_model"] = result["provider_model"]
        if "openrouter_provider" in result:
            metadata["openrouter_provider"] = result["openrouter_provider"]

        return {
            **question_data,
            "answer": result["answer"],
            "reasoning": result.get("reasoning"),
            "model": model_config["name"],
            "temperature": model_config.get("temperature", 1.0),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metadata": metadata,
        }
    except Exception as e:
        return {
            **question_data,
            "error": str(e),
            "model": model_config["name"],
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }


def run_inference_stage(config: dict, output_dir: Path, logger) -> None:
    model_config = config["models"][0]
    dataset_config = config["datasets"][0]

    logger.info(f"Loading dataset: {dataset_config['name']}")
    dataset = Dataset(dataset_config["name"])

    question_ids = dataset_config.get("question_ids")
    if question_ids:
        logger.info(f"Filtering to {len(question_ids)} specific question IDs")
        all_questions = list(dataset.get_questions(num_questions=None, shuffle=False))
        question_map = {q["question_id"]: q for q in all_questions}
        questions = [question_map[qid] for qid in question_ids if qid in question_map]
        if len(questions) < len(question_ids):
            logger.warning(f"Could not find {len(question_ids) - len(questions)} question IDs in dataset")
    else:
        questions = list(dataset.get_questions(dataset_config.get("num_questions"), dataset_config.get("shuffle", False)))

    samples_per_question = dataset_config.get("samples_per_question", 1)
    if samples_per_question > 1:
        logger.info(f"Generating {samples_per_question} samples per question")
        expanded_questions = []
        for q in questions:
            for sample_idx in range(samples_per_question):
                sample_q = q.copy()
                sample_q["sample_index"] = sample_idx
                expanded_questions.append(sample_q)
        questions = expanded_questions
    else:
        for q in questions:
            q["sample_index"] = 0

    logger.info(f"Loaded {len(questions)} total samples ({len(questions) // samples_per_question} unique questions)")
    logger.info(f"Initializing provider: {model_config['provider']}")

    provider = get_provider(model_config["provider"])
    inference_file = output_dir / "inference.jsonl"

    max_workers = config["concurrency"]["max_workers"]
    logger.info(f"Running inference with {max_workers} workers")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_question, q, model_config, provider) for q in questions]

        for future in tqdm(as_completed(futures), total=len(questions), desc="Inference"):
            result = future.result()
            append_jsonl(inference_file, result)

            if "error" in result:
                logger.warning(f"Error on question {result['question_id']}: {result['error']}")

    logger.info("Converting results to JSON format")
    results = list(read_jsonl(inference_file))
    json_file = output_dir / "inference.json"
    write_json(json_file, results)
    inference_file.unlink()
    logger.info(f"Inference complete. {len(results)} results written to {json_file}")
