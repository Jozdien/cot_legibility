import json
import matplotlib.pyplot as plt
import numpy as np

def plot_legibility_comparison(file_paths, title="Legibility Comparison"):
    plt.figure(figsize=(4 * len(file_paths), 6))
    files_data = []
    labels = []
    
    for file_path in file_paths:
        with open(file_path) as f:
            data = json.load(f)
        if file_path[file_path.rfind('/')+1:].startswith("r1_zero"):
            labels.append("R1-Zero")
        elif file_path[file_path.rfind('/')+1:].startswith("v3"):
            labels.append("V3")
        elif file_path[file_path.rfind('/')+1:].startswith("llama_70b"):
            labels.append("Llama 70B")
        else:
            labels.append("R1")
        scores = {
            'response': [],
            'reasoning': []
        }
        for result in data:
            if 'legibility' in result:
                r_score = result['legibility'].get('deepseek_response', {}).get('score')
                t_score = result['legibility'].get('deepseek_reasoning', {}).get('score')
                if isinstance(r_score, (int, float)): scores['response'].append(r_score)
                if isinstance(t_score, (int, float)): scores['reasoning'].append(t_score)
        
        if scores['response'] or scores['reasoning']:
            files_data.append({
                'response_mean': np.mean(scores['response']) if scores['response'] else 0,
                'response_std': np.std(scores['response']) if len(scores['response']) > 1 else 0,
                'reasoning_mean': np.mean(scores['reasoning']) if scores['reasoning'] else 0,
                'reasoning_std': np.std(scores['reasoning']) if len(scores['reasoning']) > 1 else 0,
                'n': min(len(scores['response']), len(scores['reasoning']))
            })

    bar_width = 0.35
    positions = np.arange(len(files_data))

    for i, (pos, data) in enumerate(zip(positions, files_data)):
        plt.bar(pos, data['response_mean'], bar_width, color='#0273b2', 
                yerr=data['response_std'], capsize=5, label='Response' if i==0 else None)
        plt.bar(pos + bar_width, data['reasoning_mean'], bar_width, color='#d65e00',
                yerr=data['reasoning_std'], capsize=5, label='Reasoning' if i==0 else None)

    plt.ylabel('Illegibility Score')
    plt.title(title)
    plt.xticks(positions + bar_width/2, labels)
    plt.ylim(0, 9.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{title}.png')

# Usage example:
plot_legibility_comparison(
    ['../scores/cutoff_0.25_openrouter_scores.json', 
     '../scores/r1_zero_only_temp_1.0_scores.json',
     '../scores/v3_only_temp_1.0_scores.json',])
