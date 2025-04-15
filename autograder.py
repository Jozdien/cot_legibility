import os
import json
import argparse
import anthropic
from glob import glob
from datasets import load_from_disk

from utils import autograder_utils

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def process_file(file_path, dataset, client):
    """Process a single transcript file, extract answers, and grade them."""
    print(f"\nProcessing: {file_path}")
    
    question = autograder_utils.get_original_question_from_file(file_path)
    if question:
        actual_answer = autograder_utils.get_actual_answer(question, dataset)
    else:
        actual_answer = "No matching answer found"
    
    sections = autograder_utils.extract_sections(file_path)
    answers = {
        'deepseek': None,
        'cutoff': None,
        'anthropic': None,
        'openai': None,
    }
    
    if 'deepseek_response' in sections:
        answers['deepseek'] = autograder_utils.extract_answer_from_text(sections.get('deepseek_response', ''), is_reasoning=False)
    if not answers['deepseek'] and 'deepseek_reasoning' in sections:
        answers['deepseek'] = autograder_utils.extract_answer_from_text(sections.get('deepseek_reasoning', ''), is_reasoning=True)

    if 'cutoff_response' in sections:
        answers['cutoff'] = autograder_utils.extract_answer_from_text(sections.get('cutoff_response', ''), is_reasoning=False)
    if not answers['cutoff'] and 'cutoff_reasoning' in sections:
        answers['cutoff'] = autograder_utils.extract_answer_from_text(sections.get('cutoff_reasoning', ''), is_reasoning=True)
        
    if 'anthropic_response' in sections:
        answers['anthropic'] = autograder_utils.extract_answer_from_text(sections.get('anthropic_response', ''), is_reasoning=False)
    if not answers['anthropic'] and 'anthropic_reasoning' in sections:
        answers['anthropic'] = autograder_utils.extract_answer_from_text(sections.get('anthropic_reasoning', ''), is_reasoning=True)
        
    if 'openai_response' in sections:
        answers['openai'] = autograder_utils.extract_answer_from_text(sections.get('openai_response', ''), is_reasoning=False)
    if not answers['openai'] and 'openai_reasoning' in sections:
        answers['openai'] = autograder_utils.extract_answer_from_text(sections.get('openai_reasoning', ''), is_reasoning=True)
    
    legibility_grades = {}
    for section_name, text in sections.items():
        print(f"  Grading legibility of {section_name}...")
        if not text or text.strip() == "" or text.strip() == "None":
            legibility_grades[section_name] = {
                "score": "N/A", 
                "explanation": "No text content available in this section"
            }
            print(f"    Score: N/A - No text content available")
        else:
            legibility_grades[section_name] = autograder_utils.grade_legibility(text, client)
            print(f"    Score: {legibility_grades[section_name]['score']} - {legibility_grades[section_name]['explanation'][:50]}...")
    
    correctness_grades = {}
    for answer_type, answer_text in answers.items():
        print(f"  Grading correctness of {answer_type} answer...")
        if answer_text and answer_text != "No final answer found in reasoning":
            correctness_grades[answer_type] = autograder_utils.grade_answer_correctness(answer_text, actual_answer, client, file_path)
            print(f"    Correctness: {correctness_grades[answer_type]['correctness']} - {correctness_grades[answer_type]['explanation'][:50]}...")
        else:
            correctness_grades[answer_type] = {
                "correctness": "N/A", 
                "explanation": "No answer available to grade"
            }
            print(f"    Correctness: N/A - No answer available")
    
    results = {
        "file": os.path.basename(file_path),
        "question": question,
        "actual_answer": actual_answer,
        "answers": answers,
        "legibility": legibility_grades,
        "correctness": correctness_grades
    }
    
    return results

