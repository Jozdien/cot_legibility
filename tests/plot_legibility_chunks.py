import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def plot_chunk_scores(filepath):
   with open(filepath) as f:
       data = json.load(f)
   
   models = ['deepseek', 'anthropic', 'openai', 'cutoff']
   fig, axes = plt.subplots(2, 2, figsize=(15, 10))
   axes = axes.ravel()
   
   for idx, model in enumerate(models):
       # Collect scores by chunk position
       chunk_scores = defaultdict(list)
       for file_data in data:
           chunks = file_data['sections'][f'{model}_reasoning']['chunk_grades'] if f'{model}_reasoning' in file_data['sections'] else []
           if not chunks:
               continue
           for i, chunk in enumerate(chunks):
               chunk_scores[i].append(chunk['score'])
       
       # Convert to list format for boxplot
       scores_list = [scores for scores in chunk_scores.values()]
       positions = range(len(scores_list))
       
       axes[idx].boxplot(scores_list, positions=positions)
       axes[idx].set_xlabel('Tokens')
       axes[idx].set_ylabel('Score')
       axes[idx].set_title(f'{model.capitalize()} Reasoning')
       axes[idx].set_xticks(positions)
       axes[idx].set_xticklabels([i * 5000 for i in range(len(positions))])
       axes[idx].grid(True)
   
   plt.tight_layout()
   plt.savefig(f'{filepath.split("/")[-1]}.png')

plot_chunk_scores('../scores/cutoff_0.25_openrouter_legibility_chunks_scores.json')