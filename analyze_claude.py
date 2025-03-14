import os
import re
import json
import time
import anthropic
import argparse
from datetime import datetime
from dotenv import load_dotenv
from datasets import load_from_disk

# Load environment variables
load_dotenv()

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
)

def get_actual_answer(question, dataset):
    """Find the actual answer in the dataset based on the question."""
    if not question:
        return "No question provided"
    
    # Remove trailing period if present for matching
    question = question.strip().rstrip('.')
    
    # Search through the dataset for matching questions
    for item in dataset:
        if item['Question'].strip().rstrip('.') == question:
            return item.get('Answer', "No answer found in dataset")
    
    return "No matching answer found"

def grade_claude_answer(claude_answer, actual_answer, question):
    """Use Claude 3.7 to grade if the answer is correct."""
    if not claude_answer or claude_answer == "Section not found in file":
        return {"correctness": "N/A", "explanation": "No Claude answer available"}
    
    if not actual_answer or actual_answer == "No matching answer found":
        return {"correctness": "N/A", "explanation": "No reference answer available"}
    
    grading_instructions = """
    Compare the Claude answer with the actual answer and determine if Claude's answer is:
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
    Compare Claude's answers with actual answers from the dataset.
    
    Args:
        results_file: Path to the JSON file produced by analyze_oversight.py
        dataset_path: Path to the GPQA dataset
    
    Returns:
        A dictionary with comparison results
    """
    # Load results file
    with open(results_file, 'r', encoding='utf-8') as f:
        all_results = json.load(f)
    
    # Load the GPQA dataset
    print(f"Loading dataset from {dataset_path}")
    gpqa_dataset = load_from_disk(dataset_path)
    
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
    section_grades = {section: {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0} 
                     for section in ["DeepSeek reasoning", "Cut off deepseek reasoning", 
                                     "cutoff_deepseek_completion reasoning", "Anthropic completion", 
                                     "OpenAI completion", "paraphrased_deepseek_completion_anthropic reasoning",
                                     "paraphrased_deepseek_completion_openai reasoning"]}
    
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
    comparison_file = f"claude37_comparison_{results_filename}"
    with open(comparison_file, 'w', encoding='utf-8') as f:
        json.dump({
            "detailed_results": comparison_results,
            "summary": section_grades,
            "percentages": section_percentages
        }, f, indent=2)
    
    # Create a markdown summary
    markdown_file = comparison_file.replace('.json', '.md')
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write("# Claude 3.7 Answer Comparison Summary\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Write summary table
        f.write("## Summary Statistics\n\n")
        f.write("| Section | Correct | Partially Correct | Incorrect | N/A | Errors |\n")
        f.write("|---------|---------|-------------------|-----------|-----|--------|\n")
        
        for section, counts in section_grades.items():
            total_valid = counts["correct"] + counts["partially_correct"] + counts["incorrect"]
            if total_valid > 0:
                correct_pct = (counts["correct"] / total_valid) * 100
                partially_pct = (counts["partially_correct"] / total_valid) * 100
                incorrect_pct = (counts["incorrect"] / total_valid) * 100
                
                f.write(f"| {section} | {counts['correct']} ({correct_pct:.1f}%) | {counts['partially_correct']} ({partially_pct:.1f}%) | {counts['incorrect']} ({incorrect_pct:.1f}%) | {counts['N/A']} | {counts['error']} |\n")
            else:
                f.write(f"| {section} | 0 (0%) | 0 (0%) | 0 (0%) | {counts['N/A']} | {counts['error']} |\n")
        
        # Write detailed results for each question
        f.write("\n## Detailed Results\n\n")
        for file_path, file_result in comparison_results.items():
            file_name = os.path.basename(file_path)
            f.write(f"### {file_name}\n\n")
            f.write(f"**Question:** {file_result['question']}\n\n")
            f.write(f"**Actual Answer:** {file_result['actual_answer']}\n\n")
            
            f.write("**Grades by Section:**\n\n")
            for section, grade in file_result.get("grades", {}).items():
                f.write(f"- **{section}**: {grade.get('correctness', 'N/A')} - {grade.get('explanation', '')}\n")
            
            f.write("\n---\n\n")
    
    print(f"Comparison complete. Results saved to {comparison_file} and {markdown_file}")
    return comparison_results

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Compare Claude answers with actual answers')
    parser.add_argument('--results', type=str, required=True,
                        help='Path to results JSON file from analyze_oversight.py')
    parser.add_argument('--dataset', type=str, default="data/gpqa_diamond",
                        help='Path to GPQA dataset (default: data/gpqa_diamond)')
    args = parser.parse_args()
    
    # Check if the results file exists
    if not os.path.exists(args.results):
        print(f"Error: Results file {args.results} not found")
        return
    
    # Run the comparison
    compare_claude_answers_with_actual(args.results, args.dataset)

if __name__ == "__main__":
    main()