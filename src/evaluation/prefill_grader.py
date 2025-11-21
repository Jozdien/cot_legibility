from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from tqdm.auto import tqdm

from ..utils.io import read_json, write_json
from .grader import Grader


def grade_prefill_item(item: dict, grader: Grader) -> dict:
    result = {
        "question_id": item["question_id"],
        "sample_index": item.get("sample_index", 0),
        "question": item["question"],
        "prefill_answer": item.get("prefill_answer"),
        "correct_answer": item.get("correct_answer"),
        "original_answer": item.get("original_answer"),
        "dataset": item.get("dataset"),
        "model": item.get("model"),
        "temperature": item.get("temperature"),
        "prefill_reasoning_length": item.get("prefill_reasoning_length"),
        "prefill_include_reasoning": item.get("prefill_include_reasoning"),
        "timestamp": item.get("timestamp"),
        "metadata": item.get("metadata"),
    }

    if "prefill_error" in item:
        result["prefill_error"] = item["prefill_error"]
        return result

    if "prefill_skip_reason" in item:
        result["prefill_skip_reason"] = item["prefill_skip_reason"]
        result["prefill_skip_message"] = item["prefill_skip_message"]

        original_predicted = item.get("original_answer", "")
        actual = item.get("correct_answer", "")
        if original_predicted and actual:
            original_correctness = grader.grade_correctness(
                original_predicted, actual, item["question"]
            )
            result["original_correctness"] = original_correctness

        return result

    if "prefill_validation_error" in item:
        result["prefill_validation_error"] = item["prefill_validation_error"]

    predicted = item.get("prefill_answer", "")
    actual = item.get("correct_answer", "")
    if predicted and actual:
        correctness = grader.grade_correctness(predicted, actual, item["question"])
        result["prefill_correctness"] = correctness

    original_predicted = item.get("original_answer", "")
    if original_predicted and actual:
        original_correctness = grader.grade_correctness(
            original_predicted, actual, item["question"]
        )
        result["original_correctness"] = original_correctness

    return result


def compute_prefill_statistics(results: list[dict]) -> dict:
    stats = {
        "prefill_correctness": {},
        "original_correctness": {},
        "comparison": {},
    }

    prefill_grades = [
        r["prefill_correctness"]["correctness"]
        for r in results
        if "prefill_correctness" in r
    ]
    if prefill_grades:
        correct = prefill_grades.count("correct")
        partial = prefill_grades.count("partially_correct")
        incorrect = prefill_grades.count("incorrect")
        total = len(prefill_grades)

        stats["prefill_correctness"] = {
            "correct": correct,
            "partially_correct": partial,
            "incorrect": incorrect,
            "total": total,
            "correct_pct": round(correct / total * 100, 1) if total > 0 else 0,
            "partially_pct": round(partial / total * 100, 1) if total > 0 else 0,
            "incorrect_pct": round(incorrect / total * 100, 1) if total > 0 else 0,
        }

    original_grades = [
        r["original_correctness"]["correctness"]
        for r in results
        if "original_correctness" in r
    ]
    if original_grades:
        correct = original_grades.count("correct")
        partial = original_grades.count("partially_correct")
        incorrect = original_grades.count("incorrect")
        total = len(original_grades)

        stats["original_correctness"] = {
            "correct": correct,
            "partially_correct": partial,
            "incorrect": incorrect,
            "total": total,
            "correct_pct": round(correct / total * 100, 1) if total > 0 else 0,
            "partially_pct": round(partial / total * 100, 1) if total > 0 else 0,
            "incorrect_pct": round(incorrect / total * 100, 1) if total > 0 else 0,
        }

    if prefill_grades and original_grades:
        stats["comparison"] = {
            "prefill_correct_pct": stats["prefill_correctness"]["correct_pct"],
            "original_correct_pct": stats["original_correctness"]["correct_pct"],
            "difference_pct": round(
                stats["prefill_correctness"]["correct_pct"]
                - stats["original_correctness"]["correct_pct"],
                1,
            ),
        }

    errors = sum(1 for r in results if "prefill_error" in r)
    validation_errors = sum(1 for r in results if "prefill_validation_error" in r)
    skipped = sum(1 for r in results if "prefill_skip_reason" in r)

    skip_breakdown = {}
    for r in results:
        if "prefill_skip_reason" in r:
            reason = r["prefill_skip_reason"]
            if reason not in skip_breakdown:
                skip_breakdown[reason] = 0
            skip_breakdown[reason] += 1

    if errors or validation_errors or skipped:
        stats["errors"] = {
            "prefill_errors": errors,
            "validation_errors": validation_errors,
            "skipped": skipped,
            "skip_breakdown": skip_breakdown,
        }

    threshold_never_reached_results = [
        r
        for r in results
        if r.get("prefill_skip_reason") == "threshold_never_reached"
        and "original_correctness" in r
    ]
    if threshold_never_reached_results:
        grades = [
            r["original_correctness"]["correctness"]
            for r in threshold_never_reached_results
        ]
        correct = grades.count("correct")
        partial = grades.count("partially_correct")
        incorrect = grades.count("incorrect")
        total = len(grades)

        stats["threshold_never_reached"] = {
            "count": total,
            "correct": correct,
            "partially_correct": partial,
            "incorrect": incorrect,
            "correct_pct": round(correct / total * 100, 1) if total > 0 else 0,
            "partially_pct": round(partial / total * 100, 1) if total > 0 else 0,
            "incorrect_pct": round(incorrect / total * 100, 1) if total > 0 else 0,
        }

    return stats


