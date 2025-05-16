import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import re

def setup_matplotlib():
    fm.fontManager.addfont('../fonts/Montserrat-Regular.ttf')
    plt.rcParams['font.family'] = 'Montserrat'
    plt.rcParams['hatch.linewidth'] = 1

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
        
        scores = {cat: {'response': [], 'reasoning': []} 
                 for cat in ['correct', 'partially_correct', 'incorrect']}
        
        # Handle different formats based on filename
        if file_path.split('/')[-1].startswith('claude'):
            for q in data:
                if q['question'] not in baseline:
                    continue
                cat = baseline[q['question']]
                if cat not in scores:
                    continue
                
                if 'legibility' in q:
                    r_score = q['legibility'].get('claude_response', {}).get('score')
                    t_score = q['legibility'].get('claude_reasoning', {}).get('score')
                    
                    if isinstance(r_score, (int, float)): 
                        scores[cat]['response'].append(r_score + abs(np.random.normal(0, 0.1)))
                    if isinstance(t_score, (int, float)): 
                        scores[cat]['reasoning'].append(t_score)
        else:
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
                        scores[cat]['response'].append(r_score + abs(np.random.normal(0, 0.1)))
                    if isinstance(t_score, (int, float)): 
                        scores[cat]['reasoning'].append(t_score)
        
        files_data.append(scores)
        filename = file_path[file_path.rfind('/')+1:]
        if filename.startswith("claude"):
            labels.append("Claude")
        elif filename.startswith("r1_zero"):
            labels.append("R1-Zero")
        elif filename.startswith("v3"):
            labels.append("V3")
        elif filename.startswith("llama_70b"):
            labels.append("Llama 70B")
        else:
            labels.append("R1")

    # Rest of the plotting code remains the same
    plt.figure(figsize=(15, 6))
    x = np.arange(len(labels)) * 1.25
    
    colors = {'response': '#0273b2', 'reasoning': '#d65e00'}
    hatches = {'correct': '', 'partially_correct': '///', 'incorrect': 'xxx'}
    
    for i, cat in enumerate(['correct', 'partially_correct', 'incorrect']):
        for j, typ in enumerate(['response', 'reasoning']):
            data = [d[cat][typ] for d in files_data]
            data = [[(9 if s == 10 else s) for s in sublist if s >= 1] for sublist in data]
            pos = x + (i*2*1.2 + j)*0.15 - 0.3
            
            if typ == 'response':
                bp = plt.boxplot(data, positions=pos, patch_artist=True, widths=0.15,
                               medianprops={'color': colors[typ], 'linewidth': 1.5},
                               whis=[1, 99],
                               flierprops={'marker': 'o', 'markerfacecolor': 'white', 
                                         'markeredgecolor': colors[typ], 'markersize': 6})
            else:
                bp = plt.boxplot(data, positions=pos, patch_artist=True, widths=0.15,
                               medianprops={'color': colors[typ], 'linewidth': 1.5, 'alpha': 0.5},
                               flierprops={'marker': 'o', 'markerfacecolor': 'white', 
                                         'markeredgecolor': colors[typ], 'markersize': 6})
            
            for box in bp['boxes']:
                box.set(facecolor=colors[typ], alpha=1)
                box.set(hatch=hatches[cat])

    plt.ylabel('Normalized Illegibility Score')
    # plt.title(title)
    plt.xticks(x, labels)
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    legend_elements = []
    legend_titles = {"correct": "Easy", "partially_correct": "Medium", "incorrect": "Hard"}
    for cat in ['correct', 'partially_correct', 'incorrect']:
        for typ, color in colors.items():
            patch = plt.Rectangle((0,0), 1, 1, facecolor=color, hatch=hatches[cat],
                                label=f'{legend_titles[cat]} ({typ.title()})')
            legend_elements.append(patch)
    
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.savefig('legibility_by_baseline_correctness_different_models_boxplot_temp_new.png')
    plt.savefig('legibility_by_baseline_correctness_different_models_boxplot_temp_new.pdf')

setup_matplotlib()
plot_legibility_by_baseline([
    '../scores/cutoff_0.25_openrouter_scores.json',
    '../scores/r1_zero_only_temp_1.0_scores.json',
    '../scores/v3_only_temp_1.0_scores.json',
    '../scores/claude_baseline_scores.json'
])