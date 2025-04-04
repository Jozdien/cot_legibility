import os
import json
import glob
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Patch
from matplotlib.ticker import MaxNLocator

fm.fontManager.addfont('fonts/Montserrat-Regular.ttf')
plt.rcParams['font.family'] = 'Montserrat'

def load_score_file(file_path):
    """Load a score JSON file and return the data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_scores(data):
    """Analyze scores from a single JSON file."""
    # For legibility scores
    section_scores = {
        "deepseek_response": [], 
        "deepseek_reasoning": [],
        "cutoff_response": [], 
        "cutoff_reasoning": [],
        "anthropic_response": [], 
        "anthropic_reasoning": [],
        "openai_response": [], 
        "openai_reasoning": []
    }
    
    section_na_counts = {section: 0 for section in section_scores}
    
    # For correctness scores
    correctness_models = ["deepseek", "cutoff", "anthropic", "openai"]
    correctness_counts = {
        model: {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
        for model in correctness_models
    }
    
    for result in data:
        # Process legibility scores
        for section, score_data in result.get("legibility", {}).items():
            if section in section_scores:
                if score_data.get("score") == "N/A":
                    section_na_counts[section] += 1
                elif isinstance(score_data.get("score"), (int, float)):
                    section_scores[section].append(score_data["score"])
        
        # Process correctness assessments
        for model, assessment in result.get("correctness", {}).items():
            if model in correctness_models:
                correctness = assessment.get("correctness", "N/A")
                if correctness in correctness_counts[model]:
                    correctness_counts[model][correctness] += 1
                else:
                    correctness_counts[model]["error"] += 1
    
    # Calculate legibility statistics
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
    
    # Calculate correctness statistics
    correctness_stats = {}
    for model, counts in correctness_counts.items():
        total = sum(counts.values())
        correct_percentage = (counts["correct"] / total * 100) if total > 0 else 0
        partially_percentage = (counts["partially_correct"] / total * 100) if total > 0 else 0
        incorrect_percentage = (counts["incorrect"] / total * 100) if total > 0 else 0
        
        correctness_stats[model] = {
            "correct": counts["correct"],
            "partially_correct": counts["partially_correct"],
            "incorrect": counts["incorrect"],
            "N/A": counts["N/A"],
            "error": counts["error"],
            "total": total,
            "correct_percentage": correct_percentage,
            "partially_percentage": partially_percentage,
            "incorrect_percentage": incorrect_percentage
        }
    
    return {
        "legibility": legibility_stats,
        "correctness": correctness_stats,
        "raw_legibility_scores": section_scores
    }

def print_summary(stats, file_name):
    """Print a summary of stats for a file."""
    print(f"\nSummary for {file_name}:")
    
    # Print legibility stats
    print("\nLegibility Scores:")
    for section, section_stats in stats["legibility"].items():
        if section_stats["avg_score"] is not None:
            print(f"{section}: Avg score {section_stats['avg_score']:.2f} (σ={section_stats['std_dev']:.2f}, max={section_stats['max_score']:.2f}) "
                  f"from {section_stats['count']} samples (N/A: {section_stats['na_count']})")
        else:
            print(f"{section}: No valid scores found (N/A: {section_stats['na_count']})")
    
    # Print correctness stats
    print("\nCorrectness Assessment:")
    for model, model_stats in stats["correctness"].items():
        total = model_stats["total"]
        if total > 0:
            print(f"{model.capitalize()}: "
                  f"Correct: {model_stats['correct']} ({model_stats['correct_percentage']:.1f}%), "
                  f"Partially: {model_stats['partially_correct']} ({model_stats['partially_percentage']:.1f}%), "
                  f"Incorrect: {model_stats['incorrect']} ({model_stats['incorrect_percentage']:.1f}%), "
                  f"N/A: {model_stats['N/A']}, "
                  f"Errors: {model_stats['error']}")
        else:
            print(f"{model.capitalize()}: No assessments found")

def compare_files(all_stats):
    """Compare stats across different files."""
    # Compare legibility scores
    for section in ["deepseek_response", "deepseek_reasoning", "cutoff_response", "cutoff_reasoning", "anthropic_response", 
                   "anthropic_reasoning", "openai_response", "openai_reasoning"]:
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

def create_plots_directory():
    """Create a directory for saving plots if it doesn't exist."""
    plots_dir = "plots/all"
    os.makedirs(plots_dir, exist_ok=True)
    return plots_dir

