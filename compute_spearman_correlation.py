#!/usr/bin/env python3
"""
Compute Spearman's rank correlation for chunk legibility scores.
"""

import json
import numpy as np
from scipy import stats
import argparse
from collections import defaultdict
import pandas as pd


def load_scores(filepath):
    """Load scores from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def extract_chunk_scores(data):
    """Extract chunk scores for each section type across all files."""
    section_scores = defaultdict(list)
    file_section_mapping = defaultdict(lambda: defaultdict(list))
    
    for entry in data:
        file_name = entry['file']
        for section_name, section_data in entry['sections'].items():
            # Extract individual chunk scores
            chunk_scores = [chunk['score'] for chunk in section_data['chunk_grades']]
            section_scores[section_name].extend(chunk_scores)
            
            # Also store per-file average for file-level correlations
            file_section_mapping[file_name][section_name] = section_data['average_score']
    
    return section_scores, file_section_mapping


def compute_chunk_level_correlations(section_scores):
    """Compute Spearman correlations between all pairs of sections at chunk level."""
    sections = list(section_scores.keys())
    results = []
    
    print("\n=== Chunk-Level Spearman Correlations ===")
    print("(Using all individual chunk scores)")
    
    for i in range(len(sections)):
        for j in range(i+1, len(sections)):
            section1, section2 = sections[i], sections[j]
            scores1 = section_scores[section1]
            scores2 = section_scores[section2]
            
            # For chunk-level correlation, we need paired data
            # This is tricky since different sections may have different numbers of chunks
            # We'll skip this comparison if lengths don't match
            if len(scores1) == len(scores2):
                correlation, p_value = stats.spearmanr(scores1, scores2)
                results.append({
                    'section1': section1,
                    'section2': section2,
                    'correlation': correlation,
                    'p_value': p_value,
                    'n_chunks': len(scores1)
                })
                print(f"\n{section1} vs {section2}:")
                print(f"  Correlation: {correlation:.4f}")
                print(f"  P-value: {p_value:.4f}")
                print(f"  N chunks: {len(scores1)}")
            else:
                print(f"\nSkipping {section1} vs {section2} - different chunk counts ({len(scores1)} vs {len(scores2)})")
    
    return results


def compute_file_level_correlations(file_section_mapping):
    """Compute Spearman correlations between sections at file level (using average scores)."""
    # Convert to DataFrame for easier manipulation
    df_data = []
    for file_name, sections in file_section_mapping.items():
        row = {'file': file_name}
        row.update(sections)
        df_data.append(row)
    
    df = pd.DataFrame(df_data)
    
    # Get all section columns (excluding 'file')
    section_columns = [col for col in df.columns if col != 'file']
    
    print("\n\n=== File-Level Spearman Correlations ===")
    print("(Using average scores per file)")
    
    results = []
    for i in range(len(section_columns)):
        for j in range(i+1, len(section_columns)):
            section1, section2 = section_columns[i], section_columns[j]
            
            # Remove rows where either value is missing
            valid_mask = df[section1].notna() & df[section2].notna()
            valid_df = df[valid_mask]
            
            if len(valid_df) > 0:
                correlation, p_value = stats.spearmanr(valid_df[section1], valid_df[section2])
                results.append({
                    'section1': section1,
                    'section2': section2,
                    'correlation': correlation,
                    'p_value': p_value,
                    'n_files': len(valid_df)
                })
                print(f"\n{section1} vs {section2}:")
                print(f"  Correlation: {correlation:.4f}")
                print(f"  P-value: {p_value:.4f}")
                print(f"  N files: {len(valid_df)}")
    
    return results, df


def print_summary_statistics(section_scores, df):
    """Print summary statistics for each section."""
    print("\n\n=== Summary Statistics ===")
    
    # Chunk-level statistics
    print("\nChunk-level statistics:")
    for section, scores in section_scores.items():
        if scores:
            print(f"\n{section}:")
            print(f"  Total chunks: {len(scores)}")
            print(f"  Mean score: {np.mean(scores):.4f}")
            print(f"  Std dev: {np.std(scores):.4f}")
            print(f"  Min: {min(scores)}")
            print(f"  Max: {max(scores)}")
            print(f"  Score distribution: {dict(zip(*np.unique(scores, return_counts=True)))}")
    
    # File-level statistics
    print("\n\nFile-level statistics (average scores):")
    section_columns = [col for col in df.columns if col != 'file']
    for section in section_columns:
        valid_scores = df[section].dropna()
        if len(valid_scores) > 0:
            print(f"\n{section}:")
            print(f"  Files with scores: {len(valid_scores)}")
            print(f"  Mean average score: {valid_scores.mean():.4f}")
            print(f"  Std dev: {valid_scores.std():.4f}")
            print(f"  Min: {valid_scores.min():.4f}")
            print(f"  Max: {valid_scores.max():.4f}")


def main():
    parser = argparse.ArgumentParser(description='Compute Spearman rank correlation for chunk legibility scores')
    parser.add_argument('score_file', help='Path to the JSON score file')
    parser.add_argument('--output', '-o', help='Optional output file for results')
    args = parser.parse_args()
    
    # Load data
    data = load_scores(args.score_file)
    
    # Extract scores
    section_scores, file_section_mapping = extract_chunk_scores(data)
    
    # Compute correlations
    chunk_results = compute_chunk_level_correlations(section_scores)
    file_results, df = compute_file_level_correlations(file_section_mapping)
    
    # Print summary statistics
    print_summary_statistics(section_scores, df)
    
    # Save results if output file specified
    if args.output:
        output_data = {
            'chunk_level_correlations': chunk_results,
            'file_level_correlations': file_results,
            'summary': {
                'total_files': len(data),
                'sections': list(section_scores.keys()),
                'chunk_counts': {section: len(scores) for section, scores in section_scores.items()}
            }
        }
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"\n\nResults saved to: {args.output}")


if __name__ == '__main__':
    main()