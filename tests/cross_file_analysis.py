import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from src.utils.io import read_json


def compare_questions_across_files(file_paths):
    all_questions = {}

    for file_path in file_paths:
        data = read_json(file_path)
        label = Path(file_path).stem

        for item in data:
            question = item.get("question")
            if not question:
                continue

            if question not in all_questions:
                all_questions[question] = {}

            all_questions[question][label] = item

    shared_questions = [q for q, files in all_questions.items() if len(files) == len(file_paths)]

    print("\nCross-File Analysis")
    print(f"Total files: {len(file_paths)}")
    print(f"Questions shared across all files: {len(shared_questions)}/{len(all_questions)}")

    return shared_questions, all_questions


def compare_correctness_consistency(file_paths, model="deepseek"):
    shared_questions, all_questions = compare_questions_across_files(file_paths)

    consistent_correct = 0
    consistent_incorrect = 0
    inconsistent = 0

    for question in shared_questions:
        grades = []
        for label, item in all_questions[question].items():
            grade = item.get("correctness", {}).get(model, {}).get("correctness")
            grades.append(grade)

        unique_grades = set(g for g in grades if g)

        if len(unique_grades) == 1:
            if "correct" in unique_grades:
                consistent_correct += 1
            else:
                consistent_incorrect += 1
        else:
            inconsistent += 1

    print(f"\nCorrectness Consistency ({model}):")
    print(f"  Consistently correct: {consistent_correct}")
    print(f"  Consistently incorrect/partial: {consistent_incorrect}")
    print(f"  Inconsistent: {inconsistent}")

    return {"consistent_correct": consistent_correct,
            "consistent_incorrect": consistent_incorrect,
            "inconsistent": inconsistent}


def compare_legibility_across_files(file_paths, model="deepseek", metric="reasoning"):
    shared_questions, all_questions = compare_questions_across_files(file_paths)

    scores_by_file = {Path(fp).stem: [] for fp in file_paths}

    for question in shared_questions:
        for label, item in all_questions[question].items():
            score = item.get("legibility", {}).get(f"{model}_{metric}", {}).get("score")
            if isinstance(score, (int, float)):
                scores_by_file[label].append(score)

    print(f"\nLegibility Comparison ({model}_{metric}):")
    for label, scores in scores_by_file.items():
        if scores:
            print(f"  {label}: mean={np.mean(scores):.2f}, std={np.std(scores):.2f}, n={len(scores)}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python cross_file_analysis.py <file1> <file2> [file3 ...]")
        sys.exit(1)

    file_paths = sys.argv[1:]

    compare_questions_across_files(file_paths)
    compare_correctness_consistency(file_paths)
    compare_legibility_across_files(file_paths)