def plot_legibility_scores(stats, file_name, plots_dir, std_display="error_bars"):
    """
    Create and save bar charts for legibility scores with model names grouped under x-axis.
    Differentiates eval_types (answer vs reasoning) with different shading patterns.
    """
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
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = {'deepseek': '#3498db', 'cutoff': '#2ecc71', 
              'anthropic': '#9b59b6', 'openai': '#e74c3c'}
    
    # Extract info from section names
    bar_colors = []
    models = []
    hatches = []
    
    for section in sections:
        parts = section.split('_')
        model, eval_type = parts[0], parts[1]  # e.g., 'deepseek', 'response'
        
        bar_colors.append(colors.get(model, '#7f8c8d'))
        models.append(model)
        
        # Assign hatching pattern based on eval_type
        if eval_type == 'reasoning':
            hatches.append('///')  # Reduced density hatching (single slash instead of triple)
        else:
            hatches.append('')  # Solid for answers
    
    # Set the hatch linewidth for the entire figure
    plt.rcParams['hatch.linewidth'] = 0.3  # Thinner hatch lines
    
    # Plot bars with appropriate display style and hatching
    if std_display == "error_bars":
        bars = ax.bar(range(len(sections)), avg_scores, alpha=1, color=bar_colors)
        error_bars = ax.errorbar(range(len(sections)), avg_scores, yerr=std_devs, capsize=5, alpha=0.5, ecolor='black', linestyle='none')
        # Apply hatching after creating bars
        for bar, hatch in zip(bars, hatches):
            bar.set_hatch(hatch)
    
    elif std_display == "shaded":
        bars = ax.bar(range(len(sections)), avg_scores, alpha=1, color=bar_colors)
        # Apply hatching after creating bars
        for bar, hatch in zip(bars, hatches):
            bar.set_hatch(hatch)
                
        for i, (avg, std) in enumerate(zip(avg_scores, std_devs)):
            lower, upper = max(1, avg - std), min(9, avg + std)
            fill = ax.fill_between([i-0.4, i+0.391], [lower, lower], [upper, upper], 
                           color=bar_colors[i], alpha=0.3)
            
    elif std_display == "violin":
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
            bars = ax.bar(range(len(sections)), avg_scores, yerr=std_devs, alpha=0.8, color=bar_colors)
            # Apply hatching after creating bars
            for bar, hatch in zip(bars, hatches):
                bar.set_hatch(hatch)
    
    # Set up x-axis without labels (replaced by legend)
    ax.set_xticks(range(len(sections)))
    ax.set_xticklabels([''] * len(sections))  # Empty labels since we'll use the legend
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    
    # Group models below x-axis
    model_groups = {}
    for i, model in enumerate(models):
        if model not in model_groups:
            model_groups[model] = []
        model_groups[model].append(i)
    
    # Add model labels as group headers
    for model, positions in model_groups.items():
        mid_point = sum(positions) / len(positions)
        ax.annotate(model.capitalize(), xy=(mid_point, -0.03), xycoords=('data', 'axes fraction'),
                   ha='center', va='top', fontsize=11)
    
    # Create custom legend for eval_types with thinner hatching
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='gray', edgecolor='black', label='Answer'),
        Patch(facecolor='gray', hatch='///', edgecolor='black', alpha=0.75, label='Reasoning')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    # Customize plot
    ax.set_title(f'Illegibility In Various Settings (n={min(counts)})', fontsize=14)
    ax.set_ylabel('Illegibility Score', fontsize=12)
    ax.set_ylim(0, 9.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add extra space for model annotations
    plt.subplots_adjust(bottom=0.15)
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_legibility_scores_{std_display}.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Legibility scores plot saved to {plot_path}")

def plot_correctness_assessment(stats, file_name, plots_dir):
    """Create and save bar charts for correctness assessments."""
    # Create plot
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
    
    # Add labels and customize plot
    plt.xlabel('Models', fontsize=12)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.title(f'Correctness Assessment - {file_name}', fontsize=14)
    plt.xticks([r + bar_width for r in range(len(models))], [m.capitalize() for m in models])
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels and counts inside bars
    for i, bars in enumerate([bars1, bars2, bars3]):
        values = [correct_pct, partially_pct, incorrect_pct][i]
        counts_list = [correct_counts, partially_counts, incorrect_counts][i]
        
        for j, (bar, value, count) in enumerate(zip(bars, values, counts_list)):
            # Add percentage on top
            if value > 0:
                plt.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value:.1f}%', 
                        ha='center', va='bottom', fontsize=9)
                
                # Add count inside bar if bar is tall enough
                if value > 10:  # Only add if bar is tall enough
                    plt.text(bar.get_x() + bar.get_width()/2, value/2,
                            f'n={count}', ha='center', va='center', 
                            color='white', fontweight='bold', fontsize=8)
    
    # Add total count beneath model name
    for i, (model, count) in enumerate(zip(models, counts)):
        plt.text(r2[i], -5, f'total={count}', ha='center', va='top', fontsize=8)
    
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_correctness_assessment.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Correctness assessment plot saved to {plot_path}")

