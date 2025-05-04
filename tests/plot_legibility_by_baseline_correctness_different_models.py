import json
import numpy as np
import matplotlib.pyplot as plt

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
        scores = {cat: {'response': [], 'reasoning': []} 
                 for cat in ['correct', 'partially_correct', 'incorrect']}
        
        # Collect scores by baseline correctness
        for q in data:
            if q['question'] not in baseline:
                continue
            cat = baseline[q['question']]
            if cat not in scores:
                continue
                
            if 'legibility' in q:
                r_score = q['legibility'].get('deepseek_response', {}).get('score')
                t_score = q['legibility'].get('deepseek_reasoning', {}).get('score')
                if isinstance(r_score, (int, float)): 
                    scores[cat]['response'].append(r_score)
                if isinstance(t_score, (int, float)): 
                    scores[cat]['reasoning'].append(t_score)
        
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

    # Plotting
    plt.figure(figsize=(15, 6))
    width = 0.15
    x = np.arange(len(labels)) * 1.25
    
    # Define styles
    colors = {'response': '#0273b2', 'reasoning': '#d65e00'}
    hatches = {'correct': '', 'partially_correct': '///', 'incorrect': 'xxx'}
    
    # Plot bars for each category
    for i, cat in enumerate(['correct', 'partially_correct', 'incorrect']):
        for j, typ in enumerate(['response', 'reasoning']):
            means = [d[cat][f'{typ}_mean'] for d in files_data]
            stds = [d[cat][f'{typ}_std'] for d in files_data]
            pos = x + (i*2*1.2 + j)*width - 2*width
            
            bars = plt.bar(pos, means, width, color=colors[typ], 
                          yerr=stds, capsize=3, alpha=1,
                          label=f'{cat.replace("_", " ").title()} ({typ.title()})')
            
            # Add hatching
            for bar in bars:
                bar.set_hatch(hatches[cat])

    plt.ylabel('Illegibility Score')
    plt.title(title)
    plt.xticks(x, labels)
    plt.ylim(0, 9.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('legibility_by_baseline_correctness_different_models.png')

# Usage example:
plot_legibility_by_baseline(['../scores/cutoff_0.25_openrouter_scores.json', '../scores/r1_zero_only_temp_1.0_scores.json', '../scores/v3_only_temp_1.0_scores.json'])