import json
import numpy as np
from scipy.stats import mannwhitneyu

# Load scores
with open('../scores/r1_zero_only_temp_1.0_scores.json', 'r') as f:
    file1_scores = json.load(f)
with open('../scores/temp_0_cutoff_0.25_openrouter_scores.json', 'r') as f:
    file2_scores = json.load(f)

# Initialize score dictionaries
correct = {k: [] for k in ['deepseek_response', 'deepseek_reasoning', 'cutoff_response', 
    'cutoff_reasoning', 'anthropic_response', 'anthropic_reasoning', 'openai_response', 
    'openai_reasoning']}
partially_correct = {k: [] for k in correct}
incorrect = {k: [] for k in correct}

# Create correctness mapping
correctness_map = {q['question']: q['correctness']['deepseek']['correctness'] 
                  for q in file2_scores if 'correctness' in q}

# Categorize scores
for q in file1_scores:
    if q['question'] not in correctness_map:
        continue
    target = correct if correctness_map[q['question']] == "correct" else \
            partially_correct if correctness_map[q['question']] == "partially_correct" else \
            incorrect
    
    for model in ['deepseek', 'cutoff', 'anthropic', 'openai']:
        for metric in ['response', 'reasoning']:
            key = f"{model}_{metric}"
            if key in q['legibility']:
                score = q['legibility'][key].get('score')
                if score is not None and score != "N/A":
                    target[key].append(score)

# Compute p-values
categories = [(correct, "correct"), (partially_correct, "partially_correct"), (incorrect, "incorrect")]
for key in correct.keys():
    print(f"\nP-values for {key}:")
    for cat1, cat1_name in categories:
        for cat2, cat2_name in categories:
            if cat1_name >= cat2_name:
                continue
            if len(cat1[key]) > 0 and len(cat2[key]) > 0:
                stat, p = mannwhitneyu(cat1[key], cat2[key], alternative='two-sided')
                print(f"{cat1_name} vs {cat2_name}: {p:.8f}")