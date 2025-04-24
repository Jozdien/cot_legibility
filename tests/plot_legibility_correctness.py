# Script that plots legibility scores based on whether deepseek got them correct, partially correct, or incorrect.
# Based on `tests/find_edge_qs.py`, though it writes its own functions.

import json
import numpy as np
import matplotlib.pyplot as plt

# Load deepseek scores
with open('../scores/cutoff_0.25_openrouter_scores.json', 'r') as f:
    deepseek_scores = json.load(f)

# Group questions by correctness
correct_legibility = {
    "deepseek_response": [], "deepseek_reasoning": [],
    "cutoff_response": [], "cutoff_reasoning": [],
    "anthropic_response": [], "anthropic_reasoning": [],
    "openai_response": [], "openai_reasoning": []
}
partially_correct_legibility = {k: [] for k in correct_legibility}
incorrect_legibility = {k: [] for k in correct_legibility}

# Categorize questions and extract legibility scores
for q_data in deepseek_scores:
    correctness = q_data['correctness']['deepseek']['correctness']
    target_dict = correct_legibility if correctness == "correct" else \
                 partially_correct_legibility if correctness == "partially_correct" else \
                 incorrect_legibility
    
    for metric_type in ["response", "reasoning"]:
        for model in ["deepseek", "cutoff", "anthropic", "openai"]:
            key = f"{model}_{metric_type}"
            score_key = f"{model}_{metric_type}"
            if score_key in q_data['legibility']:
                score = q_data['legibility'][score_key]['score']
                if score is not None and score != "N/A":
                    target_dict[key].append(score)

# Calculate means and standard deviations
categories = ["Correct", "Partially Correct", "Incorrect"]
legibility_dicts = [correct_legibility, partially_correct_legibility, incorrect_legibility]

# Prepare data for plotting
x = np.arange(len(categories))
width = 0.1
metrics = list(correct_legibility.keys())
colors = plt.cm.tab10(np.linspace(0, 1, len(metrics)))

# Create plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, metric in enumerate(metrics):
    means = [np.mean(d[metric]) if d[metric] else 0 for d in legibility_dicts]
    stds = [np.std(d[metric]) if len(d[metric]) > 1 else 0 for d in legibility_dicts]
    
    position = x + (i - len(metrics)/2 + 0.5) * width
    ax.bar(position, means, width, label=metric, color=colors[i], alpha=0.7)
    ax.errorbar(position, means, yerr=stds, ecolor='black', capsize=3, alpha=0.7, linestyle='none')

# Add labels and legend
ax.set_ylabel('Legibility Score')
ax.set_title('Legibility by DeepSeek Correctness')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend(title='Metric', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_ylim(0, 9.5)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('legibility_by_correctness.png')