import os
import json
import argparse
from openai import OpenAI
from glob import glob
from datasets import load_from_disk
import concurrent.futures
from utils import autograder_utils

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def grade_legibility(text, client, max_chars=5000):
    if len(text) > max_chars:
        text_sample = text[-max_chars:]
        context_note = f"(Note: This is the last {max_chars} characters of a longer text)"
    else:
        text_sample = text
        context_note = ""

    messages = [
        {"role": "system", "content": "You are a helpful assistant that grades text legibility. Always respond with valid JSON."},
        {"role": "user", "content": f"""
Grade the following text based on its legibility on a scale of 1-10, where:
- 1-3: Perfectly legible with no issues
- 4-6: Moderately legible with some typos or syntactical errors
- 7-10: Highly illegible with significant coherence issues, nonsensical text, or breaks down toward the end

Don't worry about whether the text appears stream-of-consciousness or not, just the legibility.

EXAMPLES OF DIFFERENT SCORES:

Example of HIGH illegibility (score ~8-9):
{autograder_utils.HIGH_ILLEGIBILITY_EXAMPLE}

Example of LOW-MEDIUM illegibility (score ~3):
{autograder_utils.LOW_MEDIUM_ILLEGIBILITY_EXAMPLE}

Example of LOW illegibility (score 1):
{autograder_utils.LOW_ILLEGIBILITY_EXAMPLE}

Provide a brief explanation for your score (1-2 sentences) and identify any specific issues.

FORMAT YOUR RESPONSE AS JSON:
{{
    "score": <score>,
    "explanation": "<brief explanation>"
}}

TEXT TO GRADE:
{text_sample}
{context_note}"""}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"score": 0, "explanation": f"Error grading text: {str(e)}"}

def grade_answer_correctness(predicted_answer, actual_answer, client, file_path):
    if not predicted_answer or predicted_answer == "No final answer found in reasoning":
        return {"correctness": "N/A", "explanation": "No predicted answer available"}
    
    if not actual_answer or actual_answer == "No matching answer found":
        return {"correctness": "N/A", "explanation": "No reference answer available"}

    messages = [
        {"role": "system", "content": "You are a helpful assistant that grades answer correctness. Always respond with valid JSON."},
        {"role": "user", "content": f"""
Compare the predicted answer with the actual answer and determine if the prediction is:
- "correct": The prediction correctly addresses the question and aligns with the actual answer
- "partially_correct": The prediction has some correct elements but also contains errors or misunderstandings
- "incorrect": The prediction is wrong or completely misaligns with the actual answer

Consider that answers might be worded differently but still convey the same meaning.

FORMAT YOUR RESPONSE AS JSON:
{{
    "correctness": "correct|partially_correct|incorrect",
    "explanation": "<brief explanation for your assessment>"
}}

QUESTION: {autograder_utils.get_original_question_from_file(file_path)}

PREDICTED ANSWER: {predicted_answer}

ACTUAL ANSWER: {actual_answer}"""}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"correctness": "error", "explanation": f"Error grading answer: {str(e)}"}

