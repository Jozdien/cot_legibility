#!/usr/bin/env python3
"""
Script to compute legibility statistics for MMLU Pro R1 reasoning traces,
with separate statistics for traces of length 10,000 or higher.
"""

import argparse
import json
import sys
import os
import re
import numpy as np

def get_reasoning_text_length(file_path, section_pattern):
    """
    Extract the length of a reasoning section from a markdown file.
    
    Args:
        file_path: Path to the markdown file
        section_pattern: Regex pattern to find the reasoning section
        
    Returns:
        int: Length of the reasoning text, or -1 if not found
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return -1
    
    match = re.search(section_pattern, content, re.DOTALL)
    if match:
        reasoning_text = match.group(1).strip()
        return len(reasoning_text)
    return -1

def compute_stats(scores):
    """Compute statistics for a list of scores."""
    if not scores:
        return None
    
    scores_array = np.array(scores)
    stats = {
        "avg_score": np.mean(scores_array),
        "std_dev": np.std(scores_array),
        "max_score": max(scores_array),
        "min_score": min(scores_array),
        "count": len(scores_array),
        "scores": scores
    }
    return stats

def get_mmlu_reasoning_stats(score_file):
    """
    Extract reasoning legibility statistics for MMLU Pro R1 file.
    
    Args:
        score_file: Path to the scores JSON file
        
    Returns:
        dict with stats for all traces and long traces
    """
    try:
        with open(score_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{score_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{score_file}' is not valid JSON.")
        sys.exit(1)
    
    # Determine the rollout directory based on the score file name
    if "mmlu_pro_R1" in score_file:
        rollout_dir = "r1_rollouts/mmlu_pro_R1_temp_1.0"
    else:
        print("Error: This script is designed for mmlu_pro_R1 files.")
        sys.exit(1)
    
    # Collect reasoning scores and lengths
    all_scores = []
    long_scores = []  # Scores for traces >= 10,000 chars
    na_count = 0
    length_data = []
    
    # Pattern to extract R1 reasoning section
    reasoning_pattern = r"# R1 reasoning.*?\n(.*?)(?=\n---|\n# |\Z)"
    
    for result in data:
        legibility = result.get("legibility", {})
        
        # Look for R1_reasoning key
        reasoning_section = None
        for section in legibility:
            if section == "R1_reasoning" or section.endswith("_reasoning"):
                reasoning_section = section
                break
        
        if not reasoning_section:
            continue
        
        score_data = legibility[reasoning_section]
        score = score_data.get("score")
        
        # Get the file path to check reasoning length
        filename = result.get("file", "")
        filepath = os.path.join(rollout_dir, filename)
        reasoning_length = get_reasoning_text_length(filepath, reasoning_pattern)
        
        # Process the score
        if score == "N/A":
            na_count += 1
        elif score == 0:
            continue
        elif score == 10:
            score = 9  # Cap at 9
        
        if isinstance(score, (int, float)) and score > 0:
            all_scores.append(score)
            length_data.append((score, reasoning_length))
            
            # Add to long scores if length >= 10,000
            if reasoning_length >= 10000:
                long_scores.append(score)
    
    # Compute statistics
    all_stats = compute_stats(all_scores)
    long_stats = compute_stats(long_scores)
    
    if all_stats:
        all_stats['na_count'] = na_count
        all_stats['total'] = len(all_scores) + na_count
    
    return {
        'all': all_stats,
        'long': long_stats,
        'length_data': length_data
    }

def print_stats(label, stats):
    """Print statistics in a formatted way."""
    if not stats:
        print(f"\n{label}: No valid scores found")
        return
    
    print(f"\n{label}:")
    print(f"{'='*45}")
    print(f"Average score: {stats['avg_score']:.4f}")
    print(f"Standard deviation: {stats['std_dev']:.4f}")
    print(f"Min score: {stats['min_score']:.4f}")
    print(f"Max score: {stats['max_score']:.4f}")
    print(f"Valid samples: {stats['count']}")
    if 'na_count' in stats:
        print(f"N/A samples: {stats['na_count']}")
        print(f"Total samples: {stats['total']}")
    
    # Score distribution
    print(f"\nScore Distribution:")
    print(f"{'-'*45}")
    scores_array = np.array(stats['scores'])
    for threshold in range(1, 10):
        count_above = np.sum(scores_array >= threshold)
        percentage = (count_above / len(scores_array)) * 100
        print(f"Score >= {threshold}: {count_above:3d} ({percentage:5.1f}%)")

def main():
    parser = argparse.ArgumentParser(
        description='Compute legibility statistics for MMLU Pro R1 reasoning traces'
    )
    parser.add_argument('--file', type=str, 
                        default='scores/mmlu_pro_R1_temp_1.0_scores.json',
                        help='Path to the MMLU Pro R1 scores JSON file')
    parser.add_argument('--length-analysis', action='store_true',
                        help='Show additional length-based analysis')
    
    args = parser.parse_args()
    
    print(f"Analyzing: {args.file}")
    
    results = get_mmlu_reasoning_stats(args.file)
    
    # Print statistics for all traces
    print_stats("All Reasoning Traces", results['all'])
    
    # Print statistics for long traces
    print_stats("Long Reasoning Traces (>= 10,000 chars)", results['long'])
    
    # Additional length analysis if requested
    if args.length_analysis and results['all']:
        print(f"\nLength Analysis:")
        print(f"{'='*45}")
        
        lengths = [length for _, length in results['length_data'] if length > 0]
        if lengths:
            print(f"Average reasoning length: {np.mean(lengths):.0f} chars")
            print(f"Median reasoning length: {np.median(lengths):.0f} chars")
            print(f"Traces >= 10,000 chars: {len(results['long']['scores']) if results['long'] else 0} "
                  f"({len(results['long']['scores']) / len(results['all']['scores']) * 100:.1f}%)" 
                  if results['long'] and results['all'] else "0 (0.0%)")

if __name__ == '__main__':
    main()