def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze and grade answers from markdown files.')
    parser.add_argument('--dir', type=str, default='r1_rollouts/cutoff_0.5_openrouter', 
                        help='Directory containing markdown files to analyze (default: r1_rollouts)')
    parser.add_argument('--scores-output', type=str, default=None,
                        help='Output JSON file path (defaults to dir_name_scores.json)')
    parser.add_argument('--answers-output', type=str, default=None,
                        help='Output markdown file path (defaults to dir_name_analysis.md)')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit number of files to process')
    parser.add_argument('--max-chars', type=int, default=5000,
                        help='Maximum characters to use from each text section for legibility grading')
    return parser.parse_args()
def main():
    args = parse_arguments()
    
    dir_name = os.path.basename(args.dir.rstrip('/'))
    
    # Ensure scores directory exists
    os.makedirs("scores", exist_ok=True)
    if args.scores_output is None:
        args.scores_output = f"{dir_name}_scores.json"
        scores_output_path = os.path.join("scores", args.scores_output)
    else:
        scores_output_path = args.scores_output

    # Ensure correctness directory exists
    os.makedirs("answers", exist_ok=True)
    if args.answers_output is None:
        args.answers_output = f"{dir_name}_answers.md"
        answers_output_path = os.path.join("answers", args.answers_output)
    else:
        answers_output_path = args.answers_output
    
    dataset_path = "data/gpqa_diamond"
    gpqa_dataset = load_from_disk(dataset_path)
    
    rollout_files = glob(f'{args.dir}/**/*.md', recursive=True)
    if args.limit:
        rollout_files = rollout_files[:args.limit]
    print(f"Found {len(rollout_files)} markdown files to analyze in {args.dir}")
    
    all_results = []
    with open(answers_output_path, 'w', encoding='utf-8') as answers_file:
        for file_path in rollout_files:
            try:
                result = process_file(file_path, gpqa_dataset, client)
                all_results.append(result)
                
                answers_file.write(f"## Question from {os.path.basename(file_path)}\n\n")
                answers_file.write(f"**Original Question:**\n{result['question']}\n\n")
                answers_file.write(f"**DeepSeek Original Answer:**\n{result['answers']['deepseek']}\n\n")
                answers_file.write(f"**Cutoff Continuation Answer:**\n{result['answers']['cutoff']}\n\n")
                answers_file.write(f"**Anthropic Continuation Answer:**\n{result['answers']['anthropic']}\n\n")
                answers_file.write(f"**OpenAI Continuation Answer:**\n{result['answers']['openai']}\n\n")
                answers_file.write(f"**Actual Answer:**\n{result['actual_answer']}\n\n")
                
                answers_file.write("**Correctness Assessment:**\n")
                for model, grade in result['correctness'].items():
                    answers_file.write(f"- {model.capitalize()}: {grade['correctness']} - {grade['explanation']}\n")

                answers_file.write("\n---\n\n")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    with open(scores_output_path, 'w', encoding='utf-8') as scores_file:
        json.dump(all_results, scores_file, indent=2)
    
    print(f"Analysis complete. Results written to {answers_output_path} and {scores_output_path}")

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
    correctness_counts = {
        "deepseek": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
        "cutoff": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
        "anthropic": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
        "openai": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
    }
    
    for result in all_results:
        for section, grade in result['legibility'].items():
            if section in section_scores:
                if grade["score"] != "N/A" and isinstance(grade["score"], (int, float)):
                    section_scores[section].append(grade["score"])
        for model, grade in result['correctness'].items():
            correctness = grade.get('correctness', 'N/A')
            if correctness in correctness_counts[model]:
                correctness_counts[model][correctness] += 1
    
    print("\nSummary:")
    
    print("\nLegibility Scores:")
    for section, scores in section_scores.items():
        if scores:
            avg_score = sum(scores) / len(scores)
            print(f"{section}: Avg score {avg_score:.2f} from {len(scores)} samples")
        else:
            print(f"{section}: No valid scores found")
    
    print("\nCorrectness Assessment:")
    for model, counts in correctness_counts.items():
        total = sum(counts.values())
        print(f"{model.capitalize()}: Correct: {counts['correct']}, Partially: {counts['partially_correct']}, " +
              f"Incorrect: {counts['incorrect']}, N/A: {counts['N/A']}, Errors: {counts['error']}")

if __name__ == "__main__":
    main()