import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from src.utils.io import read_json, write_json


def normalize_score(score, length, method="log", scale=4.5, offset=1.0):
    if length <= 1:
        return score

    if method == "log":
        return (score / np.log(length + 1)) * scale + offset
    elif method == "linear":
        return (score / length) * scale
    else:
        raise ValueError(f"Unknown normalization method: {method}")


def normalize_legibility_scores(scores_path, length_key="words", method="log", output_path=None):
    data = read_json(scores_path)

    for item in data:
        if "legibility" not in item or "cot_length" not in item:
            continue

        length = item["cot_length"].get(length_key)
        if not length:
            continue

        for metric_key, metric_data in item["legibility"].items():
            score = metric_data.get("score")
            if not isinstance(score, (int, float)):
                continue

            normalized = normalize_score(score, length, method)
            metric_data["normalized_score"] = normalized

    if output_path:
        write_json(output_path, data)

    return data


def compare_normalized_vs_raw(scores_path, model="deepseek", metric="reasoning"):
    data = read_json(scores_path)

    raw_scores, normalized_scores = [], []

    for item in data:
        if "legibility" not in item:
            continue

        metric_data = item["legibility"].get(f"{model}_{metric}", {})
        raw = metric_data.get("score")
        normalized = metric_data.get("normalized_score")

        if isinstance(raw, (int, float)) and isinstance(normalized, (int, float)):
            raw_scores.append(raw)
            normalized_scores.append(normalized)

    if raw_scores:
        print(f"\n{model}_{metric} - Raw vs Normalized Scores")
        print(f"Raw: mean={np.mean(raw_scores):.2f}, std={np.std(raw_scores):.2f}")
        print(f"Normalized: mean={np.mean(normalized_scores):.2f}, std={np.std(normalized_scores):.2f}")
        print(f"Correlation: {np.corrcoef(raw_scores, normalized_scores)[0, 1]:.4f}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python normalize_scores.py <scores_file_with_lengths> [output_file]")
        sys.exit(1)

    scores_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    data = normalize_legibility_scores(scores_path, output_path=output_path)
    compare_normalized_vs_raw(scores_path)
