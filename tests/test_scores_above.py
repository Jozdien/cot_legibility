import json

def calculate_high_deepseek_reasoning_percentage(data, threshold_score):
    # Counter for scores > threshold_score
    high_scores = 0
    # Counter for total scores
    total_scores = 0
    
    # Iterate through each item in the data
    for item in data:
        # Check if legibility exists and contains deepseek_reasoning
        if 'legibility' in item and 'deepseek_reasoning' in item['legibility']:
            total_scores += 1
            if item['legibility']['deepseek_reasoning']['score'] >= threshold_score:
                high_scores += 1
    
    # Calculate percentage
    if total_scores == 0:
        return 0
    
    percentage = (high_scores / total_scores) * 100
    return percentage

# Example usage:
with open('../scores/cutoff_0.25_openrouter_scores.json', 'r') as f:
    data = json.load(f)
    threshold_score = 5
    percentage = calculate_high_deepseek_reasoning_percentage(data, threshold_score)
    print(f"Percentage of deepseek_reasoning scores >= {threshold_score}: {percentage:.2f}%")