def plot_comparison_legibility(all_stats, section, plots_dir):
    """Create and save bar charts comparing legibility scores across files for a specific section."""
    plt.figure(figsize=(14, 7))
    
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
    
    # Get model name from section
    model = section.split('_')[0]
    component = section.split('_')[1]
    
    # Define color based on model
    colors = {'deepseek': '#3498db', 'cutoff': '#2ecc71', 
              'anthropic': '#9b59b6', 'openai': '#e74c3c'}
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
    """Create and save grouped bar charts comparing correctness assessments across files for a specific model."""
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
    
    # Add value labels and counts inside bars
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
                if value > 10:  # Only add if bar is tall enough
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
    """Create and save a plot showing overall model performance across all files."""
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
    plt.xticks(x, [m.capitalize() for m in models], fontsize=12)
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

def load_claude_score_file(file_path):
    """Load a Claude score JSON file and return the data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

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
        
        # Extract or use percentages directly
        correct_pct = section_percentages.get("correct_pct", 0)
        partially_pct = section_percentages.get("partially_pct", 0)
        incorrect_pct = section_percentages.get("incorrect_pct", 0)
        
        correctness_stats[section] = {
            "correct": section_summary.get("correct", 0),
            "partially_correct": section_summary.get("partially_correct", 0),
            "incorrect": section_summary.get("incorrect", 0),
            "N/A": section_summary.get("N/A", 0),
            "error": section_summary.get("error", 0),
            "total": total,
            "correct_percentage": correct_pct,
            "partially_percentage": partially_pct,
            "incorrect_percentage": incorrect_pct
        }
    
    return {
        "correctness": correctness_stats
    }

def print_claude_summary(stats, file_name):
    """Print a summary of Claude answer stats for a file."""
    print(f"\nSummary for {file_name}:")
    
    # Print correctness stats
    print("\nCorrectness Assessment:")
    for section, section_stats in stats["correctness"].items():
        total = section_stats["total"]
        if total > 0:
            print(f"{section}: "
                  f"Correct: {section_stats['correct']} ({section_stats['correct_percentage']:.1f}%), "
                  f"Partially: {section_stats['partially_correct']} ({section_stats['partially_percentage']:.1f}%), "
                  f"Incorrect: {section_stats['incorrect']} ({section_stats['incorrect_percentage']:.1f}%), "
                  f"N/A: {section_stats['N/A']}, "
                  f"Errors: {section_stats['error']}")
        else:
            print(f"{section}: No assessments found")

def plot_claude_correctness(stats, file_name, plots_dir):
    """Create and save bar charts for Claude correctness assessments."""
    # Create plot
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
    
    # Define bar width and positions
    bar_width = 0.25
    r1 = np.arange(len(sections))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    # Create bars
    bars1 = plt.bar(r1, correct_pct, width=bar_width, label='Correct', color='#2ecc71', alpha=0.8)
    bars2 = plt.bar(r2, partially_pct, width=bar_width, label='Partially Correct', color='#f39c12', alpha=0.8)
    bars3 = plt.bar(r3, incorrect_pct, width=bar_width, label='Incorrect', color='#e74c3c', alpha=0.8)
    
    # Add labels and customize plot
    plt.xlabel('Reasoning Sections', fontsize=12)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.title(f'Claude Answer Correctness Assessment - {file_name} n={total_counts[0]}', fontsize=14)
    plt.xticks([r + bar_width for r in range(len(sections))], [s.replace("_", " ").capitalize() for s in sections], rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels and counts inside bars
    for i, (bars, values, counts) in enumerate([
            (bars1, correct_pct, correct_counts),
            (bars2, partially_pct, partially_counts),
            (bars3, incorrect_pct, incorrect_counts)
        ]):
        for j, (bar, value, count) in enumerate(zip(bars, values, counts)):
            # Add percentage on top if value is significant
            if value > 0:
                plt.text(bar.get_x() + bar.get_width()/2, value + 2, f'{value:.1f}%', 
                        ha='center', va='bottom', fontsize=9)
                
                # Add count inside bar if bar is tall enough
                if value > 5:  # Only add if bar is tall enough
                    plt.text(bar.get_x() + bar.get_width()/2, value/2,
                            f'n={count}', ha='center', va='center', 
                            color='white', fontweight='bold', fontsize=8)
    
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(plots_dir, f"{file_name}_claude_correctness.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Claude correctness assessment plot saved to {plot_path}")

def plot_claude_comparisons(stats, file_name, plots_dir):
    """Create comparison plots for different types of reasoning sections."""
    plt.figure(figsize=(14, 8))
    
    # Group sections by model type (deepseek, cutoff, etc.)
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
        if correct_values[i] > 5:  # Only add text if there's enough space
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
        
        # Add section count below the x-axis
        section_count = len(model_sections[model])
        plt.text(i, -5, "", ha='center', va='top')
    
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

def process_claude_file(file_path, plots=False):
    """Process a single Claude answers score file and generate analysis."""
    try:
        print(f"Analyzing Claude answers file: {file_path}")
        file_name = os.path.basename(file_path).replace('.json', '')
        data = load_claude_score_file(file_path)
        stats = analyze_claude_scores(data)
        
        # Print summary for this file
        print_claude_summary(stats, file_name)
        
        # Generate plots if requested
        if plots:
            plots_dir = create_plots_directory()
            plot_claude_correctness(stats, file_name, plots_dir)
            plot_claude_comparisons(stats, file_name, plots_dir)
            
        return True
    except Exception as e:
        print(f"Error processing Claude answers file {file_path}: {e}")
        return False

def main():
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
    parser.add_argument('--analysis-type', type=str, choices=['regular', 'claude'], default=None,
                        help='Type of analysis to run (regular or claude)')
    parser.add_argument('--std-display', type=str, choices=['error_bars', 'shaded', 'violin'], default='shaded',
                        help='Type of standard deviation display (error_bars, shaded, violin)')
    
    args = parser.parse_args()
    
    analysis_type = args.analysis_type
    
    if analysis_type is None:
        if args.claude_file:
            analysis_type = 'claude'
        else:
            analysis_type = 'regular'
    
    if analysis_type == 'claude':
        if args.claude_file:
            claude_file_path = args.claude_file
            if os.path.exists(claude_file_path):
                process_claude_file(claude_file_path, plots=args.plots)
            else:
                print(f"Claude answers file not found: {claude_file_path}")
        else:
            print("Error: When using --analysis-type=claude, you must provide a --claude-file")
        return  # Exit after processing Claude file

    if analysis_type == 'regular':
        # Find all matching files
        file_pattern = os.path.join(args.dir, args.pattern)
        files = glob.glob(file_pattern)
        
        print(f"Found {len(files)} score files to analyze")
        
        all_stats = {}
        
        for file_path in files:
            try:
                print(f"Analyzing: {file_path}")
                file_name = os.path.basename(file_path).replace('_scores.json', '')
                data = load_score_file(file_path)
                stats = analyze_scores(data)
                all_stats[file_name] = stats
                
                # Print summary for this file
                print_summary(stats, file_name)
                
                # Generate plots if requested
                if args.plots:
                    plots_dir = create_plots_directory()
                    plot_legibility_scores(stats, file_name, plots_dir, std_display=args.std_display)
                    plot_correctness_assessment(stats, file_name, plots_dir)
                
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        # If comparison is requested, print comparison tables
        if args.compare and len(all_stats) > 1:
            compare_files(all_stats)
            
            # Generate comparison plots if requested
            if args.plots:
                plots_dir = create_plots_directory()
                
                # Plot legibility comparisons for each section
                for section in ["deepseek_response", "deepseek_reasoning", "cutoff_response", "cutoff_reasoning", 
                               "anthropic_response", "anthropic_reasoning", "openai_response", "openai_reasoning"]:
                    plot_comparison_legibility(all_stats, section, plots_dir)
                
                # Plot correctness comparisons for each model
                for model in ["deepseek", "cutoff", "anthropic", "openai"]:
                    plot_comparison_correctness(all_stats, model, plots_dir)
                
                # Plot overall model performance
                plot_overall_model_performance(all_stats, plots_dir)

if __name__ == "__main__":
    main()