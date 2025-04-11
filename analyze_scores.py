import os
import json
import glob
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Patch
from matplotlib.ticker import MaxNLocator

# ===== SETUP FUNCTIONS =====

def setup_matplotlib():
    """Set up matplotlib with custom fonts and style."""
    fm.fontManager.addfont('fonts/Montserrat-Regular.ttf')
    plt.rcParams['font.family'] = 'Montserrat'
    plt.rcParams['hatch.linewidth'] = 0.3  # Thinner hatch lines

def create_plots_directory():
    """Create a directory for saving plots if it doesn't exist."""
    plots_dir = "plots/all"
    os.makedirs(plots_dir, exist_ok=True)
    return plots_dir

# ===== DATA LOADING FUNCTIONS =====

def load_json_file(file_path):
    """Load a JSON file and return the data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Aliases for semantic clarity
load_score_file = load_json_file
load_claude_score_file = load_json_file

# ===== DATA ANALYSIS FUNCTIONS =====

def analyze_legibility_scores(data):
    """Extract and analyze legibility scores from the data."""
    # Define sections to analyze
    section_scores = {
        "deepseek_response": [], "deepseek_reasoning": [],
        "cutoff_response": [], "cutoff_reasoning": [],
        "anthropic_response": [], "anthropic_reasoning": [],
        "openai_response": [], "openai_reasoning": []
    }
    
    section_na_counts = {section: 0 for section in section_scores}
    
    # Process each result
    for result in data:
        for section, score_data in result.get("legibility", {}).items():
            if section in section_scores:
                if score_data.get("score") == "N/A":
                    section_na_counts[section] += 1
                elif isinstance(score_data.get("score"), (int, float)):
                    section_scores[section].append(score_data["score"])
    
    # Calculate statistics
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
                "total": total
            }
        else:
            legibility_stats[section] = {
                "avg_score": None,
                "std_dev": None,
                "max_score": None,
                "count": 0,
                "na_count": na_count,
                "total": total
            }
    
    return {
        "legibility_stats": legibility_stats,
        "raw_scores": section_scores
    }

def analyze_correctness_scores(data, models=None):
    """Extract and analyze correctness scores from the data."""
    if models is None:
        models = ["deepseek", "cutoff", "anthropic", "openai"]
    
    # Initialize counters
    correctness_counts = {
        model: {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
        for model in models
    }
    
    # Process each result
    for result in data:
        for model, assessment in result.get("correctness", {}).items():
            if model in models:
                correctness = assessment.get("correctness", "N/A")
                if correctness in correctness_counts[model]:
                    correctness_counts[model][correctness] += 1
                else:
                    correctness_counts[model]["error"] += 1
    
    # Calculate percentages
    correctness_stats = {}
    for model, counts in correctness_counts.items():
        total = sum(counts.values())
        
        correctness_stats[model] = {
            **counts,  # Include all original counts
            "total": total,
            "correct_percentage": (counts["correct"] / total * 100) if total > 0 else 0,
            "partially_percentage": (counts["partially_correct"] / total * 100) if total > 0 else 0,
            "incorrect_percentage": (counts["incorrect"] / total * 100) if total > 0 else 0
        }
    
    return correctness_stats

def analyze_scores(data):
    """Analyze both legibility and correctness scores from data."""
    legibility_results = analyze_legibility_scores(data)
    correctness_results = analyze_correctness_scores(data)
    
    return {
        "legibility": legibility_results["legibility_stats"],
        "correctness": correctness_results,
        "raw_legibility_scores": legibility_results["raw_scores"]
    }

def analyze_claude_scores(data):
    """Analyze scores from a Claude answers JSON file."""
    # Extract section names from the summary
    sections = list(data.get("summary", {}).keys())
    
    # Prepare data structure for correctness scores
    correctness_stats = {}
    for section in sections:
        section_summary = data["summary"].get(section, {})
        section_percentages = data["percentages"].get(section, {})
        
        # Calculate total
        total = sum(section_summary.values())
        
        correctness_stats[section] = {
            "correct": section_summary.get("correct", 0),
            "partially_correct": section_summary.get("partially_correct", 0),
            "incorrect": section_summary.get("incorrect", 0),
            "N/A": section_summary.get("N/A", 0),
            "error": section_summary.get("error", 0),
            "total": total,
            "correct_percentage": section_percentages.get("correct_pct", 0),
            "partially_percentage": section_percentages.get("partially_pct", 0),
            "incorrect_percentage": section_percentages.get("incorrect_pct", 0)
        }
    
    return {"correctness": correctness_stats}

def extract_claude_stats_from_file(claude_scores_file):
    """Extract Claude stats from the scores file."""
    try:
        data = load_json_file(claude_scores_file)
        
        # Extract stats from our format
        summary = data.get("summary", {})
        percentages = data.get("percentages", {})
        
        return {
            "correct": summary.get("correct", 0),
            "partially_correct": summary.get("partially_correct", 0),
            "incorrect": summary.get("incorrect", 0),
            "N/A": summary.get("N/A", 0),
            "error": summary.get("error", 0),
            "total_valid": percentages.get("total_valid", 0),
            "correct_pct": percentages.get("correct_pct", 0),
            "partially_pct": percentages.get("partially_pct", 0),
            "incorrect_pct": percentages.get("incorrect_pct", 0)
        }
    except Exception as e:
        print(f"Error extracting Claude stats from file {claude_scores_file}: {e}")
        return None

# ===== PRINTING FUNCTIONS =====

def format_legibility_stats(section, stats):
    """Format legibility stats for printing."""
    if stats["avg_score"] is None:
        return f"{section}: No valid scores found (N/A: {stats['na_count']})"
    
    return (f"{section}: Avg score {stats['avg_score']:.2f} "
            f"(σ={stats['std_dev']:.2f}, max={stats['max_score']:.2f}) "
            f"from {stats['count']} samples (N/A: {stats['na_count']})")

def format_correctness_stats(model, stats):
    """Format correctness stats for printing."""
    total = stats["total"]
    if total <= 0:
        return f"{model.capitalize()}: No assessments found"
    
    return (f"{model.capitalize()}: "
            f"Correct: {stats['correct']} ({stats['correct_percentage']:.1f}%), "
            f"Partially: {stats['partially_correct']} ({stats['partially_percentage']:.1f}%), "
            f"Incorrect: {stats['incorrect']} ({stats['incorrect_percentage']:.1f}%), "
            f"N/A: {stats['N/A']}, "
            f"Errors: {stats['error']}")

def print_summary(stats, file_name):
    """Print a summary of stats for a file."""
    print(f"\nSummary for {file_name}:")
    
    # Print legibility stats
    print("\nLegibility Scores:")
    for section, section_stats in stats["legibility"].items():
        print(format_legibility_stats(section, section_stats))
    
    # Print correctness stats
    print("\nCorrectness Assessment:")
    for model, model_stats in stats["correctness"].items():
        print(format_correctness_stats(model, model_stats))

def print_claude_summary(stats, file_name):
    """Print a summary of Claude answer stats for a file."""
    print(f"\nSummary for {file_name}:")
    
    # Print correctness stats
    print("\nCorrectness Assessment:")
    for section, section_stats in stats["correctness"].items():
        print(format_correctness_stats(section, section_stats))

def compare_files(all_stats):
    """Compare stats across different files."""
    # Compare legibility scores
    for section in ["deepseek_response", "deepseek_reasoning", "cutoff_response", "cutoff_reasoning", 
                   "anthropic_response", "anthropic_reasoning", "openai_response", "openai_reasoning"]:
        print(f"\n--- {section} comparison ---")
        print(f"{'File':<40} {'Avg Score':<10} {'Std Dev':<10} {'Max':<10} {'Count':<10} {'N/A':<10}")
        print("-" * 90)
        
        for file_name, stats in all_stats.items():
            section_stats = stats["legibility"].get(section, {})
            avg_score = section_stats.get("avg_score")
            std_dev = section_stats.get("std_dev")
            max_score = section_stats.get("max_score")
            count = section_stats.get("count", 0)
            na_count = section_stats.get("na_count", 0)
            
            avg_display = f"{avg_score:.2f}" if avg_score is not None else "N/A"
            std_display = f"{std_dev:.2f}" if std_dev is not None else "N/A"
            max_display = f"{max_score:.2f}" if max_score is not None else "N/A"
            print(f"{file_name:<40} {avg_display:<10} {std_display:<10} {max_display:<10} {count:<10} {na_count:<10}")
    
    # Compare correctness assessments
    for model in ["deepseek", "cutoff", "anthropic", "openai"]:
        print(f"\n--- {model.capitalize()} correctness comparison ---")
        print(f"{'File':<40} {'Correct':<20} {'Partially':<20} {'Incorrect':<20} {'N/A':<10}")
        print("-" * 110)
        
        for file_name, stats in all_stats.items():
            model_stats = stats["correctness"].get(model, {})
            correct = model_stats.get("correct", 0)
            partially = model_stats.get("partially_correct", 0)
            incorrect = model_stats.get("incorrect", 0)
            na_count = model_stats.get("N/A", 0)
            total = model_stats.get("total", 0)
            
            if total > 0:
                correct_display = f"{correct} ({model_stats['correct_percentage']:.1f}%)"
                partially_display = f"{partially} ({model_stats['partially_percentage']:.1f}%)"
                incorrect_display = f"{incorrect} ({model_stats['incorrect_percentage']:.1f}%)"
            else:
                correct_display = "0 (0.0%)"
                partially_display = "0 (0.0%)"
                incorrect_display = "0 (0.0%)"
                
            print(f"{file_name:<40} {correct_display:<20} {partially_display:<20} {incorrect_display:<20} {na_count:<10}")

# ===== PLOTTING HELPERS =====

def get_model_colors():
    """Get a mapping of model names to colors."""
    return {
        'deepseek': '#3498db', 
        'cutoff': '#2ecc71', 
        'openai': '#9b59b6', 
        'anthropic': '#e74c3c'
    }

def get_model_display_name(model_key):
    """Convert internal model names to display names."""
    model_map = {
        'deepseek': 'Default',
        'cutoff': 'With Cutoff',
        'openai': 'With GPT-4o Paraphrase',
        'anthropic': 'With Claude Paraphrase',
        'claude': 'Baseline'
    }
    return model_map.get(model_key, model_key)

def get_section_display_name(section):
    """Convert section names to display names."""
    mapping = {
        "claude": "Baseline",
        "DeepSeek reasoning": "With r1 CoT",
        "Cut off deepseek reasoning": "With cutoff r1 CoT",
        "Anthropic completion": "With Claude paraphrase",
        "OpenAI completion": "With GPT-4o paraphrase",
        "cutoff_deepseek_completion reasoning": "With r1 reasoning after cutoff",
        "paraphrased_deepseek_completion_anthropic reasoning": "With r1 reasoning after Claude paraphrase",
        "paraphrased_deepseek_completion_openai reasoning": "With r1 reasoning after GPT-4o paraphrase"
    }
    return mapping.get(section, f"With {section.replace('_', ' ').capitalize()}")

def create_hatched_bar(ax, x, height, width=0.25, color='blue', hatch='', label=None, alpha=1.0):
    """Create a bar with optional hatching."""
    bar = ax.bar(x, height, width, color=color, alpha=alpha, label=label)
    if hatch:
        for b in bar:
            b.set_hatch(hatch)
    return bar

def add_value_labels(ax, bars, values, counts=None, threshold=0, offset=2, inside=False):
    """Add text labels with values to bars."""
    for i, (bar, value) in enumerate(zip(bars, values)):
        if value <= threshold:
            continue
            
        text_x = bar.get_x() + bar.get_width()/2
        
        if inside:
            text_y = value/2
            text_color = 'white'
            fontweight = 'bold'
        else:
            text_y = value + offset
            text_color = 'black'
            fontweight = 'normal'
        
        text = f"{value:.1f}%" if isinstance(value, float) else f"{value}"
        if counts is not None and i < len(counts):
            text = f"{text} (n={counts[i]})"
            
        ax.text(text_x, text_y, text, 
                ha='center', va='center' if inside else 'bottom', 
                color=text_color, fontweight=fontweight, fontsize=9)

# ===== PLOTTING FUNCTIONS =====

def plot_legibility_scores(stats, file_name, plots_dir, std_display=None):
    """Plot legibility scores with different visualization options."""
    # Extract data for plotting
    sections = []
    avg_scores = []
    std_devs = []
    counts = []
    raw_scores = stats.get("raw_legibility_scores", {})
    
    for section, section_stats in stats["legibility"].items():
        if section_stats["avg_score"] is not None:
            sections.append(section)
            avg_scores.append(section_stats["avg_score"])
            std_devs.append(section_stats["std_dev"])
            counts.append(section_stats["count"])
    
    if not sections:
        print(f"No valid legibility scores to plot for {file_name}")
        return
    
    # Process section information for display
    colors = get_model_colors()
    bar_colors = []
    models = []
    hatches = []
    
    for section in sections:
        parts = section.split('_')
        model, eval_type = parts[0], parts[1]
        bar_colors.append(colors.get(model.lower(), '#7f8c8d'))
        models.append(get_model_display_name(model))
        hatches.append('///' if eval_type == 'reasoning' else '')
    
    # Define display types to generate
    display_types = ["error_bars", "shaded", "violin"] if std_display is None else [std_display]
    
    # Create each type of plot
    for display_type in display_types:
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if display_type == "error_bars":
            plot_legibility_with_error_bars(ax, sections, avg_scores, std_devs, bar_colors, hatches)
        elif display_type == "shaded":
            plot_legibility_with_shading(ax, sections, avg_scores, std_devs, bar_colors, hatches)
        elif display_type == "violin":
            plot_legibility_with_violin(ax, sections, avg_scores, std_devs, bar_colors, hatches, raw_scores)
        
        # Set up x-axis without labels (replaced by legend)
        ax.set_xticks(range(len(sections)))
        ax.set_xticklabels([''] * len(sections))
        ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        
        # Group models below x-axis
        add_model_group_labels(ax, models)
        
        # Create custom legend for eval types
        add_eval_type_legend(ax)
        
        # Customize plot
        ax.set_title(f'Illegibility In Various Settings (n={min(counts)})', fontsize=14)
        ax.set_ylabel('Illegibility Score', fontsize=12)
        ax.set_ylim(0, 9.5)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        
        # Save plot
        plot_path = os.path.join(plots_dir, f"{file_name}_legibility_scores_{display_type}.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"Legibility scores plot ({display_type}) saved to {plot_path}")

def plot_legibility_with_error_bars(ax, sections, avg_scores, std_devs, bar_colors, hatches):
    """Plot legibility scores with error bars."""
    bars = ax.bar(range(len(sections)), avg_scores, alpha=1, color=bar_colors)
    error_bars = ax.errorbar(range(len(sections)), avg_scores, yerr=std_devs, 
                            capsize=5, alpha=0.7, ecolor='black', linestyle='none')
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)

def plot_legibility_with_shading(ax, sections, avg_scores, std_devs, bar_colors, hatches):
    """Plot legibility scores with shaded regions for standard deviation."""
    bars = ax.bar(range(len(sections)), avg_scores, alpha=1, color=bar_colors)
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)
        
    for i, (avg, std) in enumerate(zip(avg_scores, std_devs)):
        lower, upper = max(1, avg - std), min(9, avg + std)
        fill = ax.fill_between([i-0.4, i+0.391], [lower, lower], [upper, upper], 
                              color=bar_colors[i], alpha=0.3)
        fill.set_hatch(hatches[i])

def plot_legibility_with_violin(ax, sections, avg_scores, std_devs, bar_colors, hatches, raw_scores):
    """Plot legibility scores using violin plots."""
    try:
        violin_data = []
        for i, section in enumerate(sections):
            if section in raw_scores and len(raw_scores[section]) > 1:
                valid_scores = [float(score) for score in raw_scores[section]
                             if isinstance(score, (int, float))
                             or (isinstance(score, str) and score.replace('.', '', 1).isdigit())]
                violin_data.append(valid_scores if valid_scores else [avg_scores[i]])
            else:
                violin_data.append([avg_scores[i] - 0.1, avg_scores[i], avg_scores[i] + 0.1])
                
        violin_parts = ax.violinplot(
            violin_data,
            range(len(sections)),
            showmeans=False,
            showmedians=False,
            showextrema=False,
            points=200,
            bw_method=0.5,
        )
        
        for i, pc in enumerate(violin_parts['bodies']):
            pc.set_facecolor(bar_colors[i])
            if hatches[i]:
                pc.set_hatch(hatches[i])
            pc.set_alpha(1)
            pc.set_edgecolor('black')
            pc.set_linewidth(0.5)
            
    except Exception as e:
        print(f"Warning: Could not create violin plots, falling back to error bars: {e}")
        plot_legibility_with_error_bars(ax, sections, avg_scores, std_devs, bar_colors, hatches)

def add_model_group_labels(ax, models):
    """Add model labels as group headers below the x-axis."""
    model_groups = {}
    for i, model in enumerate(models):
        if model not in model_groups:
            model_groups[model] = []
        model_groups[model].append(i)
    
    for model, positions in model_groups.items():
        mid_point = sum(positions) / len(positions)
        ax.annotate(model, xy=(mid_point, -0.03), xycoords=('data', 'axes fraction'),
                   ha='center', va='top', fontsize=11)

def add_eval_type_legend(ax):
    """Add a legend for evaluation types (answer vs reasoning)."""
    legend_elements = [
        Patch(facecolor='gray', edgecolor='black', label='Answer'),
        Patch(facecolor='gray', hatch='///', edgecolor='black', alpha=0.75, label='Reasoning')
    ]
    ax.legend(handles=legend_elements, loc='upper right')

def plot_correctness_assessment(stats, file_name, plots_dir):
    """Plot correctness assessment for a file."""
    plt.figure(figsize=(12, 6))
    
    # Prepare data
    models = list(stats["correctness"].keys())
    correct_pct = [stats["correctness"][model]["correct_percentage"] for model in models]
    partially_pct = [stats["correctness"][model]["partially_percentage"] for model in models]
    incorrect_pct = [stats["correctness"][model]["incorrect_percentage"] for model in models]
    counts = [stats["correctness"][model]["total"] for model in models]
    correct_counts = [stats["correctness"][model]["correct"] for model in models]
    partially_counts = [stats["correctness"][model]["partially_correct"] for model in models]
    incorrect_counts = [stats["correctness"][model]["incorrect"] for model in models]
    
    # Define bar width and positions
    bar_width = 0.25
    r1 = np.arange(len(models))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    # Create bars
    bars1 = plt.bar(r1, correct_pct, width=bar_width, label='Correct', color='#2ecc71', alpha=0.8)
    bars2 = plt.bar(r2, partially_pct, width=bar_width, label='Partially Correct', color='#f39c12', alpha=0.8)
    bars3 = plt.bar(r3, incorrect_pct, width=bar_width, label='Incorrect', color='#e74c3c', alpha=0.8)

    # Format x-axis labels with model display names
    model_labels = [get_model_display_name(model) for model in models]
    
    # Add labels and customize plot
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.title(f'Correctness Assessment for r1 (n={min(counts)})', fontsize=14)
    plt.xticks([r + bar_width for r in range(len(models))], model_labels)
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels
    for i, bars in enumerate([bars1, bars2, bars3]):
        values = [correct_pct, partially_pct, incorrect_pct][i]
        
        for bar, value in zip(bars, values):
            if value > 0:
                plt.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value:.1f}%', 
                        ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()

    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_correctness_assessment.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Correctness assessment plot saved to {plot_path}")

def plot_claude_correctness(stats, file_name, plots_dir, claude_baseline=None):
    """Plot correctness for Claude answers."""
    plt.figure(figsize=(14, 8))
    
    # Prepare data
    sections = list(stats["correctness"].keys())
    correct_pct = [stats["correctness"][section]["correct_percentage"] for section in sections]
    partially_pct = [stats["correctness"][section]["partially_percentage"] for section in sections]
    incorrect_pct = [stats["correctness"][section]["incorrect_percentage"] for section in sections]
    correct_counts = [stats["correctness"][section]["correct"] for section in sections]
    partially_counts = [stats["correctness"][section]["partially_correct"] for section in sections]
    incorrect_counts = [stats["correctness"][section]["incorrect"] for section in sections]
    total_counts = [stats["correctness"][section]["total"] for section in sections]

    # Add Claude baseline if provided
    if claude_baseline is not None:
        sections.insert(0, "claude")
        correct_pct.insert(0, claude_baseline["correct_pct"])
        partially_pct.insert(0, claude_baseline["partially_pct"])
        incorrect_pct.insert(0, claude_baseline["incorrect_pct"])
        correct_counts.insert(0, claude_baseline["correct"])
        partially_counts.insert(0, claude_baseline["partially_correct"])
        incorrect_counts.insert(0, claude_baseline["incorrect"])
        total_counts.insert(0, claude_baseline["total_valid"])
    
    # Define bar width and positions
    bar_width = 0.25
    r1 = np.arange(len(sections))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    # Create bars
    bars1 = plt.bar(r1, correct_pct, width=bar_width, label='Correct', color='#2ecc71', alpha=0.8)
    bars2 = plt.bar(r2, partially_pct, width=bar_width, label='Partially Correct', color='#f39c12', alpha=0.8)
    bars3 = plt.bar(r3, incorrect_pct, width=bar_width, label='Incorrect', color='#e74c3c', alpha=0.8)

    # Format section labels
    section_labels = [get_section_display_name(s) for s in sections]
    
    # Add labels and customize plot
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.title(f'Correctness of Claude Answers (n={total_counts[0]})', fontsize=14)
    plt.xticks([r + bar_width for r in range(len(sections))], section_labels, rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels
    for i, (bars, values) in enumerate([
            (bars1, correct_pct),
            (bars2, partially_pct),
            (bars3, incorrect_pct)
        ]):
        for bar, value in zip(bars, values):
            if value > 0:
                plt.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value:.1f}%', 
                        ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_claude_correctness.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Claude correctness assessment plot saved to {plot_path}")

def plot_comparison_legibility(all_stats, section, plots_dir):
    """Plot comparison of legibility scores across files for a section."""
    plt.figure(figsize=(14, 7))
    
    # Extract data
    file_names = []
    avg_scores = []
    std_devs = []
    counts = []
    
    for file_name, stats in all_stats.items():
        section_stats = stats["legibility"].get(section, {})
        avg_score = section_stats.get("avg_score")
        
        if avg_score is not None:
            file_names.append(file_name)
            avg_scores.append(avg_score)
            std_devs.append(section_stats.get("std_dev", 0))
            counts.append(section_stats.get("count", 0))
    
    if not file_names:
        print(f"No valid data to plot comparison for {section}")
        return
    
    # Get model and component from section
    model = section.split('_')[0]
    component = section.split('_')[1]
    
    # Get color based on model
    colors = get_model_colors()
    bar_color = colors.get(model, '#7f8c8d')
    
    # Create bars
    bars = plt.bar(file_names, avg_scores, yerr=std_devs, alpha=0.8, color=bar_color)
    
    # Add value labels and counts inside bars
    for bar, score, count in zip(bars, avg_scores, counts):
        # Add score on top
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{score:.2f}', ha='center', va='bottom', fontsize=9)
        
        # Add count inside bar if bar is tall enough
        if bar.get_height() > 0.5:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                    f'n={count}', ha='center', va='center', 
                    color='white', fontweight='bold', fontsize=9)
    
    # Customize plot
    plt.title(f'Comparison of {model.capitalize()} {component.capitalize()} Legibility Scores', fontsize=14)
    plt.ylabel('Average Score', fontsize=12)
    plt.ylim(0, max(avg_scores) * 1.2)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"comparison_{section}_legibility.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Comparison plot for {section} saved to {plot_path}")

def plot_comparison_correctness(all_stats, model, plots_dir):
    """Plot comparison of correctness across files for a model."""
    plt.figure(figsize=(14, 7))
    
    # Prepare data
    file_names = list(all_stats.keys())
    correct_pcts = []
    partially_pcts = []
    incorrect_pcts = []
    correct_counts = []
    partially_counts = []
    incorrect_counts = []
    total_counts = []
    
    for file_name, stats in all_stats.items():
        model_stats = stats["correctness"].get(model, {})
        correct_pcts.append(model_stats.get("correct_percentage", 0))
        partially_pcts.append(model_stats.get("partially_percentage", 0))
        incorrect_pcts.append(model_stats.get("incorrect_percentage", 0))
        correct_counts.append(model_stats.get("correct", 0))
        partially_counts.append(model_stats.get("partially_correct", 0))
        incorrect_counts.append(model_stats.get("incorrect", 0))
        total_counts.append(model_stats.get("total", 0))
    
    # Define bar width and positions
    x = np.arange(len(file_names))
    width = 0.25
    
    # Create bars
    bars1 = plt.bar(x - width, correct_pcts, width, label='Correct', color='#2ecc71', alpha=0.8)
    bars2 = plt.bar(x, partially_pcts, width, label='Partially Correct', color='#f39c12', alpha=0.8)
    bars3 = plt.bar(x + width, incorrect_pcts, width, label='Incorrect', color='#e74c3c', alpha=0.8)
    
    # Add value labels and counts
    for i, (bars, values, counts) in enumerate([
            (bars1, correct_pcts, correct_counts),
            (bars2, partially_pcts, partially_counts),
            (bars3, incorrect_pcts, incorrect_counts)
        ]):
        for j, (bar, value, count) in enumerate(zip(bars, values, counts)):
            # Add percentage on top if value is significant
            if value > 0:
                plt.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value:.1f}%', 
                        ha='center', va='bottom', fontsize=9)
                
                # Add count inside bar if bar is tall enough
                if value > 10:
                    plt.text(bar.get_x() + bar.get_width()/2, value/2,
                            f'n={count}', ha='center', va='center', 
                            color='white', fontweight='bold', fontsize=8)
    
    # Add total counts beneath the file names
    for i, count in enumerate(total_counts):
        plt.text(i, -5, f'total={count}', ha='center', va='top', fontsize=8)
    
    # Customize plot
    plt.title(f'Comparison of {model.capitalize()} Correctness Assessments', fontsize=14)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.xticks(x, file_names, rotation=45, ha='right')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylim(0, 100)
    plt.subplots_adjust(bottom=0.2)  # Make room for counts text
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"comparison_{model}_correctness.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Comparison plot for {model} correctness saved to {plot_path}")

def plot_overall_model_performance(all_stats, plots_dir):
    """Plot overall model performance across all files."""
    # Aggregate data across all files
    models = ["deepseek", "cutoff", "anthropic", "openai"]
    correct_counts = {model: 0 for model in models}
    partially_counts = {model: 0 for model in models}
    incorrect_counts = {model: 0 for model in models}
    total_counts = {model: 0 for model in models}
    
    for file_stats in all_stats.values():
        for model in models:
            model_stats = file_stats["correctness"].get(model, {})
            correct_counts[model] += model_stats.get("correct", 0)
            partially_counts[model] += model_stats.get("partially_correct", 0)
            incorrect_counts[model] += model_stats.get("incorrect", 0)
            total_counts[model] += (model_stats.get("correct", 0) + 
                                  model_stats.get("partially_correct", 0) + 
                                  model_stats.get("incorrect", 0))
    
    # Calculate percentages
    correct_pcts = []
    partially_pcts = []
    incorrect_pcts = []
    
    for model in models:
        if total_counts[model] > 0:
            correct_pcts.append((correct_counts[model] / total_counts[model]) * 100)
            partially_pcts.append((partially_counts[model] / total_counts[model]) * 100)
            incorrect_pcts.append((incorrect_counts[model] / total_counts[model]) * 100)
        else:
            correct_pcts.append(0)
            partially_pcts.append(0)
            incorrect_pcts.append(0)
    
    # Create plot
    plt.figure(figsize=(12, 8))
    
    # Define bar width and positions
    x = np.arange(len(models))
    width = 0.25
    
    # Create stacked bars
    plt.bar(x, correct_pcts, width, label='Correct', color='#2ecc71')
    plt.bar(x, partially_pcts, width, bottom=correct_pcts, label='Partially Correct', color='#f39c12')
    bottom_vals = [c + p for c, p in zip(correct_pcts, partially_pcts)]
    plt.bar(x, incorrect_pcts, width, bottom=bottom_vals, label='Incorrect', color='#e74c3c')
    
    # Add value annotations
    for i, model in enumerate(models):
        # Correct
        if correct_pcts[i] > 5:  # Only add text if there's enough space
            plt.text(i, correct_pcts[i]/2, f'{correct_pcts[i]:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
        
        # Partially correct
        if partially_pcts[i] > 5:
            plt.text(i, correct_pcts[i] + partially_pcts[i]/2, f'{partially_pcts[i]:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
        
        # Incorrect
        if incorrect_pcts[i] > 5:
            plt.text(i, bottom_vals[i] + incorrect_pcts[i]/2, f'{incorrect_pcts[i]:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
        
        # Add total count below the x-axis
        plt.text(i, -5, f'n={total_counts[model]}', ha='center', va='top')
    
    # Customize plot
    plt.title('Overall Model Performance Across All Files', fontsize=16)
    plt.ylabel('Percentage (%)', fontsize=14)
    plt.xticks(x, [get_model_display_name(m) for m in models], fontsize=12)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)
    
    # Adjust layout to make room for the legend
    plt.subplots_adjust(bottom=0.2)
    
    # Save plot
    plot_path = os.path.join(plots_dir, "overall_model_performance.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Overall model performance plot saved to {plot_path}")

def plot_claude_comparisons(stats, file_name, plots_dir):
    """Plot comparison of different reasoning sections for Claude."""
    plt.figure(figsize=(14, 8))
    
    # Group sections by model type
    model_sections = {}
    for section in stats["correctness"].keys():
        if section not in model_sections:
            model_sections[section] = []  
        model_sections[section].append(section)
    
    # Create a stacked bar chart
    models = list(model_sections.keys())
    x = np.arange(len(models))
    width = 0.6
    
    # Collect data for each model
    correct_values = []
    partially_values = []
    incorrect_values = []
    
    for model in models:
        # Average the values across all sections for this model
        sections = model_sections[model]
        correct_avg = np.mean([stats["correctness"][s]["correct_percentage"] for s in sections])
        partially_avg = np.mean([stats["correctness"][s]["partially_percentage"] for s in sections])
        incorrect_avg = np.mean([stats["correctness"][s]["incorrect_percentage"] for s in sections])
        
        correct_values.append(correct_avg)
        partially_values.append(partially_avg)
        incorrect_values.append(incorrect_avg)
    
    # Create stacked bars
    plt.bar(x, correct_values, width, label='Correct', color='#2ecc71')
    plt.bar(x, partially_values, width, bottom=correct_values, label='Partially Correct', color='#f39c12')
    bottom_vals = [c + p for c, p in zip(correct_values, partially_values)]
    plt.bar(x, incorrect_values, width, bottom=bottom_vals, label='Incorrect', color='#e74c3c')
    
    # Add value annotations
    for i, model in enumerate(models):
        # Correct
        if correct_values[i] > 5:
            plt.text(i, correct_values[i]/2, f'{correct_values[i]:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
        
        # Partially correct
        if partially_values[i] > 5:
            plt.text(i, correct_values[i] + partially_values[i]/2, f'{partially_values[i]:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
        
        # Incorrect
        if incorrect_values[i] > 5:
            plt.text(i, bottom_vals[i] + incorrect_values[i]/2, f'{incorrect_values[i]:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold')
    
    # Customize plot
    plt.title('Model Performance in Reasoning Sections', fontsize=16)
    plt.ylabel('Percentage (%)', fontsize=14)
    plt.xticks(x, [m.replace('_', ' ').capitalize() for m in models], fontsize=12, rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.legend(loc='upper right')
    
    # Adjust layout to make room for the legend
    plt.subplots_adjust(bottom=0.45)
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_model_comparison.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Model comparison plot saved to {plot_path}")

# ===== FILE PROCESSING FUNCTIONS =====

def process_regular_file(file_path, plots_dir=None, std_display=None):
    """Process a single regular score file."""
    try:
        print(f"Analyzing: {file_path}")
        file_name = os.path.basename(file_path).replace('_scores.json', '')
        data = load_score_file(file_path)
        stats = analyze_scores(data)
        
        # Print summary
        print_summary(stats, file_name)
        
        # Generate plots if requested
        if plots_dir:
            plot_legibility_scores(stats, file_name, plots_dir, std_display=std_display)
            plot_correctness_assessment(stats, file_name, plots_dir)
        
        return file_name, stats
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None, None

def process_claude_file(file_path, plots_dir=None, claude_baseline=None):
    """Process a single Claude answers score file."""
    try:
        print(f"Analyzing Claude answers file: {file_path}")
        file_name = os.path.basename(file_path).replace('.json', '')
        data = load_claude_score_file(file_path)
        stats = analyze_claude_scores(data)
        
        # Print summary
        print_claude_summary(stats, file_name)
        
        # Generate plots if requested
        if plots_dir:
            plot_claude_correctness(stats, file_name, plots_dir, claude_baseline)
            plot_claude_comparisons(stats, file_name, plots_dir)
            
        return True
    except Exception as e:
        print(f"Error processing Claude answers file {file_path}: {e}")
        return False

def process_regular_files(file_pattern, compare=False, plots=False, std_display=None):
    """Process all regular score files matching the pattern."""
    files = glob.glob(file_pattern)
    print(f"Found {len(files)} score files to analyze")
    
    all_stats = {}
    plots_dir = create_plots_directory() if plots else None
    
    for file_path in files:
        file_name, stats = process_regular_file(file_path, plots_dir, std_display)
        if file_name and stats:
            all_stats[file_name] = stats
    
    # If comparison is requested, print comparison tables and plots
    if compare and len(all_stats) > 1:
        compare_files(all_stats)
        
        if plots:
            # Plot legibility comparisons
            for section in ["deepseek_response", "deepseek_reasoning", "cutoff_response", "cutoff_reasoning", 
                           "anthropic_response", "anthropic_reasoning", "openai_response", "openai_reasoning"]:
                plot_comparison_legibility(all_stats, section, plots_dir)
            
            # Plot correctness comparisons
            for model in ["deepseek", "cutoff", "anthropic", "openai"]:
                plot_comparison_correctness(all_stats, model, plots_dir)
            
            # Plot overall model performance
            plot_overall_model_performance(all_stats, plots_dir)

# ===== MAIN FUNCTION =====

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
    parser.add_argument('--std-display', type=str, choices=['error_bars', 'shaded', 'violin'], default=None,
                        help='Type of standard deviation display (error_bars, shaded, violin)')
    
    return parser.parse_args()

def main():
    """Main function to run the analysis."""
    args = parse_arguments()
    setup_matplotlib()
    
    # Determine analysis type
    analysis_type = args.analysis_type
    if analysis_type is None:
        analysis_type = 'claude' if args.claude_file else 'regular'
    
    # Load Claude baseline if needed
    claude_baseline = None
    if args.claude_baseline and os.path.exists(args.claude_baseline):
        claude_baseline = extract_claude_stats_from_file(args.claude_baseline)
        print(f"Loaded Claude scores from {args.claude_baseline}")
    
    # Process based on analysis type
    if analysis_type == 'claude':
        if args.claude_file:
            if os.path.exists(args.claude_file):
                plots_dir = create_plots_directory() if args.plots else None
                process_claude_file(args.claude_file, plots_dir, claude_baseline)
            else:
                print(f"Claude answers file not found: {args.claude_file}")
        else:
            print("Error: When using --analysis-type=claude, you must provide a --claude-file")
    else:  # 'regular'
        file_pattern = os.path.join(args.dir, args.pattern)
        process_regular_files(file_pattern, args.compare, args.plots, args.std_display)

if __name__ == "__main__":
    main()