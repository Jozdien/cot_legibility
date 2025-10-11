import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.utils.io import read_json


def analyze_threshold(scores_path, threshold, model="deepseek", metric="reasoning"):
    data = read_json(scores_path)

    total_scores = 0
    above_threshold = 0

    for item in data:
        if "legibility" not in item:
            continue

        score = item["legibility"].get(f"{model}_{metric}", {}).get("score")

        if isinstance(score, (int, float)):
            total_scores += 1
            if score >= threshold:
                above_threshold += 1

    percentage = (above_threshold / total_scores * 100) if total_scores > 0 else 0

    print("\nThreshold Analysis")
    print(f"Model: {model}, Metric: {metric}")
    print(f"Threshold: {threshold}")
    print(f"Scores >= threshold: {above_threshold}/{total_scores} ({percentage:.1f}%)")

    return {"threshold": threshold, "above": above_threshold, "total": total_scores, "percentage": percentage}


def analyze_multiple_thresholds(scores_path, thresholds, model="deepseek", metric="reasoning"):
    print(f"\nMultiple Threshold Analysis ({model}_{metric})")
    print(f"File: {Path(scores_path).stem}\n")

    results = []
    for threshold in thresholds:
        result = analyze_threshold(scores_path, threshold, model, metric)
        results.append(result)

    return results


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python threshold_analysis.py <scores_file> <threshold> [model] [metric]")
        print("       python threshold_analysis.py <scores_file> <threshold1,threshold2,...> [model] [metric]")
        sys.exit(1)

    scores_path = sys.argv[1]
    threshold_arg = sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "deepseek"
    metric = sys.argv[4] if len(sys.argv) > 4 else "reasoning"

    if "," in threshold_arg:
        thresholds = [float(t) for t in threshold_arg.split(",")]
        analyze_multiple_thresholds(scores_path, thresholds, model, metric)
    else:
        analyze_threshold(scores_path, float(threshold_arg), model, metric)
