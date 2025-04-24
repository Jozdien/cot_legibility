import os
import json
import re

def extract_provider_info(file_path):
    """Extract provider information for each section from a rollout file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract provider information for different sections
    providers = {}
    
    # Initial DeepSeek response provider
    deepseek_match = re.search(r"# DeepSeek response \(via (.*?)\)", content)
    if deepseek_match:
        providers["deepseek"] = deepseek_match.group(1)
    
    # Cutoff provider
    cutoff_match = re.search(r"# cutoff_deepseek_completion \(via (.*?)\)", content)
    if cutoff_match:
        providers["cutoff"] = cutoff_match.group(1)
    
    # Anthropic paraphrase provider
    anthropic_match = re.search(r"# paraphrased_deepseek_completion_anthropic \(via (.*?)\)", content)
    if anthropic_match:
        providers["anthropic"] = anthropic_match.group(1)
    
    # OpenAI paraphrase provider
    openai_match = re.search(r"# paraphrased_deepseek_completion_openai \(via (.*?)\)", content)
    if openai_match:
        if openai_match.group(1) == "openrouter":
            print(f"Filename: {file_path}; OpenAI provider: {openai_match.group(1)}")
        providers["openai"] = openai_match.group(1)
    
    return providers

def analyze_deepseek_only_correctness(rollouts_dir, scores_file):
    """Analyze correctness scores for responses actually generated via DeepSeek API."""
    # Load scores file
    with open(scores_file, 'r', encoding='utf-8') as f:
        scores_data = json.load(f)
    
    # Initialize counters for DeepSeek-only responses
    deepseek_only_counts = {
        model: {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
        for model in ["deepseek", "cutoff", "anthropic", "openai"]
    }
    openrouter_only_counts = {
        model: {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
        for model in ["deepseek", "cutoff", "anthropic", "openai"]
    }
    
    total_files = len(scores_data)
    processed_files = 0
    
    for score_entry in scores_data:
        file_basename = score_entry.get("file")
        
        # Find the corresponding rollout file
        rollout_file = None
        for root, _, files in os.walk(rollouts_dir):
            for file in files:
                if file == file_basename:
                    rollout_file = os.path.join(root, file)
                    break
            if rollout_file:
                break
        
        if not rollout_file:
            print(f"Could not find rollout file for: {file_basename}")
            continue
        
        # Extract provider information
        providers = extract_provider_info(rollout_file)
        
        # For each model type, check if it was generated via DeepSeek
        for model in ["deepseek", "cutoff", "anthropic", "openai"]:
            # Check if this model's response was generated via DeepSeek API
            correctness = score_entry.get("correctness", {}).get(model, {}).get("correctness", "N/A")
            if providers.get(model) == "deepseek":
                deepseek_only_counts[model][correctness] += 1
            else:
                openrouter_only_counts[model][correctness] += 1
        
        processed_files += 1
        if processed_files % 10 == 0:
            print(f"Processed {processed_files}/{total_files} files")
    
    return deepseek_only_counts, openrouter_only_counts

def print_deepseek_only_summary(counts):
    """Print a summary of correctness scores for DeepSeek-only responses."""
    print("\n=== DeepSeek-only API Correctness Assessment ===")
    print("(Only counting responses actually generated via DeepSeek API, not OpenRouter)")
    
    for model, model_counts in counts.items():
        total = sum(count for cat, count in model_counts.items() if cat not in ["N/A", "error"])
        
        if total > 0:
            print(f"\n{model.capitalize()}:")
            print(f"  Correct: {model_counts['correct']} ({model_counts['correct']/total*100:.1f}%)")
            print(f"  Partially Correct: {model_counts['partially_correct']} ({model_counts['partially_correct']/total*100:.1f}%)")
            print(f"  Incorrect: {model_counts['incorrect']} ({model_counts['incorrect']/total*100:.1f}%)")
            print(f"  Total Valid: {total}")
            print(f"  N/A: {model_counts['N/A']}")
            print(f"  Error: {model_counts['error']}")
        else:
            print(f"\n{model.capitalize()}: No valid assessments via DeepSeek API")

if __name__ == "__main__":
    # Define paths relative to /tests
    rollouts_dir = "../r1_rollouts/cutoff_0.25_deepseek_openrouter"
    scores_file = "../scores/cutoff_0.25_deepseek_openrouter_scores.json"
    
    # Check if files exist
    if not os.path.exists(rollouts_dir):
        print(f"Error: Rollouts directory not found: {rollouts_dir}")
        exit(1)
        
    if not os.path.exists(scores_file):
        print(f"Error: Scores file not found: {scores_file}")
        exit(1)
        
    print(f"Analyzing DeepSeek-only correctness scores...")
    print(f"Rollouts directory: {rollouts_dir}")
    print(f"Scores file: {scores_file}")
    
    # Run the analysis
    deepseek_only_counts, openrouter_only_counts = analyze_deepseek_only_correctness(rollouts_dir, scores_file)
    
    # Print summary
    print_deepseek_only_summary(deepseek_only_counts)
    print_deepseek_only_summary(openrouter_only_counts)