import json
import pandas as pd
from scipy.stats import chi2_contingency

def compare_models(file1_path, file2_path):
    # Read and parse the JSON files
    with open(file1_path) as f1, open(file2_path) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    
    # Get correctness values for each model
    models = ['deepseek', 'cutoff', 'anthropic', 'openai']
    
    results = {}
    for model in models:
        # Count occurrences in each file
        counts1 = {'correct': 0, 'partially_correct': 0, 'incorrect': 0}
        counts2 = {'correct': 0, 'partially_correct': 0, 'incorrect': 0}
        
        for item in data1:
            if item['correctness'][model]['correctness'] == 'N/A' or item['correctness'][model]['correctness'] == 'error':
                continue
            counts1[item['correctness'][model]['correctness']] += 1
        for item in data2:
            if item['correctness'][model]['correctness'] == 'N/A' or item['correctness'][model]['correctness'] == 'error':
                continue
            counts2[item['correctness'][model]['correctness']] += 1
            
        # Create contingency table
        contingency = pd.DataFrame([
            [counts1['correct'], counts1['partially_correct'], counts1['incorrect']],
            [counts2['correct'], counts2['partially_correct'], counts2['incorrect']]
        ])
        
        # Perform chi-square test
        chi2, p_val, _, _ = chi2_contingency(contingency)
        results[model] = {
            'p_value': p_val,
            'file1_counts': counts1,
            'file2_counts': counts2
        }
    
    return results

results = compare_models('../scores/cutoff_0.25_openrouter_scores.json', '../scores/temp_0_cutoff_0.25_openrouter_scores.json')
for model, result in results.items():
    print(f"{model}: {result['p_value']}")