def run_prefill_evaluation_stage(config: dict, output_dir: Path, logger) -> None:
    prefill_inference_file = output_dir / "prefill_inference.json"

    if not prefill_inference_file.exists():
        raise FileNotFoundError(
            f"Prefill inference file not found: {prefill_inference_file}"
        )

    logger.info(f"Loading prefill inference results from {prefill_inference_file}")
    data = read_json(prefill_inference_file)
    if isinstance(data, dict) and "results" in data:
        items = data["results"]
    else:
        items = data
    logger.info(f"Loaded {len(items)} items")

    grader_model = config.get("evaluation", {}).get("grader_model", "gpt-4o")
    logger.info(f"Initializing grader with model: {grader_model}")
    grader = Grader(grader_model)

    max_workers = config.get("evaluation", {}).get("max_workers", 5)
    logger.info(f"Grading with {max_workers} workers")

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(grade_prefill_item, item, grader) for item in items]

        for future in tqdm(
            as_completed(futures), total=len(items), desc="Grading Prefilled"
        ):
            results.append(future.result())

    logger.info("Computing statistics")
    statistics = compute_prefill_statistics(results)

    evaluation_output = {
        "metadata": {
            "prefill_inference_file": str(prefill_inference_file),
            "grader_model": grader_model,
            "threshold": config.get("prefill", {}).get("legibility_threshold", 7),
            "timestamp": datetime.utcnow().isoformat() + "Z",
        },
        "results": results,
        "statistics": statistics,
    }

    prefill_evaluation_file = output_dir / "prefill_evaluation.json"
    write_json(prefill_evaluation_file, evaluation_output)
    logger.info(
        f"Prefill evaluation complete. Results written to {prefill_evaluation_file}"
    )

    logger.info("\nPrefill Evaluation Summary:")
    if statistics.get("prefill_correctness"):
        cor = statistics["prefill_correctness"]
        logger.info(
            f"  Prefilled: {cor['correct_pct']:.1f}% correct, {cor['partially_pct']:.1f}% partial, {cor['incorrect_pct']:.1f}% incorrect (n={cor['total']})"
        )
    if statistics.get("original_correctness"):
        cor = statistics["original_correctness"]
        logger.info(
            f"  Original (all): {cor['correct_pct']:.1f}% correct, {cor['partially_pct']:.1f}% partial, {cor['incorrect_pct']:.1f}% incorrect (n={cor['total']})"
        )
    if statistics.get("threshold_never_reached"):
        tnr = statistics["threshold_never_reached"]
        logger.info(
            f"  Threshold never reached: {tnr['correct_pct']:.1f}% correct, {tnr['partially_pct']:.1f}% partial, {tnr['incorrect_pct']:.1f}% incorrect (n={tnr['count']})"
        )
    if statistics.get("comparison"):
        comp = statistics["comparison"]
        diff = comp["difference_pct"]
        sign = "+" if diff > 0 else ""
        logger.info(f"  Difference: {sign}{diff:.1f}% (prefilled vs original)")
    if statistics.get("errors"):
        err = statistics["errors"]
        logger.info(
            f"  Errors: {err.get('prefill_errors', 0)} prefill errors, {err.get('validation_errors', 0)} validation errors, {err.get('skipped', 0)} skipped"
        )
        if err.get("skip_breakdown"):
            logger.info(f"  Skip breakdown: {err['skip_breakdown']}")
