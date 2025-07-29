import argparse
import concurrent.futures
import json
import os
import re
from glob import glob

import anthropic
from datasets import load_from_disk

from utils import autograder_utils_multi as autograder_utils

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def extract_custom_sections(file_path, model_display_name):
    """Extract sections for a custom model from a transcript file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    sections = {}
    
    # Pattern for response section
    response_pattern = rf"# {model_display_name} response \(via .*?\)\n\n([\s\S]*?)(?=\n---\n|\n# |$)"
    response_match = re.search(response_pattern, content, re.DOTALL)
    if response_match:
        sections[f"{model_display_name}_response"] = response_match.group(1).strip()
    
    # Pattern for reasoning section (if exists)
    reasoning_pattern = rf"# {model_display_name} reasoning \(via .*?\)\n\n([\s\S]*?)(?=\n---\n|\n# |$)"
    reasoning_match = re.search(reasoning_pattern, content, re.DOTALL)
    if reasoning_match:
        sections[f"{model_display_name}_reasoning"] = reasoning_match.group(1).strip()
    
    return sections


def detect_dataset_from_directory(dir_path):
    """Detect dataset type from directory name."""
    dir_name = os.path.basename(os.path.normpath(dir_path))
    if "mmlu_pro" in dir_name:
        return "mmlu_pro"
    return "gpqa"


def process_file(file_path, dataset, client, model_display_name, dataset_type):
    """Process a single transcript file, extract answers, and grade them."""
    print(f"\nProcessing: {file_path}")

    question = autograder_utils.get_original_question_from_file(file_path)
    if question:
        actual_answer = autograder_utils.get_actual_answer(question, dataset)
    else:
        actual_answer = "No matching answer found"

    sections = extract_custom_sections(file_path, model_display_name)
    answers = {
        model_display_name: None,
    }

    # Extract answer from response or reasoning
    if f"{model_display_name}_response" in sections:
        answers[model_display_name] = autograder_utils.extract_answer_from_text(
            sections.get(f"{model_display_name}_response", ""), 
            is_reasoning=False,
            dataset_type=dataset_type
        )
    if not answers[model_display_name] and f"{model_display_name}_reasoning" in sections:
        answers[model_display_name] = autograder_utils.extract_answer_from_text(
            sections.get(f"{model_display_name}_reasoning", ""), 
            is_reasoning=True,
            dataset_type=dataset_type
        )

    # Grade legibility
    legibility_grades = {}
    for section_name, text in sections.items():
        print(f"  Grading legibility of {section_name}...")
        if not text or text.strip() == "" or text.strip() == "None":
            legibility_grades[section_name] = {
                "score": "N/A",
                "explanation": "No text content available in this section",
            }
            print("    Score: N/A - No text content available")
        else:
            legibility_grades[section_name] = autograder_utils.grade_legibility(
                text, client
            )
            print(
                f"    Score: {legibility_grades[section_name]['score']} - {legibility_grades[section_name]['explanation'][:50]}..."
            )

    # Grade correctness
    correctness_grades = {}
    for answer_type, answer_text in answers.items():
        print(f"  Grading correctness of {answer_type} answer...")
        if answer_text and answer_text != "No final answer found in reasoning":
            correctness_grades[answer_type] = autograder_utils.grade_answer_correctness(
                answer_text, actual_answer, client, file_path, dataset_type
            )
            print(
                f"    Correctness: {correctness_grades[answer_type]['correctness']} - {correctness_grades[answer_type]['explanation'][:50]}..."
            )
        else:
            correctness_grades[answer_type] = {
                "correctness": "N/A",
                "explanation": "No answer extracted",
            }
            print("    Correctness: N/A - No answer extracted")

    return {
        "file": os.path.basename(file_path),
        "question": question,
        "answers": answers,
        "actual_answer": actual_answer,
        "legibility": legibility_grades,
        "correctness": correctness_grades,
        "dataset_type": dataset_type
    }


def save_result_to_answers_file(result, answers_file, model_display_name):
    """Save individual result to answers file."""
    answers_file.write(f"### {result['file']}\n\n")
    answers_file.write(f"**Question:** {result['question'][:200]}...\n\n" if len(result['question']) > 200 else f"**Question:** {result['question']}\n\n")
    answers_file.write(
        f"**{model_display_name} Answer:** {result['answers'][model_display_name]}\n\n"
    )
    answers_file.write(f"**Actual Answer:** {result['actual_answer']}\n\n")

    answers_file.write("**Correctness Assessment:**\n")
    for model, grade in result["correctness"].items():
        answers_file.write(
            f"- {model}: {grade['correctness']} - {grade['explanation']}\n"
        )

    answers_file.write("\n---\n\n")
    answers_file.flush()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze and grade answers from custom model markdown files."
    )
    parser.add_argument(
        "--dir",
        type=str,
        required=True,
        help="Directory containing markdown files to analyze",
    )
    parser.add_argument(
        "--model-display-name",
        type=str,
        required=True,
        help="Display name of the model (as used in the markdown files)",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        choices=["gpqa", "mmlu_pro", "auto"],
        default="auto",
        help="Dataset type (auto-detect from directory name by default)",
    )
    parser.add_argument(
        "--scores-output",
        type=str,
        default=None,
        help="Output JSON file path (defaults to scores/dir_name_scores.json)",
    )
    parser.add_argument(
        "--answers-output",
        type=str,
        default=None,
        help="Output markdown file path (defaults to answers/dir_name_answers.md)",
    )
    parser.add_argument(
        "--limit", type=int, default=None, help="Limit number of files to process"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=5,
        help="Number of parallel workers",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Auto-detect dataset type from directory name if needed
    if args.dataset == "auto":
        dataset_type = detect_dataset_from_directory(args.dir)
        print(f"Auto-detected dataset type: {dataset_type}")
    else:
        dataset_type = args.dataset

    # Set default output paths based on directory name
    dir_name = os.path.basename(os.path.normpath(args.dir))
    if args.scores_output is None:
        args.scores_output = f"scores/{dir_name}_scores.json"
    if args.answers_output is None:
        args.answers_output = f"answers/{dir_name}_answers.md"

    # Ensure output directories exist
    os.makedirs(os.path.dirname(args.scores_output), exist_ok=True)
    os.makedirs(os.path.dirname(args.answers_output), exist_ok=True)

    # Load appropriate dataset
    if dataset_type == "mmlu_pro":
        dataset = load_from_disk("data/mmlu_pro")
    else:
        dataset = load_from_disk("data/gpqa_diamond")

    # Get markdown files
    md_files = glob(os.path.join(args.dir, "*.md"))
    if args.limit:
        md_files = md_files[: args.limit]

    print(f"Found {len(md_files)} markdown files to process")
    print(f"Using dataset: {dataset_type}")

    # Process files in parallel
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_file = {
            executor.submit(process_file, file, dataset, client, args.model_display_name, dataset_type): file
            for file in md_files
        }

        with open(args.answers_output, "w") as answers_file:
            answers_file.write(f"# {args.model_display_name} Model Analysis - {dataset_type.upper()}\n\n")
            answers_file.write(f"Analyzed {len(md_files)} responses\n")
            answers_file.write(f"Dataset: {dataset_type}\n\n---\n\n")

            for future in concurrent.futures.as_completed(future_to_file):
                try:
                    result = future.result()
                    results.append(result)
                    save_result_to_answers_file(result, answers_file, args.model_display_name)
                except Exception as e:
                    file = future_to_file[future]
                    print(f"Error processing {file}: {str(e)}")

    # Save results to JSON
    with open(args.scores_output, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nProcessing complete!")
    print(f"Scores saved to: {args.scores_output}")
    print(f"Answers saved to: {args.answers_output}")

    # Print summary statistics
    total_files = len(results)
    correct_count = sum(
        1
        for r in results
        if r["correctness"].get(args.model_display_name, {}).get("correctness") == "correct"
    )
    partially_correct_count = sum(
        1
        for r in results
        if r["correctness"].get(args.model_display_name, {}).get("correctness") == "partially_correct"
    )

    print(f"\nSummary:")
    print(f"Total questions: {total_files}")
    print(f"Correct: {correct_count} ({correct_count/total_files*100:.1f}%)")
    if dataset_type == "gpqa":  # MMLU-Pro doesn't have partial credit
        print(
            f"Partially correct: {partially_correct_count} ({partially_correct_count/total_files*100:.1f}%)"
        )
    print(
        f"Incorrect: {total_files - correct_count - partially_correct_count} ({(total_files - correct_count - partially_correct_count)/total_files*100:.1f}%)"
    )


if __name__ == "__main__":
    main()