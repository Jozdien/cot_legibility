import os
import json
import argparse
import anthropic
from tqdm.auto import tqdm
import concurrent.futures
from glob import glob
from datasets import load_from_disk

from utils import autograder_utils

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Grade legibility and correctness of answers from Claude rollouts.')
    parser.add_argument('--file', type=str, default='claude_answers/claude_baseline_answers.json', 
                        help='JSON file containing Claude rollout answers (default: claude_answers/claude_baseline_answers.json)')
    parser.add_argument('--output-file', type=str, default='scores/claude_baseline_scores.json',
                        help='Output JSON file path (defaults to dir_name_scores.json)')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit number of files to process')
    parser.add_argument('--max-chars', type=int, default=5000,
                        help='Maximum characters to use from each text section for legibility grading')
    parser.add_argument('--workers', type=int, default=5,
                        help='Number of concurrent workers for processing files (default: 5)')
    return parser.parse_args()

def process_item(file, item, dataset, client):
    question = item['question']
    answer = item['answer']
    reasoning = item['reasoning']

    actual_answer = autograder_utils.get_actual_answer(question, dataset)

    legibility_grades = {}
    print(f"Grading legibility of {question} answer...")
    legibility_grades['claude_response'] = autograder_utils.grade_legibility(answer, client)
    legibility_grades['claude_reasoning'] = autograder_utils.grade_legibility(reasoning, client)

    correctness_grade = {}
    print(f"Grading correctness of {question} answer...")
    correctness_grade['claude'] = autograder_utils.grade_answer_correctness_new(answer, actual_answer, client, question)

    result = {
        "file": file,
        "question": question,
        "actual_answer": actual_answer,
        "answers": {
            "claude": answer,
        },
        "legibility": legibility_grades,
        "correctness": correctness_grade
    }
    return result

def main():
    args = parse_arguments()
    
    dataset_path = "data/gpqa_diamond"
    gpqa_dataset = load_from_disk(dataset_path)
    
    all_results = []
    processed_count = 0
    failed_count = 0

    with open(args.file, 'r', encoding='utf-8') as f:
        items = json.load(f)
    items = dict(list(items.items())[:args.limit]) if args.limit else items
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_file = {
            executor.submit(process_item, args.file, items[item_idx], gpqa_dataset, client): item_idx 
            for item_idx in items
        }
        
        with tqdm(total=len(items), desc="Processing items") as pbar:
            for future in concurrent.futures.as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    result = future.result()
                    all_results.append(result)
                    processed_count += 1
                    
                    print(f"Progress: {processed_count + failed_count}/{len(items)} "
                        f"({processed_count} successful, {failed_count} failed)")
                    
                except Exception as e:
                    failed_count += 1
                    print(f"Error processing {file_path}: {e}")
                    print(f"Progress: {processed_count + failed_count}/{len(items)} "
                        f"({processed_count} successful, {failed_count} failed)")
    
    # Write JSON results
    with open(args.output_file, 'w', encoding='utf-8') as scores_file:
        json.dump(all_results, scores_file, indent=2)
    
    print(f"Analysis complete. Results written to {args.output_file}")
    print(f"Successfully processed: {processed_count}")
    print(f"Failed: {failed_count}")

    section_scores = {
        "claude_response": [],
        "claude_reasoning": [],
    }
    
    for result in all_results:
        for section, grade in result['legibility'].items():
            if section in section_scores:
                if grade["score"] != "N/A" and isinstance(grade["score"], (int, float)):
                    section_scores[section].append(grade["score"])
    
    print("\nSummary:")
    
    print("\nLegibility Scores:")
    for section, scores in section_scores.items():
        if scores:
            avg_score = sum(scores) / len(scores)
            print(f"{section}: Avg score {avg_score:.2f} from {len(scores)} samples")
        else:
            print(f"{section}: No valid scores found")

if __name__ == "__main__":
    main()