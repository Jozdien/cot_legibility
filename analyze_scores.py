import os
import json
import glob
import argparse
import numpy as np

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
        "correctness": correctness_stats
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

def main():
    parser = argparse.ArgumentParser(description='Analyze legibility and correctness scores from JSON files')
    parser.add_argument('--dir', type=str, default='scores',
                        help='Directory containing score JSON files')
    parser.add_argument('--pattern', type=str, default='*_scores.json',
                        help='File pattern to match')
    parser.add_argument('--compare', action='store_true',
                        help='Compare stats across different files')
    
    args = parser.parse_args()
    
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
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # If comparison is requested, print comparison tables
    if args.compare and len(all_stats) > 1:
        compare_files(all_stats)

if __name__ == "__main__":
    main()