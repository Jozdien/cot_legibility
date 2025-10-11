import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from src.utils.io import read_json


def grade_to_numeric(grade):
    return {"correct": 2, "partially_correct": 1, "incorrect": 0}.get(grade, -1)


def find_edge_cases(file1_path, file2_path, model1="deepseek", model2="deepseek", threshold=1):
    data1 = read_json(file1_path)
    data2 = read_json(file2_path)

    questions1 = {item["question"]: item for item in data1 if "question" in item}
    questions2 = {item["question"]: item for item in data2 if "question" in item}

    better_in_1, better_in_2, tied = [], [], []

    for question in questions1:
        if question not in questions2:
            continue

        grade1 = grade_to_numeric(questions1[question].get("correctness", {}).get(model1, {}).get("correctness"))
        grade2 = grade_to_numeric(questions2[question].get("correctness", {}).get(model2, {}).get("correctness"))

        if grade1 == -1 or grade2 == -1:
            continue

        diff = grade1 - grade2

        if diff >= threshold:
            better_in_1.append({
                "question": question,
                "grade_1": grade1,
                "grade_2": grade2,
                "diff": diff
            })
        elif diff <= -threshold:
            better_in_2.append({
                "question": question,
                "grade_1": grade1,
                "grade_2": grade2,
                "diff": diff
            })
        else:
            tied.append({
                "question": question,
                "grade_1": grade1,
                "grade_2": grade2
            })

    print(f"\nEdge Case Analysis ({Path(file1_path).stem} vs {Path(file2_path).stem})")
    print(f"Better in File 1: {len(better_in_1)}")
    print(f"Better in File 2: {len(better_in_2)}")
    print(f"Tied: {len(tied)}")

    return {"better_in_1": better_in_1, "better_in_2": better_in_2, "tied": tied}


def analyze_legibility_for_edges(scores_path, edge_cases, model="deepseek", metric="reasoning"):
    data = read_json(scores_path)
    questions_map = {item["question"]: item for item in data if "question" in item}

    for category in ["better_in_1", "better_in_2"]:
        scores = []
        for case in edge_cases[category]:
            question = case["question"]
            if question not in questions_map:
                continue

            score = questions_map[question].get("legibility", {}).get(f"{model}_{metric}", {}).get("score")
            if isinstance(score, (int, float)):
                scores.append(score)

        if scores:
            print(f"\n{category} - {model}_{metric} legibility:")
            print(f"  Mean: {np.mean(scores):.2f}, Std: {np.std(scores):.2f}, n={len(scores)}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python find_edge_cases.py <file1> <file2> [threshold]")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    threshold = int(sys.argv[3]) if len(sys.argv) > 3 else 1

    edges = find_edge_cases(file1_path, file2_path, threshold=threshold)

    if len(sys.argv) > 4:
        analyze_legibility_for_edges(sys.argv[4], edges)
