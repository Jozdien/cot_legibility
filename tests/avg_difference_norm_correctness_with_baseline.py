import json
import numpy as np
import os
from normalized_correctness_with_baseline_p_values import get_cot_length, normalize_score, process_file

def compute_differences(scores):
    differences = {}
    for metric in ['response', 'reasoning']:
        correct_avg = np.mean(scores['correct'][metric]) if scores['correct'][metric] else np.nan
        incorrect_avg = np.mean(scores['incorrect'][metric]) if scores['incorrect'][metric] else np.nan
        diff = correct_avg - incorrect_avg
        differences[metric] = {
            'difference': diff,
            'correct_avg': correct_avg,
            'incorrect_avg': incorrect_avg,
            'correct_n': len(scores['correct'][metric]),
            'incorrect_n': len(scores['incorrect'][metric])
        }
    return differences

def main():
    # Load baseline correctness
    baseline_path = '../scores/temp_0_cutoff_0.25_openrouter_scores.json'
    with open(baseline_path) as f:
        baseline_correctness = {q['question']: q['correctness']['deepseek']['correctness'] 
                              for q in json.load(f) if 'correctness' in q}

    # Files to process
    files = [
        '../scores/cutoff_0.25_openrouter_scores.json',
        '../scores/r1_zero_only_temp_1.0_scores.json',
        '../scores/v3_only_temp_1.0_scores.json'
    ]
    
    labels = ["R1", "R1-Zero", "V3"]
    
    print("Differences between correct and incorrect scores:")
    print("================================================")
    
    for file_path, label in zip(files, labels):
        print(f"\n{label}:")
        scores = process_file(file_path, baseline_correctness, '../r1_rollouts')
        differences = compute_differences(scores)
        
        for metric in ['response', 'reasoning']:
            diff_data = differences[metric]
            print(f"\n{metric.title()}:")
            print(f"Correct avg: {diff_data['correct_avg']:.3f} (n={diff_data['correct_n']})")
            print(f"Incorrect avg: {diff_data['incorrect_avg']:.3f} (n={diff_data['incorrect_n']})")
            print(f"Difference (correct - incorrect): {diff_data['difference']:.3f}")

if __name__ == "__main__":
    main()