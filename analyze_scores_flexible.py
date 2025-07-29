import os
import glob
import argparse
import json
from collections import defaultdict
import numpy as np

from utils import analysis_utils
import matplotlib.pyplot as plt

def extract_model_names_from_data(data):
    """Extract all unique model names from the data."""
    model_names = set()
    for item in data:
        # From legibility sections
        for section in item.get("legibility", {}):
            model = section.split("_")[0]
            model_names.add(model)
        # From correctness sections
        for model in item.get("correctness", {}):
            model_names.add(model)
    return list(model_names)

def analyze_legibility_scores_flexible(data):
    """Extract and analyze legibility scores with flexible section names."""
    section_scores = defaultdict(list)
    section_na_counts = defaultdict(int)
    
    for result in data:
        for section, score_data in result.get("legibility", {}).items():
            if score_data.get("score") == "N/A":
                section_na_counts[section] += 1
            elif score_data.get("score") == 0:
                continue
            elif score_data.get("score") == 10:
                score_data["score"] = 9
            elif isinstance(score_data.get("score"), (int, float)):
                section_scores[section].append(score_data["score"])
    
    legibility_stats = {}
    for section, scores in section_scores.items():
        na_count = section_na_counts[section]
        total = len(scores) + na_count
        if scores:
            legibility_stats[section] = {
                "avg_score": sum(scores) / len(scores),
                "std_dev": np.std(scores),
                "max_score": max(scores),
                "count": len(scores),
                "na_count": na_count,
                "total": total,
            }
        else:
            legibility_stats[section] = {
                "avg_score": None,
                "std_dev": None,
                "max_score": None,
                "count": 0,
                "na_count": na_count,
                "total": total,
            }
    
    return {"legibility_stats": legibility_stats, "raw_scores": section_scores}

def analyze_scores_flexible(data):
    """Analyze scores with flexible model detection."""
    # Extract model names from the data
    models = extract_model_names_from_data(data)
    
    # Analyze legibility scores with flexible section names
    legibility_results = analyze_legibility_scores_flexible(data)
    
    # Analyze correctness scores for all found models
    correctness_results = analysis_utils.analyze_correctness_scores(data, models=models)
    
    # Don't filter - include all models found
    return {
        "legibility": legibility_results["legibility_stats"],
        "correctness": correctness_results,
        "raw_legibility_scores": legibility_results["raw_scores"],
    }

def plot_legibility_by_correctness_flexible(data, file_name, plots_dir, models):
    """Plot legibility scores based on correctness categories with flexible model support."""
    # Prepare data structures
    categories = ["Correct", "Partially Correct", "Incorrect"]
    
    # Extract all metrics from the data
    all_metrics = set()
    for item in data:
        for metric in item.get("legibility", {}):
            all_metrics.add(metric)
    
    # Initialize data dictionaries
    data_by_category = {cat: {metric: [] for metric in all_metrics} for cat in categories}
    
    # Find the first model that has correctness data
    correctness_model = None
    for model in models:
        for item in data:
            if model in item.get("correctness", {}):
                correctness_model = model
                break
        if correctness_model:
            break
    
    if not correctness_model:
        print("No correctness data found for plotting")
        return
    
    # Extract data
    for q_data in data:
        correctness = q_data.get("correctness", {}).get(correctness_model, {}).get("correctness")
        if not correctness:
            continue
        
        # Map correctness to category
        if correctness == "correct":
            cat = "Correct"
        elif correctness == "partially_correct":
            cat = "Partially Correct"
        elif correctness == "incorrect":
            cat = "Incorrect"
        else:
            continue  # Skip N/A or error
        
        # Collect legibility scores for this question
        for metric in all_metrics:
            if metric in q_data.get("legibility", {}):
                score = q_data["legibility"][metric].get("score")
                if score is not None and score != "N/A" and isinstance(score, (int, float)):
                    data_by_category[cat][metric].append(score)
    
    # Check if we have any data to plot
    has_data = False
    for cat in categories:
        for metric in all_metrics:
            if data_by_category[cat][metric]:
                has_data = True
                break
        if has_data:
            break
    
    if not has_data:
        print("No legibility data found for correctness categories")
        return
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Set up positions
    x = np.arange(len(categories))
    num_metrics = len(all_metrics)
    width = 0.8 / num_metrics if num_metrics > 0 else 0.2
    
    # Get colors
    colors = analysis_utils.get_model_colors()
    
    # Plot bars for each metric
    for i, metric in enumerate(sorted(all_metrics)):
        model_name = metric.split("_")[0]
        color = colors[model_name] if hasattr(colors, '__getitem__') else colors.get(model_name, '#7f8c8d')
        
        # Calculate statistics
        means = []
        stds = []
        for cat in categories:
            values = data_by_category[cat][metric]
            if values:
                means.append(np.mean(values))
                stds.append(np.std(values))
            else:
                means.append(0)
                stds.append(0)
        
        # Plot bars
        offset = (i - num_metrics/2 + 0.5) * width
        bars = ax.bar(x + offset, means, width, 
                      yerr=stds, capsize=3,
                      label=metric.replace('_', ' ').title(),
                      color=color, alpha=0.8)
    
    # Customize plot
    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title(f"Illegibility by Correctness - {file_name}", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 9.5)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_legibility_by_correctness.png")
    plt.savefig(plot_path, bbox_inches='tight')
    plt.close()
    print(f"Illegibility by correctness plot saved to {plot_path}")

