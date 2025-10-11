#!/usr/bin/env python3
"""
Script to compute average and standard deviation of legibility scores for reasoning sections
from a given score file.
"""

import argparse
import json
import sys
import numpy as np

def get_reasoning_stats(score_file):
    """
    Extract average and standard deviation for reasoning legibility scores.
    Finds the first key ending with '_reasoning' in the results.
    
    Args:
        score_file: Path to the scores JSON file
        
    Returns:
        tuple of (section_name, stats_dict) where stats_dict has avg_score, std_dev, count
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
    
    # Collect all reasoning scores
    reasoning_scores = {}
    na_counts = {}
    
    for result in data:
        legibility = result.get("legibility", {})
        for section, score_data in legibility.items():
            if section.endswith('_reasoning'):
                if section not in reasoning_scores:
                    reasoning_scores[section] = []
                    na_counts[section] = 0
                
                score = score_data.get("score")
                if score == "N/A":
                    na_counts[section] += 1
                elif score == 0:
                    continue
                elif score == 10:
                    # Cap at 9 as per original logic
                    reasoning_scores[section].append(9)
                elif isinstance(score, (int, float)):
                    reasoning_scores[section].append(score)
    
    # Find the first reasoning section with scores
    reasoning_section = None
    reasoning_stats = None
    
    for section, scores in reasoning_scores.items():
        if scores:  # If we have any scores
            reasoning_section = section
            reasoning_stats = {
                "avg_score": np.mean(scores),
                "std_dev": np.std(scores),
                "max_score": max(scores),
                "count": len(scores),
                "na_count": na_counts[section],
                "total": len(scores) + na_counts[section],
                "scores": scores  # Include raw scores for distribution
            }
            break
    
    if not reasoning_section:
        # Check if we found any reasoning sections at all
        if reasoning_scores:
            # We found sections but no valid scores
            section = list(reasoning_scores.keys())[0]
            print(f"No valid scores found for {section}.")
            return section, None
        else:
            print("No reasoning section found in the file.")
            return None, None
    
    return reasoning_section, reasoning_stats

def main():
    parser = argparse.ArgumentParser(
        description='Compute average and standard deviation of reasoning legibility scores'
    )
    parser.add_argument('score_file', help='Path to the scores JSON file')
    parser.add_argument('--raw', action='store_true', 
                        help='Output raw values only (avg std count) for scripting')
    
    args = parser.parse_args()
    
    section_name, stats = get_reasoning_stats(args.score_file)
    
    if stats is None:
        sys.exit(1)
    
    if args.raw:
        # Output in simple format for easy parsing
        print(f"{stats['avg_score']:.4f} {stats['std_dev']:.4f} {stats['count']}")
    else:
        # Pretty formatted output
        model_name = section_name.replace('_reasoning', '').title()
        print(f"\n{model_name} Reasoning Legibility Statistics:")
        print(f"{'='*45}")
        print(f"Section: {section_name}")
        print(f"Average score: {stats['avg_score']:.4f}")
        print(f"Standard deviation: {stats['std_dev']:.4f}")
        print(f"Max score: {stats['max_score']:.4f}")
        print(f"Valid samples: {stats['count']}")
        print(f"N/A samples: {stats['na_count']}")
        print(f"Total samples: {stats['total']}")
        
        # Add score distribution
        if 'scores' in stats and stats['scores']:
            print(f"\nScore Distribution:")
            print(f"{'-'*45}")
            scores_array = np.array(stats['scores'])
            for threshold in range(1, 10):
                count_above = np.sum(scores_array >= threshold)
                percentage = (count_above / len(scores_array)) * 100
                print(f"Score >= {threshold}: {count_above:3d} ({percentage:5.1f}%)")

if __name__ == '__main__':
    main()