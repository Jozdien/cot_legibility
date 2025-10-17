from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from tqdm.auto import tqdm

from .providers import get_provider
from ..utils.io import append_jsonl, read_json, read_jsonl, write_json


def extract_reasoning_up_to_threshold(reasoning: str, legibility_chunks: list[dict], threshold: int) -> str | None:
    if not legibility_chunks or not reasoning:
        return None

    valid_chunks = []
    for chunk in legibility_chunks:
        score = chunk.get("score")
        if score is None or not isinstance(score, (int, float)):
            continue
        if score < threshold:
            valid_chunks.append(chunk)
        else:
            break

    if not valid_chunks:
        return None

    last_chunk = valid_chunks[-1]
    cutoff_pos = last_chunk.get("end_pos", 0)

    extracted = reasoning[:cutoff_pos]

    last_newline = extracted.rfind('\n')
    if last_newline != -1:
        extracted = extracted[:last_newline]

    return extracted if extracted.strip() else None


def process_prefilled_question(result: dict, model_config: dict, provider, threshold: int, include_reasoning: bool) -> dict:
    try:
        reasoning = result.get("reasoning", "")
        legibility_chunks = result.get("legibility_chunks", [])

        extracted_reasoning = extract_reasoning_up_to_threshold(reasoning, legibility_chunks, threshold)

        if not extracted_reasoning:
            return {
                **result,
                "prefill_error": "No valid reasoning to extract",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            }

        prefill_model_config = model_config.copy()
        prefill_model_config["include_reasoning"] = include_reasoning

        response = provider.generate(result["question"], prefill_model_config, prefill=extracted_reasoning)

        returned_reasoning = response.get("reasoning")
        if not include_reasoning and returned_reasoning:
            return {
                **result,
                "prefill_answer": response["answer"],
                "prefill_reasoning": returned_reasoning,
                "prefill_reasoning_length": len(extracted_reasoning),
                "prefill_validation_error": "Model returned reasoning when include_reasoning=False",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "metadata": {
                    "duration_ms": response["duration_ms"],
                    "tokens": response.get("tokens"),
                },
            }

        metadata = {
            "duration_ms": response["duration_ms"],
            "tokens": response.get("tokens"),
        }
        if "provider_model" in response:
            metadata["provider_model"] = response["provider_model"]
        if "openrouter_provider" in response:
            metadata["openrouter_provider"] = response["openrouter_provider"]

        return {
            **result,
            "prefill_answer": response["answer"],
            "prefill_reasoning": response.get("reasoning"),
            "prefill_reasoning_length": len(extracted_reasoning),
            "prefill_include_reasoning": include_reasoning,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metadata": metadata,
        }
    except Exception as e:
        return {
            **result,
            "prefill_error": str(e),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }


def run_prefill_stage(config: dict, output_dir: Path, logger) -> None:
    prefill_config = config["prefill"]

    evaluation_file = prefill_config.get("evaluation_file")
    if evaluation_file:
        evaluation_file = Path(evaluation_file)
    else:
        evaluation_file = output_dir / "evaluation.json"

    if not evaluation_file.exists():
        raise FileNotFoundError(f"Evaluation file not found: {evaluation_file}")

    logger.info(f"Loading evaluation results from {evaluation_file}")
    evaluation = read_json(evaluation_file)
    results = evaluation.get("results", [])

    if not results:
        logger.warning("No results found in evaluation file")
        return

    model_name = results[0].get("model")
    if not model_name:
        raise ValueError("Could not determine model from evaluation results")

    model_config = None
    if "inference" in config and "models" in config["inference"]:
        for m in config["inference"]["models"]:
            if m["name"] == model_name:
                model_config = m
                break

    if not model_config:
        raise ValueError(f"Model config not found for model: {model_name}")

    threshold = prefill_config["legibility_threshold"]
    include_reasoning = prefill_config["include_reasoning"]
    max_workers = prefill_config["max_workers"]

    logger.info(f"Extracting reasoning up to legibility threshold: {threshold}")
    logger.info(f"Include reasoning in prefilled calls: {include_reasoning}")
    logger.info(f"Initializing provider: {model_config['provider']}")

    provider = get_provider(model_config["provider"])
    prefill_inference_file = output_dir / "prefill_inference.jsonl"

    logger.info(f"Running prefilled inference with {max_workers} workers")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(process_prefilled_question, r, model_config, provider, threshold, include_reasoning)
            for r in results
        ]

        for future in tqdm(as_completed(futures), total=len(results), desc="Prefill Inference"):
            result = future.result()
            append_jsonl(prefill_inference_file, result)

            if "prefill_error" in result:
                logger.warning(f"Error on question {result.get('question_id')}: {result['prefill_error']}")
            elif "prefill_validation_error" in result:
                logger.warning(f"Validation error on question {result.get('question_id')}: {result['prefill_validation_error']}")

    logger.info("Converting results to JSON format")
    results = list(read_jsonl(prefill_inference_file))
    json_file = output_dir / "prefill_inference.json"
    write_json(json_file, results)
    prefill_inference_file.unlink()
    logger.info(f"Prefill inference complete. {len(results)} results written to {json_file}")