def process_regular_file_flexible(file_path, plots_dir=None):
    """Process a single score file with flexible model detection."""
    print(f"Analyzing: {file_path}")
    file_name = os.path.basename(file_path).replace('_scores.json', '')
    
    # Load data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Check if any data exists
    if not data:
        print(f"No data found in {file_path}")
        return None, None
    
    # Analyze with flexible model detection
    stats = analyze_scores_flexible(data)
    
    # Print summary
    print(f"\nSummary for {file_name}:")
    
    # Print legibility stats
    print("\nLegibility Scores:")
    for section, section_stats in stats["legibility"].items():
        if section_stats["avg_score"] is not None:
            print(f"{section}: Avg score {section_stats['avg_score']:.2f} "
                  f"(σ={section_stats['std_dev']:.2f}, max={section_stats['max_score']:.2f}) "
                  f"from {section_stats['count']} samples (N/A: {section_stats['na_count']})")
        else:
            print(f"{section}: No valid scores found (N/A: {section_stats['na_count']})")
    
    # Print correctness stats
    print("\nCorrectness Assessment:")
    for model, model_stats in stats["correctness"].items():
        total = model_stats["total"]
        if total > 0:
            print(f"{model}: "
                  f"Correct: {model_stats['correct']} ({model_stats['correct_percentage']:.1f}%), "
                  f"Partially: {model_stats['partially_correct']} ({model_stats['partially_percentage']:.1f}%), "
                  f"Incorrect: {model_stats['incorrect']} ({model_stats['incorrect_percentage']:.1f}%), "
                  f"N/A: {model_stats['N/A']}, "
                  f"Errors: {model_stats['error']}")
        else:
            print(f"{model}: No assessments found")
    
    # Generate plots if requested
    if plots_dir and stats["legibility"]:
        # Update colors for new models if needed
        colors = analysis_utils.get_model_colors()
        models = extract_model_names_from_data(data)
        
        # Use existing plotting functions
        try:
            analysis_utils.plot_legibility_scores(stats, file_name, plots_dir)
            analysis_utils.plot_correctness_assessment(stats, file_name, plots_dir)
            plot_legibility_by_correctness_flexible(data, file_name, plots_dir, models)
            analysis_utils.plot_length_vs_legibility(data, file_name, plots_dir)
        except Exception as e:
            print(f"Error generating plots: {e}")
    
    return file_name, stats

def main():
    parser = argparse.ArgumentParser(description='Analyze scores with flexible model support')
    parser.add_argument('--dir', type=str, default='scores', help='Directory containing score JSON files')
    parser.add_argument('--pattern', type=str, default='*_scores.json', help='File pattern to match')
    parser.add_argument('--plots', action='store_true', help='Generate plots of the results')
    parser.add_argument('--file', type=str, help='Process a single specific file')
    args = parser.parse_args()
    
    # Setup matplotlib if plotting
    if args.plots:
        analysis_utils.setup_matplotlib()
        plots_dir = analysis_utils.create_plots_directory()
    else:
        plots_dir = None
    
    # Process files
    if args.file:
        # Process single file
        process_regular_file_flexible(args.file, plots_dir)
    else:
        # Process all matching files
        file_pattern = os.path.join(args.dir, args.pattern)
        files = glob.glob(file_pattern)
        print(f"Found {len(files)} score files to analyze")
        
        for file_path in files:
            try:
                process_regular_file_flexible(file_path, plots_dir)
                print("-" * 80)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue

if __name__ == "__main__":
    main()