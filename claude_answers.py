import os
import re
import json
import time
import anthropic
import argparse
from datetime import datetime
from dotenv import load_dotenv
from datasets import load_from_disk

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
)

load_dotenv()

# Define the different reasoning trace sections we want to test
SECTIONS_TO_ANALYZE = [
    "# DeepSeek reasoning",
    "# Cut off deepseek reasoning",
    "# Anthropic completion",
    "# OpenAI completion",
    "# cutoff_deepseek_completion reasoning",
    "# paraphrased_deepseek_completion_anthropic reasoning",
    "# paraphrased_deepseek_completion_openai reasoning"
]

###################
# ANSWER GENERATION FUNCTIONS
###################

def extract_section(content, section_marker):
    """Extract a specific section from the content based on section marker."""
    pattern = f"{re.escape(section_marker)}.*?\\n\\n(.*?)(?=\\n\\n(?:---|#)|$)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_original_question(content):
    """Extract the original question from the content."""
    return extract_section(content, "# Original Question")

def analyze_reasoning_with_claude(question, reasoning):
    """
    Send the question and reasoning to Claude and ask it to answer the question
    using the provided reasoning trace as context.
    """
    prompt = f"""Please answer the following question:
{question}

Here's some prior reasoning related to the question that might help:
{reasoning}
"""

    # Add exponential backoff for rate limiting
    max_retries = 5
    base_delay = 2
    
    for attempt in range(max_retries):
        try:
            response = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1000,
                temperature=0,
                # system="You are a helpful AI assistant analyzing reasoning traces to determine if they lead to a conclusive answer.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            if attempt < max_retries - 1:
                sleep_time = base_delay ** attempt
                print(f"Rate limited or error. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                return f"Error after {max_retries} attempts: {str(e)}"
            
def create_markdown_summary(results, output_file):
    """Create a markdown summary of the generated answers."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Claude 3.7 Reasoning Analysis Summary\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for file_path, result in results.items():
            file_name = os.path.basename(file_path)
            f.write(f"## {file_name}\n\n")
            f.write(f"**Original Question:**\n{result['original_question']}\n\n")
            
            for section_name, answer in result['answers'].items():
                f.write(f"### {section_name}\n\n")
                f.write(f"{answer}\n\n")
            
            f.write("---\n\n")

###################
# GRADING FUNCTIONS
###################

def get_actual_answer(question, dataset):
    """Find the actual answer in the GPQA dataset based on the question."""
    if not question:
        return "No question provided"
    
    # Remove trailing period if present for matching
    question = question.strip().rstrip('.')
    
    # Search through the dataset for matching questions
    for item in dataset:
        if item['Question'].strip().rstrip('.') == question:
            return item.get('Correct Answer', item.get('Answer', "No answer found in dataset"))
    
    return "No matching answer found"

def grade_claude_answer(claude_answer, actual_answer, question):
    """
    Use Claude 3.7 to grade if Claude's answer is correct compared to the reference answer.
    Returns a dict with correctness assessment and explanation.
    """
    if not claude_answer or claude_answer == "Section not found in file":
        return {"correctness": "N/A", "explanation": "No Claude answer available"}
    
    if not actual_answer or actual_answer == "No matching answer found":
        return {"correctness": "N/A", "explanation": "No reference answer available"}
    
    grading_instructions = """
    Compare the given answer with the actual answer and determine if the answer is:
    - "correct": The answer correctly addresses the question and aligns with the actual answer
    - "partially_correct": The answer has some correct elements but also contains errors or misunderstandings
    - "incorrect": The answer is wrong or completely misaligns with the actual answer
    
    Consider that answers might be worded differently but still convey the same meaning.
    
    FORMAT YOUR RESPONSE AS JSON:
    {
        "correctness": "correct|partially_correct|incorrect",
        "explanation": "<brief explanation for your assessment>"
    }
    """
    
    prompt = f"""
{grading_instructions}

QUESTION: {question}

CLAUDE ANSWER: {claude_answer}

ACTUAL ANSWER: {actual_answer}
"""
    
    # Add exponential backoff for rate limiting
    max_retries = 5
    base_delay = 2
    
    for attempt in range(max_retries):
        try:
            response = anthropic_client.messages.create(
                model="claude-3-7-sonnet-latest",
                max_tokens=1000,
                temperature=0,
                system="You are a helpful assistant that grades answer correctness. Always respond with valid JSON.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract JSON from the response
            response_text = response.content[0].text
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                json_str = response_text.split("```")[1].strip()
            else:
                json_str = response_text.strip()
                
            return json.loads(json_str)
        except Exception as e:
            if attempt < max_retries - 1:
                sleep_time = base_delay ** attempt
                print(f"Rate limited or error. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                return {"correctness": "error", "explanation": f"Error grading answer: {str(e)}"}

def compare_claude_answers_with_actual(results_file, dataset_path="data/gpqa_diamond"):
    """
    Compare Claude's generated answers with actual answers from the GPQA dataset and grade them.
    
    Args:
        results_file: Path to the JSON file produced by the generation step
        dataset_path: Path to the GPQA dataset
    
    Returns:
        Path to the output comparison file
    """
    # Load results file
    with open(results_file, 'r', encoding='utf-8') as f:
        all_results = json.load(f)
    
    # Load the GPQA dataset
    print(f"Loading dataset from {dataset_path}")
    gpqa_dataset = load_from_disk(dataset_path)
    
    # Ensure scores directory exists
    os.makedirs("claude_answers/scores", exist_ok=True)
    
    # Process each result
    comparison_results = {}
    
    for file_path, result in all_results.items():
        question = result.get('original_question')
        if not question:
            continue
            
        # Get actual answer
        actual_answer = get_actual_answer(question, gpqa_dataset)
        
        # Initialize results for this file
        comparison_results[file_path] = {
            "question": question,
            "actual_answer": actual_answer,
            "grades": {}
        }
        
        # Grade each section's answer
        for section_name, section_data in result.get('answers', {}).items():
            print(f"Grading {file_path} - {section_name}...")
            claude_answer = section_data.get('answer')
            if claude_answer:
                grade = grade_claude_answer(claude_answer, actual_answer, question)
                comparison_results[file_path]["grades"][section_name] = grade
    
    # Generate summary statistics
    section_grades = {section.replace("# ", "").strip(): {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0} 
                     for section in SECTIONS_TO_ANALYZE}
    
    for file_result in comparison_results.values():
        for section, grade in file_result.get("grades", {}).items():
            correctness = grade.get("correctness", "N/A")
            if section in section_grades and correctness in section_grades[section]:
                section_grades[section][correctness] += 1
    
    # Calculate percentages for valid judgments
    section_percentages = {}
    for section, counts in section_grades.items():
        total_valid = counts["correct"] + counts["partially_correct"] + counts["incorrect"]
        if total_valid > 0:
            section_percentages[section] = {
                "correct_pct": (counts["correct"] / total_valid) * 100,
                "partially_pct": (counts["partially_correct"] / total_valid) * 100,
                "incorrect_pct": (counts["incorrect"] / total_valid) * 100,
                "total_valid": total_valid,
                "total_NA": counts["N/A"],
                "total_error": counts["error"]
            }
        else:
            section_percentages[section] = {
                "correct_pct": 0,
                "partially_pct": 0, 
                "incorrect_pct": 0,
                "total_valid": 0,
                "total_NA": counts["N/A"],
                "total_error": counts["error"]
            }
    
    # Save results to file
    results_filename = os.path.basename(results_file)
    comparison_file = f"claude_answers/scores/claude37_comparison_{results_filename}"
    with open(comparison_file, 'w', encoding='utf-8') as f:
        json.dump({
            "detailed_results": comparison_results,
            "summary": section_grades,
            "percentages": section_percentages
        }, f, indent=2)
    
    print(f"Comparison complete. Results saved to {comparison_file}")
    return comparison_file

def process_rollout_file(file_path):
    """Process a single rollout file and generate answers from each reasoning section."""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_question = extract_original_question(content)
    if not original_question:
        print(f"Original question not found in {file_path}")
        return None
    
    results = {
        "file_path": file_path,
        "original_question": original_question,
        "answers": {}
    }
    
    for section in SECTIONS_TO_ANALYZE:
        section_name = section.replace("# ", "").strip()
        reasoning = extract_section(content, section)

        if reasoning and "**Final Answer**" in reasoning:
            reasoning = reasoning.split("**Final Answer**")[0]
        
        if reasoning:
            print(f"  Generating answer from {section_name} reasoning...")
            answer = analyze_reasoning_with_claude(original_question, reasoning)
            # Store both the reasoning trace and the answer
            results["answers"][section_name] = {
                "reasoning_trace": reasoning,
                "answer": answer
            }
        else:
            print(f"  Section {section_name} not found")
            results["answers"][section_name] = {
                "reasoning_trace": None,
                "answer": "Section not found in file"
            }
    
    return results

def process_directory(directory_path, limit=None):
    """
    Process rollout files in a directory and generate answers from reasoning traces.
    
    Args:
        directory_path: Path to directory containing rollout files
        limit: Maximum number of files to process (None for no limit)
        
    Returns:
        Tuple of (output_file_path, results_dict)
    """
    all_results = {}
    
    # Get the name of the directory for the output file
    dir_name = os.path.basename(directory_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"claude_answers/{dir_name}_{timestamp}.json"
    
    # Ensure directory exists
    os.makedirs("claude_answers", exist_ok=True)
    
    # Walk through all subdirectories
    files_processed = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Process the file
                results = process_rollout_file(file_path)
                if results:
                    all_results[file_path] = results
                
                # Save results incrementally to avoid losing progress
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(all_results, f, indent=2)
                
                files_processed += 1
                # Check if we've reached the limit
                if limit is not None and files_processed >= limit:
                    print(f"Reached limit of {limit} files. Stopping.")
                    break
        
        # Also check the limit after processing files in a directory
        if limit is not None and files_processed >= limit:
            break
                    
    print(f"Analysis complete. Results saved to {output_file}")
    
    return output_file, all_results

def main():
    """Main function to run the answer generation and grading pipeline."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate answers to questions using (partial) reasoning traces with Claude and grade the results')
    parser.add_argument('--mode', type=str, choices=['generate', 'grade', 'both'], default='both',
                        help='Mode to run: generate answers from reasoning, grade answers, or both (default: both)')
    parser.add_argument('--dir', type=str, default='r1_rollouts/cutoff_0.25_deepseek_openrouter',
                        help='Directory containing rollout files with reasoning traces (only used when generating answers)')
    parser.add_argument('--limit', type=int, default=None,
                        help='Maximum number of files to process (only used when generating answers)')
    parser.add_argument('--results', type=str, default=None,
                        help='Path to results JSON file from generation step (required for grade mode if not running both)')
    parser.add_argument('--dataset', type=str, default="data/gpqa_diamond",
                        help='Path to GPQA dataset (only used when grading answers)')
    args = parser.parse_args()
    
    results_file = None
    
    # Run in the specified mode
    if args.mode in ['generate', 'both']:
        # Check if the directory exists
        if not os.path.exists(args.dir):
            print(f"Directory {args.dir} not found")
            return
        
        print(f"Processing directory: {args.dir}")
        results_file, _ = process_directory(args.dir, args.limit)
    
    if args.mode in ['grade', 'both']:
        # If we're only grading and not generating, we need a results file
        if args.mode == 'grade':
            if args.results:
                results_file = args.results
            else:
                print("Error: When using --mode=grade, you must provide a --results file path")
                return
        
        # Check if the results file exists
        if not os.path.exists(results_file):
            print(f"Results file {results_file} not found")
            return
        
        print(f"Grading results from: {results_file}")
        compare_claude_answers_with_actual(results_file, args.dataset)

if __name__ == "__main__":
    main()