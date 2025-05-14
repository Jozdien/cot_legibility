import json
from collections import defaultdict

def compare_correctness_scores(file1_path, file2_path):
    # Load both files
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    
    # Create dictionaries to map questions to their correctness scores
    scores1 = {}
    scores2 = {}
    
    # Process first file
    for item in data1:
        if 'question' in item and 'correctness' in item:
            deepseek_score = item['correctness'].get('deepseek', {}).get('correctness')
            if deepseek_score != 'N/A' and deepseek_score != 'error':
                scores1[item['question']] = deepseek_score
    
    # Process second file
    for item in data2:
        if 'question' in item and 'correctness' in item:
            deepseek_score = item['correctness'].get('deepseek', {}).get('correctness')
            if item['question'] in scores1:  # Only include if question exists in file1
                scores2[item['question']] = deepseek_score if deepseek_score not in ['N/A', 'error'] else None
    
    # Compare scores
    comparison_stats = defaultdict(lambda: defaultdict(int))
    total_compared = 0
    
    for question in scores1:
        if question in scores2 and scores2[question] is not None:
            comparison_stats[scores1[question]][scores2[question]] += 1
            total_compared += 1
    
    # Print results
    print(f"\nTotal questions compared: {total_compared}")
    print("\nDetailed comparison:")
    print("-" * 50)
    
    categories = ['correct', 'partially_correct', 'incorrect']
    
    # Print header
    print(f"{'File 1 \\ File 2':<20}", end='')
    for cat2 in categories:
        print(f"{cat2:>15}", end='')
    print()
    print("-" * 65)
    
    # Print comparison matrix
    for cat1 in categories:
        print(f"{cat1:<20}", end='')
        for cat2 in categories:
            count = comparison_stats[cat1][cat2]
            percentage = (count / total_compared * 100) if total_compared > 0 else 0
            print(f"{count:>8} ({percentage:>5.1f}%)", end='')
        print()

if __name__ == "__main__":
    file1 = "../scores/cutoff_0.25_openrouter_scores.json"
    file2 = "../scores/r1_zero_only_temp_1.0_scores.json"
    compare_correctness_scores(file1, file2)