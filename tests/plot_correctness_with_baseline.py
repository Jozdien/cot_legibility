import json
import matplotlib.pyplot as plt
import numpy as np

def analyze_correctness(data):
    models = ["deepseek", "cutoff", "anthropic", "openai"]
    stats = {}
    for model in models:
        counts = {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
        for result in data:
            assessment = result.get("correctness", {}).get(model, {})
            correctness = assessment.get("correctness", "N/A")
            if correctness in counts:
                counts[correctness] += 1
            else:
                counts["error"] += 1
        
        total = sum(counts.values())
        stats[model] = {
            **counts,
            "total": total,
            "correct_percentage": (counts["correct"] / total * 100) if total > 0 else 0,
            "partially_percentage": (counts["partially_correct"] / total * 100) if total > 0 else 0,
            "incorrect_percentage": (counts["incorrect"] / total * 100) if total > 0 else 0
        }
    return stats

# Load and analyze data
with open('../scores/cutoff_0.25_openrouter_scores.json') as f:
    data1 = json.load(f)
with open('../scores/temp_0.4_cutoff_0.25_openrouter_scores.json') as f:
    data2 = json.load(f)

stats1 = analyze_correctness(data1)
stats2 = analyze_correctness(data2)

# Plot setup
models = ["baseline", "deepseek", "cutoff", "anthropic", "openai"]
width = 0.25
x = np.arange(len(models))

# Extract percentages
correct = [stats2["deepseek"]["correct_percentage"] if m == "baseline" else stats1[m]["correct_percentage"] for m in models]
partial = [stats2["deepseek"]["partially_percentage"] if m == "baseline" else stats1[m]["partially_percentage"] for m in models]
incorrect = [stats2["deepseek"]["incorrect_percentage"] if m == "baseline" else stats1[m]["incorrect_percentage"] for m in models]

# Create bars
plt.figure(figsize=(12, 6))
bars1 = plt.bar(x - width, correct, width, label='Correct', color='#2ecc71', alpha=0.8)
bars2 = plt.bar(x, partial, width, label='Partially Correct', color='#f39c12', alpha=0.8)
bars3 = plt.bar(x + width, incorrect, width, label='Incorrect', color='#e74c3c', alpha=0.8)

# Add value labels
for bars, values in [(bars1, correct), (bars2, partial), (bars3, incorrect)]:
    for bar, value in zip(bars, values):
        if value > 0:
            plt.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value:.1f}%', 
                    ha='center', va='bottom', fontsize=9)

# Customize plot
plt.ylabel('Percentage (%)')
plt.title('Correctness Assessment')
plt.xticks(x, ['Baseline', 'Default', 'With Cutoff', 'With Claude Paraphrase', 'With GPT-4o Paraphrase'])
plt.legend()
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('correctness_with_baseline.png')