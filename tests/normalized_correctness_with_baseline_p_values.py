import json
import numpy as np
import os
import re
from scipy.stats import mannwhitneyu

def get_cot_length(rollout_file, question):
    if not os.path.exists(rollout_file):
        return None
        
    with open(rollout_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r"# DeepSeek reasoning.*?\n(.*?)(?=\n---|\n# |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        reasoning = match.group(1)
        return len(reasoning.split())
    return None

def normalize_score(score, cot_length):
    if cot_length == 1:
        return score
    log_length = np.log(cot_length + 1)
    return (score / log_length) * 4.5 + 1

def process_file(file_path, baseline_correctness, rollout_base_dir):
    with open(file_path) as f:
        data = json.load(f)
    
    # Initialize score dictionaries
    scores = {
        cat: {metric: [] for metric in ['response', 'reasoning']} 
        for cat in ['correct', 'partially_correct', 'incorrect']
    }
    
    rollout_dir = os.path.join(rollout_base_dir, 
                              file_path[file_path.rfind('/')+1:file_path.rfind('_scores')])
    
    for q in data:
        if q['question'] not in baseline_correctness:
            continue
            
        cat = baseline_correctness[q['question']]
        if cat not in scores:
            continue
            
        # Get CoT length
        file = os.path.join(rollout_dir, q['file'])
        cot_length = get_cot_length(file, q['question'])
        if cot_length is None:
            continue
            
        if 'legibility' in q:
            r_score = q['legibility'].get('deepseek_response', {}).get('score')
            t_score = q['legibility'].get('deepseek_reasoning', {}).get('score')
            
            if isinstance(r_score, (int, float)):
                normalized_r = normalize_score(r_score, cot_length)
                scores[cat]['response'].append(normalized_r)
            if isinstance(t_score, (int, float)):
                normalized_t = normalize_score(t_score, cot_length)
                scores[cat]['reasoning'].append(normalized_t)
    
    return scores

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
    
    for file_path, label in zip(files, labels):
        print(f"\nP-values for {label}:")
        scores = process_file(file_path, baseline_correctness, '../r1_rollouts')
        
        # Compute p-values
        categories = [
            (scores['correct'], "correct"),
            (scores['partially_correct'], "partially_correct"),
            (scores['incorrect'], "incorrect")
        ]
        
        for metric in ['response', 'reasoning']:
            print(f"\n{metric.title()} scores:")
            for cat1, cat1_name in categories:
                for cat2, cat2_name in categories:
                    if cat1_name >= cat2_name:
                        continue
                    scores1 = cat1[metric]
                    scores2 = cat2[metric]
                    if len(scores1) > 0 and len(scores2) > 0:
                        stat, p = mannwhitneyu(scores1, scores2, alternative='two-sided')
                        print(f"{cat1_name} vs {cat2_name}: {p:.8f} (n1={len(scores1)}, n2={len(scores2)})")

if __name__ == "__main__":
    main()