import numpy as np
import json
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import re

def setup_matplotlib():
    fm.fontManager.addfont('../fonts/Montserrat-Regular.ttf')
    plt.rcParams['font.family'] = 'Montserrat'
    plt.rcParams['hatch.linewidth'] = 1

def score_correctness(correctness):
    return {
        "correct": 1,
        "partially_correct": 0.5,
        "incorrect": 0
    }.get(correctness, 0)

def get_reasoning_length(filename):
    try:
        with open(os.path.join('../r1_rollouts/q_repeat_temp_1.0', filename), 'r') as f:
            content = f.read()
            # Find the start of reasoning section
            reasoning_start = content.find("DeepSeek reasoning (via openrouter)")
            if reasoning_start == -1:
                return None
            reasoning = content[reasoning_start:].strip()
            return len(reasoning) / 10000
    except:
        return None
    
def analyze_distributions(correctness_scores, legibility_scores, question_indices=None, specific_q=None):
    # Filter for specific question if provided
    if specific_q is not None and question_indices is not None:
        mask = question_indices == specific_q
        correctness_scores = np.array(correctness_scores)[mask]
        legibility_scores = np.array(legibility_scores)[mask]
    
    # Convert to numpy arrays and group
    correct = np.array(legibility_scores)[np.array(correctness_scores) == 1]
    incorrect = np.array(legibility_scores)[np.array(correctness_scores) == 0]
    
    if len(correct) < 2 or len(incorrect) < 2:
        return None, None
    
    # Mann-Whitney U test (non-parametric)
    u_stat, p_value = stats.mannwhitneyu(correct, incorrect, alternative='two-sided')
    
    # Cohen's d effect size
    cohens_d = (np.mean(correct) - np.mean(incorrect)) / np.sqrt(
        ((len(correct) - 1) * np.var(correct) + (len(incorrect) - 1) * np.var(incorrect)) /
        (len(correct) + len(incorrect) - 2)
    )
    
    return p_value, cohens_d

def create_plot(correctness_scores, legibility_scores, question_indices):
    unique_questions = np.unique(question_indices)
    n_questions = len(unique_questions)
    
    # Print overall statistics
    p_val, d = analyze_distributions(correctness_scores, legibility_scores)
    print(f"\nOverall statistics:")
    print(f"Mann-Whitney U p-value: {p_val:.4f}")
    print(f"Cohen's d: {d:.4f}")
    
    # Print per-question statistics
    print("\nPer-question statistics:")
    for q_idx in unique_questions:
        p_val, d = analyze_distributions(correctness_scores, legibility_scores, question_indices, q_idx)
        if p_val is not None:
            print(f"\nQuestion {q_idx}:")
            print(f"Mann-Whitney U p-value: {p_val:.4f}")
            print(f"Cohen's d: {d:.4f}")
        else:
            print(f"\nQuestion {q_idx}: Insufficient data for statistical analysis")
    
    # Rest of the plotting code remains the same
    n_cols = min(3, n_questions)
    n_rows = (n_questions + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
    if n_rows == 1 and n_cols == 1:
        axes = np.array([axes])
    axes = axes.flatten()
    
    for idx, q_idx in enumerate(unique_questions):
        ax = axes[idx]
        mask = question_indices == q_idx
        q_correctness = np.array(correctness_scores)[mask]
        q_legibility = np.array(legibility_scores)[mask]
        
        ax.boxplot([q_legibility[q_correctness == x] for x in [0, 0.5, 1]], 
                  positions=[0, 0.5, 1],
                  widths=0.1)
        
        for x in [0, 0.5, 1]:
            if not any(q_correctness == x):
                continue
            submask = q_correctness == x
            y = q_legibility[submask]
            if len(y) > 1:
                x_jitter = np.random.normal(0, 0.02, size=len(y)) + x
                xy = np.vstack([x_jitter, y])
                density = stats.gaussian_kde(xy)(xy)
                density_scaled = (density - density.min()) / (density.max() - density.min())
                ax.scatter(x_jitter, y, c=plt.cm.viridis(density_scaled), alpha=0.5)
        
        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(['Incorrect', 'Partial', 'Correct'])
        ax.set_title(f'Question {q_idx}')
        ax.set_ylim(0, 9.5)
        ax.grid(True, linestyle='--', alpha=0.3)
        
    for idx in range(len(unique_questions), len(axes)):
        axes[idx].set_visible(False)
        
    fig.supylabel('Normalized Illegibility Score')
    plt.tight_layout()
    return plt

def process_data(data):
    correctness_scores = []
    normalized_legibility_scores = []
    question_indices = []
    
    for item in data:
        if not item['correctness'] or not item['legibility']:
            continue
            
        # Extract question index
        q_match = re.match(r'q(\d+)_', item['file'])
        if not q_match:
            continue
        q_idx = int(q_match.group(1))
            
        reasoning_length = get_reasoning_length(item['file'])
        if not reasoning_length:
            continue
            
        correctness = score_correctness(item['correctness']['deepseek']['correctness'])
        legibility = item['legibility']['deepseek_reasoning']['score']
        
        normalized_legibility = (legibility / reasoning_length) * 4
        if normalized_legibility > 9:
            continue
        
        correctness_scores.append(correctness)
        normalized_legibility_scores.append(normalized_legibility)
        question_indices.append(q_idx)
    
    return correctness_scores, normalized_legibility_scores, question_indices

def main():
    setup_matplotlib()
    with open('../scores/q_repeat_temp_1.0_scores.json', 'r') as f:
        data = json.load(f)
    
    correctness_scores, normalized_legibility_scores, question_indices = process_data(data)
    plt = create_plot(correctness_scores, normalized_legibility_scores, question_indices)
    analyze_distributions(correctness_scores, normalized_legibility_scores)
    plt.savefig('q_repeat_temp_1.0_correctness_vs_normalized_legibility_facet.png')

if __name__ == "__main__":
    main()