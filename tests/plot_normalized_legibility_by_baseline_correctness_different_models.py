import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import re

def setup_matplotlib():
    """Set up matplotlib with custom fonts and style."""
    fm.fontManager.addfont('../fonts/Montserrat-Regular.ttf')
    plt.rcParams['font.family'] = 'Montserrat'
    plt.rcParams['hatch.linewidth'] = 1

def get_cot_length(rollout_file, question):
    if not os.path.exists(rollout_file):
        print(f"Rollout file {rollout_file} does not exist")
        return None
        
    with open(rollout_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract reasoning section using regex
    pattern = r"# DeepSeek reasoning.*?\n(.*?)(?=\n---|\n# |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        reasoning = match.group(1)
        return len(reasoning.split())
    return None

def plot_legibility_by_baseline(file_paths, baseline_path='../scores/temp_0_cutoff_0.25_openrouter_scores.json', title="Legibility by Baseline Correctness"):
    # Load baseline data
    with open(baseline_path) as f:
        baseline = {q['question']: q['correctness']['deepseek']['correctness'] 
                   for q in json.load(f) if 'correctness' in q}

    # Process each file
    files_data = []
    labels = []
    for file_path in file_paths:
        with open(file_path) as f:
            data = json.load(f)
        
        # Initialize scores dictionary
        scores = {cat: {'response': [], 'reasoning': [], 'lengths': []} 
                 for cat in ['correct', 'partially_correct', 'incorrect']}
        
        # Collect scores by baseline correctness
        for q in data:
            rollout_dir = os.path.join('../r1_rollouts', file_path[file_path.rfind('/')+1:file_path.rfind('_scores')])
            file = os.path.join(rollout_dir, q['file'])
            if q['question'] not in baseline:
                continue
            cat = baseline[q['question']]
            if cat not in scores:
                continue
                
            # Get CoT length
            cot_length = get_cot_length(file, q['question'])
            if cot_length is None:
                continue
                
            if 'legibility' in q:
                r_score = q['legibility'].get('deepseek_response', {}).get('score')
                t_score = q['legibility'].get('deepseek_reasoning', {}).get('score')
                
                # Normalize scores by log length and scale to 1-10 range
                log_length = np.log(cot_length + 1)  # Add 1 to avoid log(0)

                if cot_length == 1:
                    scores[cat]['response'].append(r_score) if isinstance(r_score, (int, float)) else 0
                    scores[cat]['reasoning'].append(t_score) if isinstance(t_score, (int, float)) else 0
                    scores[cat]['lengths'].append(cot_length)
                    continue

                if isinstance(r_score, (int, float)): 
                    # Scale to 1-10: normalize by log length, then scale and shift
                    normalized_score = (r_score / log_length) * 4.5 + 1
                    scores[cat]['response'].append(normalized_score)
                if isinstance(t_score, (int, float)): 
                    normalized_score = (t_score / log_length) * 4.5 + 1
                    scores[cat]['reasoning'].append(normalized_score)
                scores[cat]['lengths'].append(cot_length)
        
        # Calculate means and stds
        stats = {}
        for cat in scores:
            stats[cat] = {
                'response_mean': np.mean(scores[cat]['response']) if scores[cat]['response'] else 0,
                'response_std': np.std(scores[cat]['response']) if len(scores[cat]['response']) > 1 else 0,
                'reasoning_mean': np.mean(scores[cat]['reasoning']) if scores[cat]['reasoning'] else 0,
                'reasoning_std': np.std(scores[cat]['reasoning']) if len(scores[cat]['reasoning']) > 1 else 0,
                'n': len(scores[cat]['response'])
            }
        files_data.append(stats)
        if file_path[file_path.rfind('/')+1:].startswith("r1_zero"):
            labels.append("R1-Zero")
        elif file_path[file_path.rfind('/')+1:].startswith("v3"):
            labels.append("V3")
        elif file_path[file_path.rfind('/')+1:].startswith("llama_70b"):
            labels.append("Llama 70B")
        else:
            labels.append("R1")

    # Rest of plotting code remains the same
    plt.figure(figsize=(15, 6))
    width = 0.15
    x = np.arange(len(labels)) * 1.25
    
    colors = {'response': '#0273b2', 'reasoning': '#d65e00'}
    hatches = {'correct': '', 'partially_correct': '///', 'incorrect': 'xxx'}
    
    for i, cat in enumerate(['correct', 'partially_correct', 'incorrect']):
        for j, typ in enumerate(['response', 'reasoning']):
            means = [d[cat][f'{typ}_mean'] for d in files_data]
            stds = [d[cat][f'{typ}_std'] for d in files_data]
            pos = x + (i*2*1.2 + j)*width - 2*width
            
            bars = plt.bar(pos, means, width, color=colors[typ], 
                          yerr=stds, capsize=3, alpha=1,
                          label=f'{cat.replace("_", " ").title()} ({typ.title()})')
            
            for bar in bars:
                bar.set_hatch(hatches[cat])

    plt.ylabel('Normalized Illegibility Score (1-10)')
    plt.title(title)
    plt.xticks(x, labels)
    plt.ylim(0, 10)  # Adjusted y-limit for new 1-10 scale
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('legibility_by_baseline_correctness_different_models_normalized.png')

setup_matplotlib()
plot_legibility_by_baseline(['../scores/cutoff_0.25_openrouter_scores.json', '../scores/r1_zero_only_temp_1.0_scores.json', '../scores/v3_only_temp_1.0_scores.json'])