#!/usr/bin/env python3
"""
Compute Spearman's rank correlation between chunk position (time) and legibility scores
to measure temporal trends in reasoning quality.
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


def extract_temporal_scores(data, section_name='deepseek_reasoning'):
    """Extract scores in temporal order for a specific section."""
    all_scores = []
    file_scores = {}
    
    for entry in data:
        file_name = entry['file']
        if section_name in entry['sections']:
            section_data = entry['sections'][section_name]
            chunk_scores = [chunk['score'] for chunk in section_data['chunk_grades']]
            if chunk_scores:
                all_scores.extend(chunk_scores)
                file_scores[file_name] = chunk_scores
    
    return all_scores, file_scores


def compute_temporal_correlation(scores):
    """Compute Spearman correlation between chunk position and score."""
    if not scores:
        return None, None
    
    positions = list(range(1, len(scores) + 1))
    correlation, p_value = stats.spearmanr(positions, scores)
    
    return correlation, p_value


def analyze_all_sections(data):
    """Analyze temporal trends for all sections."""
    results = {}
    
    # Get all unique section names
    all_sections = set()
    for entry in data:
        all_sections.update(entry['sections'].keys())
    
    print("=== Temporal Spearman Correlations ===")
    print("(Correlation between chunk position and legibility score)\n")
    
    for section in sorted(all_sections):
        all_scores, file_scores = extract_temporal_scores(data, section)
        
        if all_scores:
            # Overall correlation across all files
            overall_corr, overall_p = compute_temporal_correlation(all_scores)
            
            # Per-file correlations
            file_correlations = []
            for file_name, scores in file_scores.items():
                if len(scores) > 2:  # Need at least 3 points for meaningful correlation
                    corr, p_val = compute_temporal_correlation(scores)
                    file_correlations.append((corr, p_val))
            
            # Calculate statistics on per-file correlations
            if file_correlations:
                file_corrs = [c[0] for c in file_correlations]
                mean_file_corr = np.mean(file_corrs)
                std_file_corr = np.std(file_corrs)
                positive_trend_files = sum(1 for c in file_corrs if c > 0)
                significant_positive = sum(1 for c, p in file_correlations if c > 0 and p < 0.05)
            else:
                mean_file_corr = std_file_corr = positive_trend_files = significant_positive = 0
            
            results[section] = {
                'overall_correlation': overall_corr,
                'overall_p_value': overall_p,
                'total_chunks': len(all_scores),
                'total_files': len(file_scores),
                'mean_file_correlation': mean_file_corr,
                'std_file_correlation': std_file_corr,
                'files_with_positive_trend': positive_trend_files,
                'files_with_significant_positive': significant_positive
            }
            
            print(f"{section}:")
            print(f"  Overall correlation: {overall_corr:.4f} (p={overall_p:.4f})")
            print(f"  Total chunks: {len(all_scores)}")
            print(f"  Total files: {len(file_scores)}")
            print(f"  Mean per-file correlation: {mean_file_corr:.4f} ± {std_file_corr:.4f}")
            print(f"  Files with positive trend: {positive_trend_files}/{len(file_scores)}")
            print(f"  Files with significant positive trend (p<0.05): {significant_positive}/{len(file_scores)}")
            print()
    
    return results


def plot_temporal_trend(scores, section_name, output_file=None):
    """Plot the temporal trend of scores."""
    if not scores:
        return
    
    positions = list(range(1, len(scores) + 1))
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Scatter plot
    plt.scatter(positions, scores, alpha=0.5, s=20)
    
    # Add trend line
    z = np.polyfit(positions, scores, 1)
    p = np.poly1d(z)
    plt.plot(positions, p(positions), "r--", alpha=0.8, label=f'Linear trend (slope={z[0]:.4f})')
    
    # Add rolling average
    window = min(50, len(scores) // 10)
    if window > 2:
        rolling_avg = np.convolve(scores, np.ones(window)/window, mode='valid')
        rolling_positions = positions[window//2:-(window//2-1) if window//2-1 > 0 else None]
        plt.plot(rolling_positions, rolling_avg, 'g-', alpha=0.8, linewidth=2, 
                label=f'Rolling average (window={window})')
    
    correlation, p_value = stats.spearmanr(positions, scores)
    
    plt.xlabel('Chunk Position (Time)')
    plt.ylabel('Legibility Score')
    plt.title(f'Temporal Trend of Legibility Scores - {section_name}\n' + 
              f'Spearman ρ = {correlation:.4f} (p = {p_value:.4f})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {output_file}")
    else:
        plt.show()
    
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description='Compute temporal Spearman correlation for chunk legibility scores'
    )
    parser.add_argument('score_file', help='Path to the JSON score file')
    parser.add_argument('--section', default='deepseek_reasoning', 
                       help='Section to analyze (default: deepseek_reasoning)')
    parser.add_argument('--plot', action='store_true', 
                       help='Generate a plot of the temporal trend')
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
        all_scores, file_scores = extract_temporal_scores(data, args.section)
        
        if not all_scores:
            print(f"No scores found for section: {args.section}")
            return
        
        # Compute overall correlation
        correlation, p_value = compute_temporal_correlation(all_scores)
        
        print(f"=== Temporal Analysis for {args.section} ===")
        print(f"Total chunks analyzed: {len(all_scores)}")
        print(f"Number of files: {len(file_scores)}")
        print(f"\nSpearman correlation coefficient: {correlation:.4f}")
        print(f"P-value: {p_value:.4f}")
        
        if p_value < 0.05:
            if correlation > 0:
                print("\nResult: Significant positive correlation - legibility increases over time")
            else:
                print("\nResult: Significant negative correlation - legibility decreases over time")
        else:
            print("\nResult: No significant temporal trend detected")
        
        # Analyze per-file trends
        print("\n=== Per-file Analysis ===")
        positive_trends = 0
        significant_positive = 0
        
        for file_name, scores in file_scores.items():
            if len(scores) > 2:  # Need at least 3 points
                corr, p_val = compute_temporal_correlation(scores)
                if corr > 0:
                    positive_trends += 1
                    if p_val < 0.05:
                        significant_positive += 1
        
        print(f"Files with positive trend: {positive_trends}/{len(file_scores)}")
        print(f"Files with significant positive trend (p<0.05): {significant_positive}/{len(file_scores)}")
        
        if args.plot:
            plot_temporal_trend(all_scores, args.section, args.plot_output)
        
        if args.output:
            results = {
                'section': args.section,
                'overall_correlation': correlation,
                'overall_p_value': p_value,
                'total_chunks': len(all_scores),
                'total_files': len(file_scores),
                'files_with_positive_trend': positive_trends,
                'files_with_significant_positive': significant_positive
            }
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nResults saved to: {args.output}")


if __name__ == '__main__':
    main()