#!/usr/bin/env python3
"""
Compute within-file temporal Spearman correlations for chunk legibility scores
to measure if reasoning quality degrades over time within individual reasoning sections.
"""

import json
import numpy as np
from scipy import stats
import argparse
import matplotlib.pyplot as plt
from collections import defaultdict


def load_scores(filepath):
    """Load scores from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def compute_within_file_correlations(data, section_name='deepseek_reasoning'):
    """Compute temporal correlation within each file's reasoning section."""
    correlations = []
    p_values = []
    chunk_counts = []
    
    for entry in data:
        file_name = entry['file']
        if section_name in entry['sections']:
            section_data = entry['sections'][section_name]
            chunk_scores = [chunk['score'] for chunk in section_data['chunk_grades']]
            
            # Need at least 3 chunks for meaningful correlation
            if len(chunk_scores) >= 3:
                positions = list(range(1, len(chunk_scores) + 1))
                corr, p_val = stats.spearmanr(positions, chunk_scores)
                
                # Only include if correlation is defined (not NaN)
                if not np.isnan(corr):
                    correlations.append(corr)
                    p_values.append(p_val)
                    chunk_counts.append(len(chunk_scores))
    
    return correlations, p_values, chunk_counts


def analyze_correlation_distribution(correlations, p_values, chunk_counts, section_name):
    """Analyze and display the distribution of within-file correlations."""
    if not correlations:
        print(f"No valid correlations found for {section_name}")
        return None
    
    correlations = np.array(correlations)
    p_values = np.array(p_values)
    chunk_counts = np.array(chunk_counts)
    
    # Basic statistics
    mean_corr = np.mean(correlations)
    median_corr = np.median(correlations)
    std_corr = np.std(correlations)
    
    # Test if mean correlation is significantly different from 0
    t_stat, t_pval = stats.ttest_1samp(correlations, 0)
    
    # Count positive/negative trends
    positive_count = np.sum(correlations > 0)
    negative_count = np.sum(correlations < 0)
    significant_positive = np.sum((correlations > 0) & (p_values < 0.05))
    significant_negative = np.sum((correlations < 0) & (p_values < 0.05))
    
    # Weighted statistics (by number of chunks)
    weights = chunk_counts / np.sum(chunk_counts)
    weighted_mean = np.sum(correlations * weights)
    
    print(f"\n=== Within-File Temporal Analysis for {section_name} ===")
    print(f"Number of files analyzed: {len(correlations)}")
    print(f"Average chunks per file: {np.mean(chunk_counts):.1f} (range: {np.min(chunk_counts)}-{np.max(chunk_counts)})")
    
    print(f"\nCorrelation Statistics:")
    print(f"  Mean correlation: {mean_corr:.4f}")
    print(f"  Median correlation: {median_corr:.4f}")
    print(f"  Std deviation: {std_corr:.4f}")
    print(f"  Weighted mean (by chunk count): {weighted_mean:.4f}")
    
    print(f"\nSignificance Testing:")
    print(f"  One-sample t-test (H0: mean = 0):")
    print(f"    t-statistic: {t_stat:.4f}")
    print(f"    p-value: {t_pval:.6f}")
    if t_pval < 0.05:
        direction = "positive" if mean_corr > 0 else "negative"
        print(f"    Result: Significant {direction} trend (legibility {'increases' if mean_corr > 0 else 'decreases'} over time)")
    else:
        print(f"    Result: No significant overall temporal trend")
    
    print(f"\nTrend Distribution:")
    print(f"  Files with positive correlation: {positive_count}/{len(correlations)} ({100*positive_count/len(correlations):.1f}%)")
    print(f"  Files with negative correlation: {negative_count}/{len(correlations)} ({100*negative_count/len(correlations):.1f}%)")
    print(f"  Files with significant positive (p<0.05): {significant_positive}/{len(correlations)} ({100*significant_positive/len(correlations):.1f}%)")
    print(f"  Files with significant negative (p<0.05): {significant_negative}/{len(correlations)} ({100*significant_negative/len(correlations):.1f}%)")
    
    # Effect size interpretation
    print(f"\nEffect Size Interpretation:")
    abs_mean = abs(mean_corr)
    if abs_mean < 0.1:
        effect = "negligible"
    elif abs_mean < 0.3:
        effect = "small"
    elif abs_mean < 0.5:
        effect = "moderate"
    else:
        effect = "large"
    print(f"  Mean correlation magnitude suggests {effect} effect size")
    
    return {
        'mean_correlation': mean_corr,
        'median_correlation': median_corr,
        'std_correlation': std_corr,
        'weighted_mean_correlation': weighted_mean,
        't_statistic': t_stat,
        't_pvalue': t_pval,
        'n_files': len(correlations),
        'positive_count': int(positive_count),
        'negative_count': int(negative_count),
        'significant_positive': int(significant_positive),
        'significant_negative': int(significant_negative)
    }


def plot_correlation_distribution(correlations, section_name, output_file=None):
    """Plot the distribution of within-file correlations."""
    if not correlations:
        return
    
    plt.figure(figsize=(10, 6))
    
    # Histogram
    plt.hist(correlations, bins=30, alpha=0.7, edgecolor='black')
    
    # Add vertical lines for mean and median
    mean_corr = np.mean(correlations)
    median_corr = np.median(correlations)
    plt.axvline(mean_corr, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_corr:.3f}')
    plt.axvline(median_corr, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_corr:.3f}')
    plt.axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)
    
    plt.xlabel('Within-File Spearman Correlation')
    plt.ylabel('Number of Files')
    plt.title(f'Distribution of Within-File Temporal Correlations\n{section_name}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"\nPlot saved to: {output_file}")
    else:
        plt.show()
    
    plt.close()


def analyze_all_sections(data):
    """Analyze within-file temporal trends for all sections."""
    # Get all unique section names
    all_sections = set()
    for entry in data:
        all_sections.update(entry['sections'].keys())
    
    results = {}
    
    for section in sorted(all_sections):
        correlations, p_values, chunk_counts = compute_within_file_correlations(data, section)
        if correlations:
            result = analyze_correlation_distribution(correlations, p_values, chunk_counts, section)
            if result:
                results[section] = result
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Compute within-file temporal Spearman correlations for chunk legibility scores'
    )
    parser.add_argument('score_file', help='Path to the JSON score file')
    parser.add_argument('--section', default='deepseek_reasoning', 
                       help='Section to analyze (default: deepseek_reasoning)')
    parser.add_argument('--plot', action='store_true', 
                       help='Generate a plot of the correlation distribution')
    parser.add_argument('--plot-output', help='Save plot to file instead of displaying')
    parser.add_argument('--all-sections', action='store_true',
                       help='Analyze all sections, not just the specified one')
    parser.add_argument('--output', '-o', help='Save results to JSON file')
    
    args = parser.parse_args()
    
    # Load data
    data = load_scores(args.score_file)
    
    if args.all_sections:
        # Analyze all sections
        results = analyze_all_sections(data)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nResults saved to: {args.output}")
    else:
        # Analyze specific section
        correlations, p_values, chunk_counts = compute_within_file_correlations(data, args.section)
        
        if not correlations:
            print(f"No valid correlations found for section: {args.section}")
            return
        
        result = analyze_correlation_distribution(correlations, p_values, chunk_counts, args.section)
        
        if args.plot:
            plot_correlation_distribution(correlations, args.section, args.plot_output)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"\nResults saved to: {args.output}")


if __name__ == '__main__':
    main()