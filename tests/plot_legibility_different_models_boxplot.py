import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def setup_matplotlib():
    """Set up matplotlib with custom fonts and style."""
    fm.fontManager.addfont('../fonts/Montserrat-Regular.ttf')
    plt.rcParams['font.family'] = 'Montserrat'
    plt.rcParams['hatch.linewidth'] = 1

def plot_legibility_comparison(file_paths, title="Legibility Comparison"):
    plt.figure(figsize=(12, 6))
    
    # Collect data for each model
    model_data = {}
    labels = []
    
    for file_path in file_paths:
        # Extract model name from file path
        if "r1_zero" in file_path:
            label = "R1-Zero"
        elif "v3" in file_path:
            label = "V3"
        elif "llama_70b" in file_path:
            label = "Llama 70B"
        elif "claude" in file_path:
            label = "Claude 3.7 Sonnet"
        else:
            label = "R1"
        labels.append(label)
        
        # Load and process data
        with open(file_path) as f:
            data = json.load(f)
        
        scores = {'response': [], 'reasoning': []}
        for result in data:
            if 'legibility' in result:
                if "claude" in file_path:
                    r_score = result['legibility'].get('claude_response', {}).get('score')
                    t_score = result['legibility'].get('claude_reasoning', {}).get('score')
                else:
                    r_score = result['legibility'].get('deepseek_response', {}).get('score')
                    t_score = result['legibility'].get('deepseek_reasoning', {}).get('score')
                if isinstance(r_score, (int, float)): 
                    if r_score == 10:
                        r_score = 9
                    if r_score == 0:
                        continue
                    scores['response'].append(r_score)
                if isinstance(t_score, (int, float)): 
                    if t_score == 10:
                        t_score = 9
                    if t_score == 0:
                        continue
                    scores['reasoning'].append(t_score)
        
        model_data[label] = scores

    # Sort labels consistently
    labels = sorted(labels, key=lambda x: ["R1", "R1-Zero", "V3", "Llama 70B", "Claude 3.7 Sonnet"].index(x))
    
    # Prepare data for plotting
    response_data = [[val + abs(np.random.normal(0, 0.1)) for val in model_data[label]['response']] for label in labels]
    reasoning_data = [model_data[label]['reasoning'] for label in labels]
    
    # Set positions for boxes
    positions = np.arange(len(labels)) * 3
    
    # Create box plots
    bp_response = plt.boxplot(response_data, positions=positions, 
                            patch_artist=True, widths=0.7,
                            medianprops={'color': '#0273b2', 'linewidth': 1.5},
                            whis=[1, 99],
                            flierprops={'marker': 'o', 'markerfacecolor': 'white', 
                                      'markeredgecolor': '#0273b2', 'markersize': 6})
    bp_reasoning = plt.boxplot(reasoning_data, positions=positions + 1, 
                             patch_artist=True, widths=0.7,
                             flierprops={'marker': 'o', 'markerfacecolor': 'white', 
                                       'markeredgecolor': '#d65e00', 'markersize': 6})
    
    # Style boxes
    for box in bp_response['boxes']:
        box.set(facecolor='#0273b2', alpha=1)
    for box in bp_reasoning['boxes']:
        box.set(facecolor='#d65e00', alpha=1)
    
    # Customize plot
    plt.ylabel('Illegibility Score', fontsize=12)
    plt.title('CoT Illegibility Scores Distribution', fontsize=14)
    plt.xticks(positions + 0.5, labels)
    plt.ylim(0, 9.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add legend
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, facecolor='#0273b2', label='Response'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#d65e00', label='Reasoning')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig(f'{title}.png')
    plt.close()

setup_matplotlib()
# Usage example:
plot_legibility_comparison([
    '../scores/cutoff_0.25_openrouter_scores.json', 
    '../scores/r1_zero_only_temp_1.0_scores.json',
    '../scores/claude_baseline_scores.json'
])