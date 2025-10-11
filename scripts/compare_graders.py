import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from src.utils.io import read_json


def extract_legibility_scores(data):
    scores_map = {}

    for item in data:
        question = item.get("question")
        if not question or "legibility" not in item:
            continue

        scores_map[question] = {}
        for key, value in item["legibility"].items():
            if isinstance(value, dict) and "score" in value:
                scores_map[question][key] = value["score"]

    return scores_map


def compare_grader_outputs(file1_path, file2_path):
    data1 = read_json(file1_path)
    data2 = read_json(file2_path)

    scores1 = extract_legibility_scores(data1)
    scores2 = extract_legibility_scores(data2)

    differences = []
    metric_diffs = {}

    for question in scores1:
        if question not in scores2:
            continue

        for metric in scores1[question]:
            if metric not in scores2[question]:
                continue

            score1 = scores1[question][metric]
            score2 = scores2[question][metric]

            if score1 == "N/A" or score2 == "N/A":
                continue

            if not isinstance(score1, (int, float)) or not isinstance(score2, (int, float)):
                continue

            diff = abs(score1 - score2)
            differences.append(diff)

            if metric not in metric_diffs:
                metric_diffs[metric] = []
            metric_diffs[metric].append(diff)

    print("\nGrader Comparison")
    print(f"File 1: {Path(file1_path).stem}")
    print(f"File 2: {Path(file2_path).stem}")

    if differences:
        print("\nOverall:")
        print(f"  Average absolute difference: {np.mean(differences):.2f}")
        print(f"  Std of differences: {np.std(differences):.2f}")
        print(f"  Max difference: {np.max(differences):.2f}")
        print(f"  Total comparisons: {len(differences)}")

    print("\nBy Metric:")
    for metric, diffs in metric_diffs.items():
        print(f"  {metric}: mean_diff={np.mean(diffs):.2f}, std={np.std(diffs):.2f}, n={len(diffs)}")

    return {"overall": differences, "by_metric": metric_diffs}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python compare_graders.py <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    compare_grader_outputs(file1_path, file2_path)
