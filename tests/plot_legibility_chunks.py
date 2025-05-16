import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from collections import defaultdict

def setup_matplotlib():
    fm.fontManager.addfont('../fonts/Montserrat-Regular.ttf')
    plt.rcParams['font.family'] = 'Montserrat'
    plt.rcParams['hatch.linewidth'] = 1

def plot_multiple_files(filepaths):
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    # axes = axes.ravel()

    colors = {
        'DeepSeek R1': '#3498db', 
        'DeepSeek R1-Zero': '#2ecc71', 
        'DeepSeek V3': '#9b59b6', 
        'Claude 3.7 Sonnet': '#e74c3c'
    }
    
    for idx, filepath in enumerate(filepaths):
        with open(filepath) as f:
            data = json.load(f)

        title_map = {
            '../scores/cutoff_0.25_openrouter_legibility_chunks_scores.json': 'DeepSeek R1',
            '../scores/r1_zero_only_temp_1.0_legibility_chunks_scores.json': 'DeepSeek R1-Zero',
            '../scores/v3_only_temp_1.0_legibility_chunks_scores.json': 'DeepSeek V3',
            '../scores/claude_baseline_legibility_chunks_scores.json': 'Claude 3.7 Sonnet'
        }
        
        # Collect scores by chunk position
        chunk_scores = defaultdict(list)
        if filepath.split('/')[-1].startswith('claude'):
            # Handle Claude format
            for item in data:
                chunks = item.get('legibility', {}).get('claude_reasoning', {}).get('chunk_grades', [])
                for i, chunk in enumerate(chunks):
                    chunk_scores[i].append(chunk['score'])
        else:
            for file_data in data:
                chunks = file_data['sections'].get('deepseek_reasoning', {}).get('chunk_grades', [])
                for i, chunk in enumerate(chunks):
                    chunk_scores[i].append(chunk['score'])
        
        scores_list = [scores for scores in chunk_scores.values()]
        positions = range(len(scores_list))
        
        ax.boxplot(scores_list, patch_artist=True, boxprops=dict(facecolor=colors[title_map[filepath]], color=colors[title_map[filepath]], alpha=0.6),
                          medianprops=dict(color=colors[title_map[filepath]]))
        ax.set_xlabel('Characters')
        ax.set_ylabel('Illegibility Score')
        # ax.set_title(f'{title_map[filepath]}')
        ax.set_xticks(positions)
        if filepath.startswith('../scores/v3_only_temp_1.0_legibility_chunks_scores.json'):
            ax.set_xticklabels([i * 500 if i % 2 == 0 else "" for i in range(len(positions))])
        else:
            ax.set_xticklabels([i * 5000 for i in range(len(positions))])
        ax.grid(True)
    
    plt.tight_layout()
    plt.savefig('comparison.png')
    plt.savefig('comparison.pdf')

# Usage:
filepaths = ['../scores/cutoff_0.25_openrouter_legibility_chunks_scores.json']
setup_matplotlib()
plot_multiple_files(filepaths)