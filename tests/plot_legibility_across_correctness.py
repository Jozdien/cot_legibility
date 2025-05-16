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
    
def analyze_distributions(correctness_scores, legibility_scores):
    # Convert to numpy arrays and group
    correct = np.array(legibility_scores)[np.array(correctness_scores) == 1]
    incorrect = np.array(legibility_scores)[np.array(correctness_scores) == 0]
    
    # Mann-Whitney U test (non-parametric)
    u_stat, p_value = stats.mannwhitneyu(correct, incorrect, alternative='two-sided')
    
    # Cohen's d effect size
    cohens_d = (np.mean(correct) - np.mean(incorrect)) / np.sqrt(
        ((len(correct) - 1) * np.var(correct) + (len(incorrect) - 1) * np.var(incorrect)) /
        (len(correct) + len(incorrect) - 2)
    )
    
    print(f"Mann-Whitney U p-value: {p_value:.4f}")
    print(f"Cohen's d: {cohens_d:.4f}")

def create_plot(correctness_scores, legibility_scores, question_indices):
    plt.figure(figsize=(10, 6))
    
    correctness = np.array(correctness_scores)
    legibility = np.array(legibility_scores)
    q_indices = np.array(question_indices)
    
    plt.boxplot([legibility[correctness == x] for x in [0, 0.5, 1]], 
                positions=[0, 0.5, 1],
                widths=0.1)
    
    # Modified color assignment
    unique_questions = np.unique(q_indices)
    n_questions = len(unique_questions)
    
    # If few questions, spread out the color ranges
    if n_questions <= 4:
        # Create spread out base colors
        base_ranges = np.linspace(0, 1, n_questions * 2 + 1)[1:-1:2]
    else:
        base_ranges = np.linspace(0, 1, n_questions)
    
    for x in [0, 0.5, 1]:
        if not any(correctness == x):
            continue
        mask = correctness == x
        y = legibility[mask]
        q = q_indices[mask]
        x_jitter = np.random.normal(0, 0.02, size=len(y)) + x
        
        xy = np.vstack([x_jitter, y])
        density = stats.gaussian_kde(xy)(xy)
        density_scaled = (density - density.min()) / (density.max() - density.min())
        
        for i, q_idx in enumerate(unique_questions):
            q_mask = q == q_idx
            base_color = plt.cm.viridis(base_ranges[i])
            
            # Vary colors within question group based on density
            color_variation = density_scaled[q_mask] * 0.2  # 20% variation
            colors = np.array(plt.cm.viridis(np.linspace(0, 1, len(unique_questions))))
            if n_questions <= 4:
                # For few questions, add/subtract from base color to stay within spread ranges
                colors = np.array([plt.cm.viridis(base_ranges[i] + (v - 0.1)) for v in color_variation])
            else:
                colors = np.array([plt.cm.viridis(base_ranges[i] + (v - 0.5) * 0.1) for v in color_variation])
            
            plt.scatter(x_jitter[q_mask], y[q_mask], c=colors, alpha=0.5,
                       label=f'Q{q_idx}' if x == 0 else "")

    plt.xticks([0, 1], ['Incorrect', 'Correct'])
    plt.ylabel('Normalized Illegibility Score (higher means less legible)')
    plt.title('Correctness vs Normalized Illegibility by Question')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.ylim(0, 9.5)
    plt.tight_layout()
    return plt

def process_data(data):
    correctness_scores = []
    normalized_legibility_scores = []
    question_indices = []
    
    for item in data:
        if not item['correctness'] or not item['legibility']:
            continue
        if not item['file'].startswith('q140_'):
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
    plt.savefig('q_repeat_temp_1.0_correctness_vs_normalized_legibility_new.png')

if __name__ == "__main__":
    main()