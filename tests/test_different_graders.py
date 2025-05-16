import json
import numpy as np

# Load both JSON files
with open('../scores/cutoff_0.25_openrouter_gpt4o_scores.json', 'r') as f:
    gpt4o_scores = json.load(f)

with open('../scores/cutoff_0.25_openrouter_scores.json', 'r') as f:
    router_scores = json.load(f)

# Create dictionaries mapping questions to their scores
def extract_scores(data):
    scores = {}
    for item in data:
        if 'question' in item and 'legibility' in item:
            question = item['question']
            leg_scores = {}
            for key, value in item['legibility'].items():
                if isinstance(value, dict) and 'score' in value:
                    leg_scores[key] = value['score']
            scores[question] = leg_scores
    return scores

gpt4o_dict = extract_scores(gpt4o_scores)
router_dict = extract_scores(router_scores)

# Compare scores for matching questions
differences = []
for question in gpt4o_dict:
    if question in router_dict:
        for score_type in gpt4o_dict[question]:
            if score_type in router_dict[question]:
                if gpt4o_dict[question][score_type] == "N/A" or router_dict[question][score_type] == "N/A":
                    continue
                diff = abs(gpt4o_dict[question][score_type] - router_dict[question][score_type])
                differences.append(diff)

# Calculate and print average difference
if differences:
    avg_diff = np.mean(differences)
    std_diff = np.std(differences)
    print(f"Average difference in scores: {avg_diff:.2f}")
    print(f"Standard deviation of differences: {std_diff:.2f}")
    print(f"Total number of score comparisons: {len(differences)}")
else:
    print("No matching questions found between the files.")