import json
import os
import re

# Configuration
scores_file = "../scores/cutoff_0.25_deepseek_openrouter_scores.json"
original_dir = "../r1_rollouts/cutoff_0.25_deepseek_openrouter"
illegibility_threshold = 6  # Scores >= this threshold will be analyzed

# Load scores data
with open(scores_file, 'r', encoding='utf-8') as f:
    results = json.load(f)

print(f"Loaded {len(results)} results from {scores_file}")

# Track our findings
high_score_files = []
provider_counts = {"openrouter": 0, "deepseek": 0, "unknown": 0}
section_counts = {}

# Find files with high illegibility scores
for result in results:
    filename = result.get("file")
    has_high_score = False
    high_score_sections = []
    
    # Check each section for high illegibility scores
    for section, score_data in result.get("legibility", {}).items():
        score = score_data.get("score")
        if score != "N/A" and isinstance(score, (int, float)) and score >= illegibility_threshold:
            has_high_score = True
            high_score_sections.append(section)
            
            # Track counts by section
            if section not in section_counts:
                section_counts[section] = {"total": 0, "openrouter": 0, "deepseek": 0, "unknown": 0}
            section_counts[section]["total"] += 1
    
    if has_high_score:
        filepath = os.path.join(original_dir, filename)
        high_score_files.append({
            "filename": filename, 
            "filepath": filepath,
            "sections": high_score_sections
        })

print(f"Found {len(high_score_files)} files with illegibility scores >= {illegibility_threshold}")

# Check original files for provider information
for file_info in high_score_files:
    filepath = file_info["filepath"]
    
    if not os.path.exists(filepath):
        print(f"WARNING: File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check each high-scoring section
    for section_name in file_info["sections"]:
        # Map section name to the heading pattern in the markdown file
        if section_name == "deepseek_response":
            pattern = r"# DeepSeek response \((?:via|with) (.*?)\)"
        elif section_name == "deepseek_reasoning":
            pattern = r"# DeepSeek reasoning \((?:via|with) (.*?)\)"
        elif section_name == "cutoff_response" or section_name == "cutoff_reasoning":
            pattern = r"# cutoff_deepseek_completion(?: \((?:via|with) (.*?)\))?"
        elif section_name == "anthropic_response" or section_name == "anthropic_reasoning":
            pattern = r"# paraphrased_deepseek_completion_anthropic(?: \((?:via|with) (.*?)\))?"
        elif section_name == "openai_response" or section_name == "openai_reasoning":
            pattern = r"# paraphrased_deepseek_completion_openai(?: \((?:via|with) (.*?)\))?"
        else:
            continue
        
        # Look for the pattern in the content
        match = re.search(pattern, content)
        if match and match.groups():
            print(filepath)
            provider = match.group(1).lower()
            if "openrouter" in provider:
                print(f"OpenRouter provider found for {section_name} in {filepath}")
                provider_counts["openrouter"] += 1
                section_counts[section_name]["openrouter"] += 1
            elif "deepseek" in provider:
                print(f"DeepSeek provider found for {section_name} in {filepath}")
                provider_counts["deepseek"] += 1
                section_counts[section_name]["deepseek"] += 1
            else:
                provider_counts["unknown"] += 1
                section_counts[section_name]["unknown"] += 1
        else:
            print(f"No provider found for {section_name} in {filepath}")
            provider_counts["unknown"] += 1
            section_counts[section_name]["unknown"] += 1

# Print results
print("\n=== Provider Statistics for High Illegibility Scores ===")
print(f"OpenRouter: {provider_counts['openrouter']}")
print(f"DeepSeek API: {provider_counts['deepseek']}")
print(f"Unknown/Not specified: {provider_counts['unknown']}")

print("\n=== Breakdown by Section ===")
for section, counts in section_counts.items():
    print(f"\n{section}:")
    print(f"  Total sections with high illegibility: {counts['total']}")
    print(f"  OpenRouter: {counts['openrouter']} ({counts['openrouter']/counts['total']*100:.1f}%)")
    print(f"  DeepSeek API: {counts['deepseek']} ({counts['deepseek']/counts['total']*100:.1f}%)")
    print(f"  Unknown/Not specified: {counts['unknown']} ({counts['unknown']/counts['total']*100:.1f}%)")