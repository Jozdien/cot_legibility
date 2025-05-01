import os
import glob
import argparse

from utils import analysis_utils

def process_regular_file(file_path, plots_dir=None, std_display=None, include_settings=None):
    """Process a single regular score file."""
    print(f"Analyzing: {file_path}")
    file_name = os.path.basename(file_path).replace('_scores.json', '')
    data = analysis_utils.load_json_file(file_path)
    stats = analysis_utils.analyze_scores(data, include_settings)
    
    analysis_utils.print_summary(stats, file_name)
    
    if plots_dir:
        analysis_utils.plot_legibility_scores(stats, file_name, plots_dir, std_display=std_display)
        analysis_utils.plot_correctness_assessment(stats, file_name, plots_dir)
        analysis_utils.plot_legibility_by_correctness(data, file_name, plots_dir)
        analysis_utils.plot_length_vs_legibility(data, file_name, plots_dir)
        analysis_utils.plot_correctness_with_baseline(stats, file_name, plots_dir)
        analysis_utils.plot_legibility_by_baseline_correctness(data, file_name, plots_dir)
    
    return file_name, stats

def process_claude_file(file_path, plots_dir=None, claude_baseline=None):
    """Process a single Claude answers score file."""
    print(f"Analyzing Claude answers file: {file_path}")
    file_name = os.path.basename(file_path).replace('.json', '')
    stats = analysis_utils.extract_claude_scores(file_path)
    
    analysis_utils.print_claude_summary(stats, file_name)
    
    if plots_dir:
        analysis_utils.plot_claude_correctness(stats, file_name, plots_dir, claude_baseline)
        analysis_utils.plot_claude_comparisons(stats, file_name, plots_dir)

def process_regular_files(file_pattern, compare=False, plots=False, std_display=None, include_settings=None):
    """Process all regular score files matching the pattern."""
    files = glob.glob(file_pattern)
    print(f"Found {len(files)} score files to analyze")
    
    all_stats = {}
    plots_dir = analysis_utils.create_plots_directory() if plots else None
    
    for file_path in files:
        file_name, stats = process_regular_file(file_path, plots_dir, std_display, include_settings)
        if file_name and stats:
            all_stats[file_name] = stats
    
    if compare and len(all_stats) > 1:
        analysis_utils.compare_files(all_stats)
        
        if plots:
            for section in ["deepseek_response", "deepseek_reasoning", "cutoff_response", "cutoff_reasoning", 
                           "anthropic_response", "anthropic_reasoning", "openai_response", "openai_reasoning"]:
                analysis_utils.plot_comparison_legibility(all_stats, section, plots_dir)
            for model in ["deepseek", "cutoff", "anthropic", "openai"]:
                analysis_utils.plot_comparison_correctness(all_stats, model, plots_dir)
            analysis_utils.plot_overall_model_performance(all_stats, plots_dir)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Analyze legibility and correctness scores from JSON files')
    parser.add_argument('--dir', type=str, default='scores',
                        help='Directory containing score JSON files')
    parser.add_argument('--pattern', type=str, default='*_scores.json',
                        help='File pattern to match')
    parser.add_argument('--compare', action='store_true',
                        help='Compare stats across different files')
    parser.add_argument('--plots', action='store_true',
                        help='Generate plots of the results')
    parser.add_argument('--claude-file', type=str, default=None,
                        help='Process a specific Claude answers score file from claude_answers/scores directory')
    parser.add_argument('--claude-baseline', type=str, default='claude_answers/scores/claude_baseline_scores.json',
                        help='Include baseline Claude 3.5 scores in the comparisons')
    parser.add_argument('--analysis-type', type=str, choices=['regular', 'claude'], default=None,
                        help='Type of analysis to run (regular or claude)')
    parser.add_argument('--exclude-default', action='store_true', default=False,
                        help='Exclude Default (DeepSeek) setting in plots')
    parser.add_argument('--exclude-cutoff', action='store_true', default=False,
                        help='Exclude With Cutoff setting in plots')
    parser.add_argument('--exclude-claude', action='store_true', default=False,
                        help='Exclude With Claude Paraphrase setting in plots')
    parser.add_argument('--exclude-gpt', action='store_true', default=False,
                        help='Exclude With GPT-4o Paraphrase setting in plots')
    return parser.parse_args()

def main():
    """Main function to run the analysis."""
    args = parse_arguments()
    analysis_utils.setup_matplotlib()

    include_settings = {
        "default": not args.exclude_default,
        "cutoff": not args.exclude_cutoff,
        "claude": not args.exclude_claude,
        "gpt": not args.exclude_gpt
    }
    print(f"Include settings: {include_settings}")
    
    analysis_type = args.analysis_type
    if analysis_type is None:
        analysis_type = 'claude' if args.claude_file else 'regular'
    
    if analysis_type == 'claude':
        claude_baseline = None
        if args.claude_baseline and os.path.exists(args.claude_baseline):
            claude_baseline = analysis_utils.extract_claude_scores(args.claude_baseline)
            print(f"Loaded Claude scores from {args.claude_baseline}")
        if args.claude_file:
            if os.path.exists(args.claude_file):
                plots_dir = analysis_utils.create_plots_directory() if args.plots else None
                process_claude_file(args.claude_file, plots_dir, claude_baseline)
            else:
                print(f"Claude answers file not found: {args.claude_file}")
        else:
            print("Error: When using --analysis-type=claude, you must provide a --claude-file")
    else:  # 'regular'
        file_pattern = os.path.join(args.dir, args.pattern)
        process_regular_files(file_pattern, args.compare, args.plots, include_settings=include_settings)

if __name__ == "__main__":
    main()