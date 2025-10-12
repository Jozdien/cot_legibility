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
    questions = list(dataset.get_questions(dataset_config.get("num_questions"), dataset_config.get("shuffle", False)))

    logger.info(f"Loaded {len(questions)} questions")
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
