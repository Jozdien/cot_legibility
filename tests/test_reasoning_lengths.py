import json
import os
import re
import matplotlib.pyplot as plt

# Load scores data
with open("../scores/cutoff_0.25_openrouter_scores.json", 'r', encoding='utf-8') as f:
    results = json.load(f)

# Dictionary to store section lengths and scores
data = {
    'deepseek_response': {'lengths': [], 'scores': []},
    'deepseek_reasoning': {'lengths': [], 'scores': []},
    'cutoff_response': {'lengths': [], 'scores': []},
    'cutoff_reasoning': {'lengths': [], 'scores': []},
    'anthropic_response': {'lengths': [], 'scores': []},
    'anthropic_reasoning': {'lengths': [], 'scores': []},
    'openai_response': {'lengths': [], 'scores': []},
    'openai_reasoning': {'lengths': [], 'scores': []}
}

# Process each result
for result in results:
    filename = result.get("file")
    filepath = os.path.join("../r1_rollouts/cutoff_0.25_openrouter", filename)
    
    if not os.path.exists(filepath):
        continue
        
    # Read the file content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract sections using patterns
    patterns = {
        'deepseek_response': r"# DeepSeek response.*?\n(.*?)(?=\n---|\n# |\Z)",
        'deepseek_reasoning': r"# DeepSeek reasoning.*?\n(.*?)(?=\n---|\n# |\Z)",
        'cutoff_response': r"# cutoff_deepseek_completion response.*?\n(.*?)(?=\n---|\n# |\Z)",
        'cutoff_reasoning': r"# cutoff_deepseek_completion reasoning.*?\n(.*?)(?=\n---|\n# |\Z)",
        'anthropic_response': r"# paraphrased_deepseek_completion_anthropic response.*?\n(.*?)(?=\n---|\n# |\Z)",
        'anthropic_reasoning': r"# paraphrased_deepseek_completion_anthropic reasoning.*?\n(.*?)(?=\n---|\n# |\Z)",
        'openai_response': r"# paraphrased_deepseek_completion_openai response.*?\n(.*?)(?=\n---|\n# |\Z)",
        'openai_reasoning': r"# paraphrased_deepseek_completion_openai reasoning.*?\n(.*?)(?=\n---|\n# |\Z)"
    }
    
    # Get legibility scores
    legibility = result.get("legibility", {})
    
    # Process each section
    for section, pattern in patterns.items():
        match = re.search(pattern, content, re.DOTALL)
        if match and section in legibility:
            section_text = match.group(1).strip()
            section_length = len(section_text)
            section_score = legibility[section].get("score")
            
            if isinstance(section_score, (int, float)):
                data[section]['lengths'].append(section_length)
                data[section]['scores'].append(section_score)

# Create scatter plots
plt.figure(figsize=(15, 10))

for i, (section, values) in enumerate(data.items(), 1):
    plt.subplot(2, 4, i)
    plt.scatter(values['lengths'], values['scores'], alpha=0.5)
    plt.title(section.replace('_', ' '))
    plt.xlabel('Section Length')
    plt.ylabel('Legibility Score')
    
plt.tight_layout()
plt.show()

# Print some basic statistics
for section, values in data.items():
    if values['lengths'] and values['scores']:
        print(f"\n{section}:")
        print(f"Average length: {sum(values['lengths']) / len(values['lengths']):.0f}")
        print(f"Average score: {sum(values['scores']) / len(values['scores']):.2f}")
        print(f"Number of samples: {len(values['lengths'])}")