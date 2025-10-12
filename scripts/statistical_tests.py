import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from scipy.stats import mannwhitneyu, chi2_contingency

from src.utils.io import read_json


def mann_whitney_test(group1, group2):
    stat, p_value = mannwhitneyu(group1, group2, alternative='two-sided')
    return {"statistic": stat, "p_value": p_value}


def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std


def chi_square_test(contingency_table):
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    return {"chi2": chi2, "p_value": p_value, "dof": dof}


def compare_legibility_by_correctness(scores_path, model="deepseek", metric="reasoning"):
    data = read_json(scores_path)

    correct, partial, incorrect = [], [], []

    for item in data:
        if "legibility" not in item or "correctness" not in item:
            continue

        score = item["legibility"].get(f"{model}_{metric}", {}).get("score")
        correctness = item["correctness"].get(model, {}).get("correctness")

        if not isinstance(score, (int, float)) or correctness not in ["correct", "partially_correct", "incorrect"]:
            continue

        if correctness == "correct":
            correct.append(score)
        elif correctness == "partially_correct":
            partial.append(score)
        else:
            incorrect.append(score)

    print(f"\n{model}_{metric} - Legibility by Correctness")
    print(f"Correct: n={len(correct)}, mean={np.mean(correct):.2f}, std={np.std(correct):.2f}")
    print(f"Partial: n={len(partial)}, mean={np.mean(partial):.2f}, std={np.std(partial):.2f}")
    print(f"Incorrect: n={len(incorrect)}, mean={np.mean(incorrect):.2f}, std={np.std(incorrect):.2f}")

    if len(correct) > 1 and len(incorrect) > 1:
        mw = mann_whitney_test(correct, incorrect)
        d = cohens_d(correct, incorrect)
        print("\nCorrect vs Incorrect:")
        print(f"  Mann-Whitney U p-value: {mw['p_value']:.6f}")
        print(f"  Cohen's d: {d:.4f}")

    return {"correct": correct, "partial": partial, "incorrect": incorrect}


def compare_correctness_distributions(file1_path, file2_path, model="deepseek"):
    data1, data2 = read_json(file1_path), read_json(file2_path)

    counts1 = {"correct": 0, "partially_correct": 0, "incorrect": 0}
    counts2 = {"correct": 0, "partially_correct": 0, "incorrect": 0}

    for item in data1:
        correctness = item.get("correctness", {}).get(model, {}).get("correctness")
        if correctness in counts1:
            counts1[correctness] += 1

    for item in data2:
        correctness = item.get("correctness", {}).get(model, {}).get("correctness")
        if correctness in counts2:
            counts2[correctness] += 1

    contingency = [[counts1["correct"], counts1["partially_correct"], counts1["incorrect"]],
                   [counts2["correct"], counts2["partially_correct"], counts2["incorrect"]]]

    result = chi_square_test(contingency)

    print(f"\nCorrectness Distribution Comparison ({model})")
    print(f"File 1: {counts1}")
    print(f"File 2: {counts2}")
    print(f"Chi-square p-value: {result['p_value']:.6f}")

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python statistical_tests.py <scores_file> [model] [metric]")
        sys.exit(1)

    scores_path = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else "deepseek"
    metric = sys.argv[3] if len(sys.argv) > 3 else "reasoning"

    compare_legibility_by_correctness(scores_path, model, metric)
