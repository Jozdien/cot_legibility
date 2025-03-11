import os
import json
import glob
import argparse

def load_score_file(file_path):
    """Load a score JSON file and return the data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_scores(data):
    """Analyze scores from a single JSON file."""
    section_scores = {
        "cutoff_response": [], 
        "cutoff_reasoning": [],
        "anthropic_response": [], 
        "anthropic_reasoning": [],
        "openai_response": [], 
        "openai_reasoning": []
    }
    
    section_na_counts = {section: 0 for section in section_scores}
    
    for result in data:
        for section, score_data in result.get("sections", {}).items():
            if section in section_scores:
                if score_data.get("score") == "N/A":
                    section_na_counts[section] += 1
                elif isinstance(score_data.get("score"), (int, float)):
                    section_scores[section].append(score_data["score"])
    
    # Calculate statistics
    stats = {}
    for section, scores in section_scores.items():
        na_count = section_na_counts[section]
        total = len(scores) + na_count
        
        if scores:
            stats[section] = {
                "avg_score": sum(scores) / len(scores),
                "count": len(scores),
                "na_count": na_count,
                "total": total
            }
        else:
            stats[section] = {
                "avg_score": None,
                "count": 0,
                "na_count": na_count,
                "total": total
            }
    
    return stats

def print_summary(stats, file_name):
    """Print a summary of stats for a file."""
    print(f"\nSummary for {file_name}:")
    for section, section_stats in stats.items():
        if section_stats["avg_score"] is not None:
            print(f"{section}: Avg score {section_stats['avg_score']:.2f} from {section_stats['count']} samples (N/A: {section_stats['na_count']})")
        else:
            print(f"{section}: No valid scores found (N/A: {section_stats['na_count']})")

def compare_files(all_stats):
    """Compare stats across different files."""
    # Create a comparison table for each section
    for section in ["cutoff_response", "cutoff_reasoning", "anthropic_response", 
                   "anthropic_reasoning", "openai_response", "openai_reasoning"]:
        print(f"\n--- {section} comparison ---")
        print(f"{'File':<40} {'Avg Score':<10} {'Count':<10} {'N/A':<10}")
        print("-" * 70)
        
        for file_name, stats in all_stats.items():
            section_stats = stats.get(section, {})
            avg_score = section_stats.get("avg_score")
            count = section_stats.get("count", 0)
            na_count = section_stats.get("na_count", 0)
            
            avg_display = f"{avg_score:.2f}" if avg_score is not None else "N/A"
            print(f"{file_name:<40} {avg_display:<10} {count:<10} {na_count:<10}")

def main():
    parser = argparse.ArgumentParser(description='Analyze legibility scores from JSON files')
    parser.add_argument('--dir', type=str, default='../scores',
                        help='Directory containing score JSON files')
    parser.add_argument('--pattern', type=str, default='*_legibility_scores.json',
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
            file_name = os.path.basename(file_path).replace('_legibility_scores.json', '')
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
