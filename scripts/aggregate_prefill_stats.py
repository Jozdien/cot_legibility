import json
from pathlib import Path

def aggregate_prefill_stats():
    runs_dir = Path("/Users/jose/cot_legibility/runs")

    prefill_files = list(runs_dir.glob("*/prefill_evaluation.json"))

    total_prefill_correct = 0
    total_prefill_partial = 0
    total_prefill_incorrect = 0
    total_prefill_total = 0

    total_original_correct = 0
    total_original_partial = 0
    total_original_incorrect = 0
    total_original_total = 0

    print(f"Found {len(prefill_files)} prefill evaluation files\n")

    for pf in prefill_files:
        with open(pf) as f:
            data = json.load(f)

        stats = data.get("statistics", {})
        prefill_stats = stats.get("prefill_correctness", {})
        original_stats = stats.get("original_correctness", {})

        total_prefill_correct += prefill_stats.get("correct", 0)
        total_prefill_partial += prefill_stats.get("partially_correct", 0)
        total_prefill_incorrect += prefill_stats.get("incorrect", 0)
        total_prefill_total += prefill_stats.get("total", 0)

        total_original_correct += original_stats.get("correct", 0)
        total_original_partial += original_stats.get("partially_correct", 0)
        total_original_incorrect += original_stats.get("incorrect", 0)
        total_original_total += original_stats.get("total", 0)

        print(f"{pf.parent.name}:")
        print(f"  Prefill: {prefill_stats.get('correct_pct', 0):.1f}% correct ({prefill_stats.get('total', 0)} total)")
        print(f"  Original: {original_stats.get('correct_pct', 0):.1f}% correct ({original_stats.get('total', 0)} total)")

    print("\n" + "="*60)
    print("AGGREGATED STATISTICS")
    print("="*60)
    print("\nPrefill (truncated reasoning):")
    print(f"  Correct: {total_prefill_correct}")
    print(f"  Partially correct: {total_prefill_partial}")
    print(f"  Incorrect: {total_prefill_incorrect}")
    print(f"  Total: {total_prefill_total}")
    if total_prefill_total > 0:
        prefill_pct = 100 * total_prefill_correct / total_prefill_total
        print(f"  Accuracy: {prefill_pct:.1f}%")

    print("\nOriginal (full reasoning):")
    print(f"  Correct: {total_original_correct}")
    print(f"  Partially correct: {total_original_partial}")
    print(f"  Incorrect: {total_original_incorrect}")
    print(f"  Total: {total_original_total}")
    if total_original_total > 0:
        original_pct = 100 * total_original_correct / total_original_total
        print(f"  Accuracy: {original_pct:.1f}%")

        if total_prefill_total > 0:
            diff = prefill_pct - original_pct
            print(f"\nDifference: {diff:+.1f}% (prefill - original)")

if __name__ == "__main__":
    aggregate_prefill_stats()