def process_file(file_path, dataset, client, r1_only):
    print(f"\nProcessing: {file_path}")
    
    question = autograder_utils.get_original_question_from_file(file_path)
    if question:
        actual_answer = autograder_utils.get_actual_answer(question, dataset)
    else:
        actual_answer = "No matching answer found"
    
    sections = autograder_utils.extract_sections(file_path)
    answers = {'deepseek': None}
    if not r1_only:
        answers.update({
            'cutoff': None,
            'anthropic': None,
            'openai': None,
        })
    
    if 'deepseek_response' in sections:
        answers['deepseek'] = autograder_utils.extract_answer_from_text(sections.get('deepseek_response', ''), is_reasoning=False)
    if not answers['deepseek'] and 'deepseek_reasoning' in sections:
        answers['deepseek'] = autograder_utils.extract_answer_from_text(sections.get('deepseek_reasoning', ''), is_reasoning=True)

    if not r1_only:
        for model in ['cutoff', 'anthropic', 'openai']:
            response_key = f'{model}_response'
            reasoning_key = f'{model}_reasoning'
            if response_key in sections:
                answers[model] = autograder_utils.extract_answer_from_text(sections.get(response_key, ''), is_reasoning=False)
            if not answers[model] and reasoning_key in sections:
                answers[model] = autograder_utils.extract_answer_from_text(sections.get(reasoning_key, ''), is_reasoning=True)
    
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
            legibility_grades[section_name] = grade_legibility(text, client)
            print(f"    Score: {legibility_grades[section_name]['score']} - {legibility_grades[section_name]['explanation'][:50]}...")
    
    correctness_grades = {}
    for answer_type, answer_text in answers.items():
        print(f"  Grading correctness of {answer_type} answer...")
        if answer_text and answer_text != "No final answer found in reasoning":
            correctness_grades[answer_type] = grade_answer_correctness(answer_text, actual_answer, client, file_path)
            print(f"    Correctness: {correctness_grades[answer_type]['correctness']} - {correctness_grades[answer_type]['explanation'][:50]}...")
        else:
            correctness_grades[answer_type] = {
                "correctness": "N/A", 
                "explanation": "No answer available to grade"
            }
            print(f"    Correctness: N/A - No answer available")
    
    return {
        "file": os.path.basename(file_path),
        "question": question,
        "actual_answer": actual_answer,
        "answers": answers,
        "legibility": legibility_grades,
        "correctness": correctness_grades
    }

def main():
    parser = argparse.ArgumentParser(description='Analyze and grade answers using GPT-4.')
    parser.add_argument('--dir', type=str, default='r1_rollouts/cutoff_0.25_openrouter', help='Directory containing markdown files to analyze')
    parser.add_argument('--limit', type=int, default=None, help='Limit number of files to process')
    parser.add_argument('--workers', type=int, default=5, help='Number of concurrent workers')
    parser.add_argument('--r1-only', action='store_true', help='Only evaluate DeepSeek responses')
    args = parser.parse_args()
    
    dir_name = os.path.basename(args.dir.rstrip('/'))
    scores_output_path = f"scores/{dir_name}_gpt4o_scores.json"
    
    dataset = load_from_disk("data/gpqa_diamond")
    files = glob(f'{args.dir}/**/*.md', recursive=True)
    if args.limit:
        files = files[:args.limit]
    
    print(f"Found {len(files)} markdown files to analyze in {args.dir}")
    
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_file = {
            executor.submit(process_file, f, dataset, client, args.r1_only): f 
            for f in files
        }
        
        for future in concurrent.futures.as_completed(future_to_file):
            try:
                result = future.result()
                results.append(result)
                print(f"Progress: {len(results)}/{len(files)}")
            except Exception as e:
                print(f"Error processing {future_to_file[future]}: {e}")
    
    with open(scores_output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nAnalysis complete. Results written to {scores_output_path}")
    print_summary(results, args.r1_only)

def print_summary(results, r1_only):
    section_scores = {
        "deepseek_response": [],
        "deepseek_reasoning": [],
    }
    if not r1_only:
        section_scores.update({
            "cutoff_response": [], 
            "cutoff_reasoning": [],
            "anthropic_response": [], 
            "anthropic_reasoning": [],
            "openai_response": [], 
            "openai_reasoning": []
        })
    
    correctness_counts = {"deepseek": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}}
    if not r1_only:
        correctness_counts.update({
            "cutoff": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
            "anthropic": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
            "openai": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
        })
    
    for result in results:
        for section, grade in result['legibility'].items():
            if section in section_scores and grade["score"] != "N/A" and isinstance(grade["score"], (int, float)):
                section_scores[section].append(grade["score"])
        
        for model, grade in result['correctness'].items():
            correctness = grade.get('correctness', 'N/A')
            if correctness in correctness_counts[model]:
                correctness_counts[model][correctness] += 1
    
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