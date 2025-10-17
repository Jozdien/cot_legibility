from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from tqdm.auto import tqdm

from .providers import get_provider
from ..utils.io import append_jsonl, read_json, read_jsonl, write_json


def extract_reasoning_up_to_threshold(reasoning: str, legibility_chunks: list[dict], threshold: int) -> tuple[str | None, str | None]:
    if not reasoning:
        return None, "no_reasoning"
    if not legibility_chunks:
        return None, "no_chunks"

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
        return None, "all_chunks_above_threshold"

    last_chunk = valid_chunks[-1]
    cutoff_pos = last_chunk.get("end_pos", 0)

    extracted = reasoning[:cutoff_pos]

    last_newline = extracted.rfind('\n')
    if last_newline != -1:
        extracted = extracted[:last_newline]

    if not extracted.strip():
        return None, "empty_after_extraction"

    return extracted, None


def process_prefilled_question(result: dict, model_config: dict, provider, threshold: int, include_reasoning: bool) -> dict:
    try:
        reasoning = result.get("reasoning", "")
        legibility_chunks = result.get("legibility_chunks", [])

        extracted_reasoning, skip_reason = extract_reasoning_up_to_threshold(reasoning, legibility_chunks, threshold)

        if extracted_reasoning:
            extracted_reasoning = f"<think>\n{extracted_reasoning}\n</think>"

        if not extracted_reasoning:
            skip_messages = {
                "no_reasoning": "No reasoning available to extract",
                "no_chunks": "No legibility chunks available",
                "all_chunks_above_threshold": f"Skipped: all chunks already above threshold ({threshold})",
                "empty_after_extraction": "Extraction resulted in empty reasoning",
            }
            output = {
                "question_id": result["question_id"],
                "question": result["question"],
                "original_answer": result.get("answer"),
                "original_correctness": result.get("correctness"),
                "legibility_chunks": legibility_chunks,
                "prefill_skip_reason": skip_reason,
                "prefill_skip_message": skip_messages.get(skip_reason, "Unknown reason"),
                "timestamp": datetime.utcnow().isoformat() + "Z",
            }
            if "sample_index" in result:
                output["sample_index"] = result["sample_index"]
            return output

        prefill_model_config = model_config.copy()
        prefill_model_config["include_reasoning"] = include_reasoning

        messages = [
            {"role": "user", "content": result["question"]},
            {"role": "assistant", "content": extracted_reasoning}
        ]

        request_sample = {
            "messages": messages,
            "model_config": prefill_model_config,
        }

        response = provider.generate(result["question"], prefill_model_config, prefill=extracted_reasoning)

        metadata = {
            "duration_ms": response["duration_ms"],
            "tokens": response.get("tokens"),
        }
        if "provider_model" in response:
            metadata["provider_model"] = response["provider_model"]
        if "openrouter_provider" in response:
            metadata["openrouter_provider"] = response["openrouter_provider"]
        if "stream_complete" in response:
            metadata["stream_complete"] = response["stream_complete"]
        if "error" in response:
            metadata["error"] = response["error"]

        output = {
            "question_id": result["question_id"],
            "question": result["question"],
            "original_answer": result.get("answer"),
            "original_correctness": result.get("correctness"),
            "legibility_chunks": legibility_chunks,
            "prefill": extracted_reasoning,
            "prefill_answer": response["answer"],
            "prefill_reasoning": response.get("reasoning"),
            "prefill_reasoning_length": len(extracted_reasoning),
            "prefill_include_reasoning": include_reasoning,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metadata": metadata,
        }
        for field in ["correct_answer", "dataset", "model", "temperature"]:
            if field in result:
                output[field] = result[field]
        if "sample_index" in result:
            output["sample_index"] = result["sample_index"]

        returned_reasoning = response.get("reasoning")
        if not include_reasoning and returned_reasoning:
            output["prefill_validation_error"] = "Model returned reasoning when include_reasoning=False"

        output["_request_sample"] = request_sample
        output["_full_original_reasoning"] = reasoning

        return output
    except Exception as e:
        output = {
            "question_id": result["question_id"],
            "question": result["question"],
            "original_answer": result.get("answer"),
            "original_correctness": result.get("correctness"),
            "prefill_error": str(e),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
        if "sample_index" in result:
            output["sample_index"] = result["sample_index"]
        return output


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
    eval_results = evaluation.get("results", [])

    inference_file = evaluation.get("metadata", {}).get("inference_file")
    if not inference_file:
        inference_file = output_dir / "inference.json"
    else:
        inference_file = Path(inference_file)

    if not inference_file.exists():
        raise FileNotFoundError(f"Inference file not found: {inference_file}")

    logger.info(f"Loading full reasoning from {inference_file}")
    inference_results = read_json(inference_file)
    reasoning_map = {
        (item["question_id"], item.get("sample_index", 0)): item.get("reasoning", "")
        for item in inference_results
    }

    results = []
    for eval_result in eval_results:
        q_id = eval_result["question_id"]
        sample_idx = eval_result.get("sample_index", 0)
        full_reasoning = reasoning_map.get((q_id, sample_idx), "")
        result = {**eval_result, "reasoning": full_reasoning}
        results.append(result)

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

            if "prefill_skip_reason" in result:
                logger.info(f"Question {result.get('question_id')}: {result['prefill_skip_message']}")
            elif "prefill_error" in result:
                logger.warning(f"Error on question {result.get('question_id')}: {result['prefill_error']}")
            elif "prefill_validation_error" in result:
                logger.warning(f"Validation error on question {result.get('question_id')}: {result['prefill_validation_error']}")

    logger.info("Converting results to JSON format")
    results = list(read_jsonl(prefill_inference_file))

    sample = None
    for r in results:
        if "_request_sample" in r and "_full_original_reasoning" in r:
            sample = {
                "note": "This is a sample entry showing the complete structure with all fields for verification",
                "question_id": r["question_id"],
                "question": r["question"],
                "original_answer": r["original_answer"],
                "original_correctness": r["original_correctness"],
                "original_reasoning_full": r["_full_original_reasoning"],
                "legibility_chunks": r["legibility_chunks"],
                "prefill_extracted": r["prefill"],
                "prefill_answer": r["prefill_answer"],
                "prefill_reasoning": r.get("prefill_reasoning"),
                "request_to_model": r["_request_sample"],
                "metadata": r["metadata"],
                "timestamp": r["timestamp"],
            }
            if "sample_index" in r:
                sample["sample_index"] = r["sample_index"]
            break

    for r in results:
        r.pop("_request_sample", None)
        r.pop("_full_original_reasoning", None)

    json_file = output_dir / "prefill_inference.json"
    output_data = {"results": results}
    if sample:
        output_data["sample"] = sample
    write_json(json_file, output_data)
    prefill_inference_file.unlink()
    logger.info(f"Prefill inference complete. {len(results)} results written to {json_file}")
