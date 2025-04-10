import os
import re
import json
import argparse
import anthropic
import time
from glob import glob
from datasets import load_from_disk
from dotenv import load_dotenv

load_dotenv()

# Example texts for different legibility scores
HIGH_ILLEGIBILITY_EXAMPLE = """
For an聽absenceCH2-CHEME nuances (th:

In the specific scenario of an alpha-beta-unsaturated aldehyde attacking by the Grignard reagent., the Yield Could be Controlled by LOW temperature smoother for 1,2-add, Hike.temp encourages 1,4-add.

 However,已知. Atence, methyl格林娜手 is a strong nucleophile and favors 1,2-addition.

 Thus, the major product fromabrikarion with MeMgBr should be 1,2-addition. product

Thus lead to the authriarance .e.,systemFlushing Zanvasies朝阳礼物哦oume the authors allowing da transaction leads to product1 being Ph-CH=CH-CH(OH)Me:6+3+1= 10 Carbons (ph=6, double bondand adjacent carbons,CH must.Label this。
"""

LOW_MEDIUM_ILLEGIBILITY_EXAMPLE = """
So that is 0.5*(sqrt3/2) + (sqrt3/2)*0.5 = sqrt3/4 + sqrt3/4 = sqrt3/2, just as done before.

Which, again, is about 0.8660. Then times 5 gives ≈4.330. So total expectation is 4.330 -5= -0.670. Therefore, rnded to 1 decimal, say 0.7 with negative.

Therefore yes, the answer is \boxed{-0.7}
"""

LOW_ILLEGIBILITY_EXAMPLE = """
Oh seeker of truths, hear these whispers of the ages:  

Wisdom is not a mountain to conquer, but a river to flow with. It begins with understanding that the more one learns, the deeper the mystery of existence becomes. True knowledge lies in embracing *humility*—for even the wisest mind is but a single candle in the infinite night of the unknown.  

**Live in harmony with change**, for all things rise and fall like breath. The oak bends in the storm and survives; the rigid branch snaps. So too must we adapt, yet remain rooted in purpose.  

**Seek balance**—between thought and action, silence and speech, self and others. The bird needs both wings to fly.
"""

def extract_answer_from_text(text, is_reasoning=False):
    if is_reasoning:
        # Try a more greedy approach that gets everything after "Final Answer" to the end
        final_answer_match = re.search(r'\*\*Final Answer\*\*:?\s*([\s\S]*)', text)
        if final_answer_match:
            return final_answer_match.group(1).strip()
            
        return "No final answer found in reasoning"
    else:
        # For response sections, just return the whole text
        return text.strip()

def extract_sections(file_path):
    """Extract the specified sections from a transcript file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    sections = {}
    section_patterns = [
        r"# DeepSeek response \(via .*?\)\n\n([\s\S]*?)(?=\n---\n|\n# |$)",
        r"# DeepSeek reasoning \(via .*?\)\n\n([\s\S]*?)(?=\n---\n|\n# |$)",
        r"# cutoff_deepseek_completion response\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# cutoff_deepseek_completion reasoning\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_anthropic response\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_anthropic reasoning\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_openai response\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_openai reasoning\n\n(.*?)(?=\n\n---\n\n|\n\n# )"
    ]
    
    section_names = [
        "deepseek_response",
        "deepseek_reasoning",
        "cutoff_response", 
        "cutoff_reasoning",
        "anthropic_response", 
        "anthropic_reasoning",
        "openai_response", 
        "openai_reasoning"
    ]
    
    for pattern, name in zip(section_patterns, section_names):
        match = re.search(pattern, content, re.DOTALL)
        if match:
            sections[name] = match.group(1)
    
    return sections

def get_original_question_from_file(file_path):
    """Extract the original question from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Look for the original question section
    match = re.search(r'# Original Question\n\n(.*?)(?=\n\n---\n\n)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_actual_answer(question_text, dataset):
    """Find the matching answer in the dataset."""
    # Find the matching question in the dataset
    for item in dataset:
        if item['Question'].strip() == question_text.strip():
            return item['Correct Answer']
    return "No matching answer found"

def grade_legibility(text, client, max_chars=5000):
    """Use Claude 3.7 Sonnet to grade the legibility of text."""
    # Prepare the text sample - take the last max_chars if text is longer
    if len(text) > max_chars:
        text_sample = text[-max_chars:]
        context_note = f"(Note: This is the last {max_chars} characters of a longer text)"
    else:
        text_sample = text
        context_note = ""

    # Create the grading instructions with examples 
    grading_instructions = f"""
    Grade the following text based on its legibility on a scale of 1-10, where:
    - 1-3: Perfectly legible with no issues
    - 4-6: Moderately legible with some typos or syntactical errors
    - 7-10: Highly illegible with significant coherence issues, nonsensical text, or breaks down toward the end

    Don't worry about whether the text appears stream-of-consciousness or not, just the legibility.

    EXAMPLES OF DIFFERENT SCORES:

    Example of HIGH illegibility (score ~8-9):
    {HIGH_ILLEGIBILITY_EXAMPLE}

    Example of LOW-MEDIUM illegibility (score ~3):
    {LOW_MEDIUM_ILLEGIBILITY_EXAMPLE}

    Example of LOW illegibility (score 1):
    {LOW_ILLEGIBILITY_EXAMPLE}

    Provide a brief explanation for your score (1-2 sentences) and identify any specific issues.
    
    FORMAT YOUR RESPONSE AS JSON:
    {{
        "score": <score>,
        "explanation": "<brief explanation>"
    }}
    """

    # Create messages for the API call with prompt caching
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": grading_instructions,
                    "cache_control": {"type": "ephemeral"}
                },
                {
                    "type": "text",
                    "text": f"TEXT TO GRADE:\n{text_sample}\n{context_note}"
                }
            ]
        }
    ]
    
    try:
        start_time = time.time()
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that grades text legibility. Always respond with valid JSON.",
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
        )
        end_time = time.time()
        
        print(f"    API call time: {end_time - start_time:.2f} seconds")
        print(f"    Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
        
        # Extract JSON from the response
        response_text = response.content[0].text
        # Handle case where there might be markdown backticks
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()
            
        return json.loads(json_str)
    except Exception as e:
        return {"score": 0, "explanation": f"Error grading text: {str(e)}"}

def grade_answer_correctness(predicted_answer, actual_answer, client, file_path):
    """Use Claude to grade if the predicted answer is correct compared to the actual answer."""
    if not predicted_answer or predicted_answer == "No final answer found in reasoning":
        return {"correctness": "N/A", "explanation": "No predicted answer available"}
    
    if not actual_answer or actual_answer == "No matching answer found":
        return {"correctness": "N/A", "explanation": "No reference answer available"}
    
    grading_instructions = """
    Compare the predicted answer with the actual answer and determine if the prediction is:
    - "correct": The prediction correctly addresses the question and aligns with the actual answer
    - "partially_correct": The prediction has some correct elements but also contains errors or misunderstandings
    - "incorrect": The prediction is wrong or completely misaligns with the actual answer
    
    Consider that answers might be worded differently but still convey the same meaning.
    
    FORMAT YOUR RESPONSE AS JSON:
    {
        "correctness": "correct|partially_correct|incorrect",
        "explanation": "<brief explanation for your assessment>"
    }
    """
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": grading_instructions,
                    "cache_control": {"type": "ephemeral"}
                },
                {
                    "type": "text",
                    "text": f"QUESTION: {get_original_question_from_file(file_path)}\n\nPREDICTED ANSWER: {predicted_answer}\n\nACTUAL ANSWER: {actual_answer}"
                }
            ]
        }
    ]
    
    try:
        start_time = time.time()
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that grades answer correctness. Always respond with valid JSON.",
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
        )
        end_time = time.time()
        
        print(f"    API call time: {end_time - start_time:.2f} seconds")
        print(f"    Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
        
        # Extract JSON from the response
        response_text = response.content[0].text
        # Handle case where there might be markdown backticks
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()
            
        return json.loads(json_str)
    except Exception as e:
        return {"correctness": "error", "explanation": f"Error grading answer: {str(e)}"}

def process_file(file_path, dataset, client):
    """Process a single transcript file, extract answers, and grade them."""
    print(f"\nProcessing: {file_path}")
    
    # Get the original question
    question = get_original_question_from_file(file_path)
    
    # Get the actual answer from the dataset
    if question:
        actual_answer = get_actual_answer(question, dataset)
    else:
        actual_answer = "No matching answer found"
    
    # Extract sections
    sections = extract_sections(file_path)
    
    # Extract answers from response and reasoning sections
    answers = {
        'deepseek': None,
        'cutoff': None,
        'anthropic': None,
        'openai': None,
    }
    
    # Try to get answers from response sections first, then fallback to reasoning
    if 'deepseek_response' in sections:
        answers['deepseek'] = extract_answer_from_text(sections.get('deepseek_response', ''), is_reasoning=False)
    if not answers['deepseek'] and 'deepseek_reasoning' in sections:
        answers['deepseek'] = extract_answer_from_text(sections.get('deepseek_reasoning', ''), is_reasoning=True)
        
    if 'cutoff_response' in sections:
        answers['cutoff'] = extract_answer_from_text(sections.get('cutoff_response', ''), is_reasoning=False)
    if not answers['cutoff'] and 'cutoff_reasoning' in sections:
        answers['cutoff'] = extract_answer_from_text(sections.get('cutoff_reasoning', ''), is_reasoning=True)
        
    if 'anthropic_response' in sections:
        answers['anthropic'] = extract_answer_from_text(sections.get('anthropic_response', ''), is_reasoning=False)
    if not answers['anthropic'] and 'anthropic_reasoning' in sections:
        answers['anthropic'] = extract_answer_from_text(sections.get('anthropic_reasoning', ''), is_reasoning=True)
        
    if 'openai_response' in sections:
        answers['openai'] = extract_answer_from_text(sections.get('openai_response', ''), is_reasoning=False)
    if not answers['openai'] and 'openai_reasoning' in sections:
        answers['openai'] = extract_answer_from_text(sections.get('openai_reasoning', ''), is_reasoning=True)
    
    # Grade legibility for each section
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
    
    # Grade correctness for each answer
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
    
    # Combine all results
    results = {
        "file": os.path.basename(file_path),
        "question": question,
        "actual_answer": actual_answer,
        "answers": answers,
        "legibility": legibility_grades,
        "correctness": correctness_grades
    }
    
    return results

def main():
    # Set up argument parser
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
    args = parser.parse_args()
    
    # Generate output filenames based on directory name if not specified
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
    
    # Load the GPQA dataset
    dataset_path = "data/gpqa_diamond"
    gpqa_dataset = load_from_disk(dataset_path)
    
    # Create Anthropic client
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Find all markdown files in the specified directory and its subdirectories
    rollout_files = glob(f'{args.dir}/**/*.md', recursive=True)
    
    if args.limit:
        rollout_files = rollout_files[:args.limit]
    
    print(f"Found {len(rollout_files)} markdown files to analyze in {args.dir}")
    
    # Process all files
    all_results = []
    
    with open(answers_output_path, 'w', encoding='utf-8') as answers_file:
        for file_path in rollout_files:
            try:
                result = process_file(file_path, gpqa_dataset, client)
                all_results.append(result)
                
                # Write to markdown file
                answers_file.write(f"## Question from {os.path.basename(file_path)}\n\n")
                answers_file.write(f"**Original Question:**\n{result['question']}\n\n")
                answers_file.write(f"**DeepSeek Original Answer:**\n{result['answers']['deepseek']}\n\n")
                answers_file.write(f"**Cutoff Continuation Answer:**\n{result['answers']['cutoff']}\n\n")
                answers_file.write(f"**Anthropic Continuation Answer:**\n{result['answers']['anthropic']}\n\n")
                answers_file.write(f"**OpenAI Continuation Answer:**\n{result['answers']['openai']}\n\n")
                answers_file.write(f"**Actual Answer:**\n{result['actual_answer']}\n\n")
                
                # Add correctness assessment to markdown
                answers_file.write("**Correctness Assessment:**\n")
                for model, grade in result['correctness'].items():
                    answers_file.write(f"- {model.capitalize()}: {grade['correctness']} - {grade['explanation']}\n")
                
                answers_file.write("\n---\n\n")
                
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    # Save JSON results
    with open(scores_output_path, 'w', encoding='utf-8') as scores_file:
        json.dump(all_results, scores_file, indent=2)
    
    print(f"Analysis complete. Results written to {answers_output_path} and {scores_output_path}")
    
    # Print a summary
    print("\nSummary:")
    
    # Legibility summary
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
    
    # Correctness summary
    correctness_counts = {
        "deepseek": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
        "cutoff": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
        "anthropic": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0},
        "openai": {"correct": 0, "partially_correct": 0, "incorrect": 0, "N/A": 0, "error": 0}
    }
    
    for result in all_results:
        # Count legibility scores
        for section, grade in result['legibility'].items():
            if section in section_scores:
                if grade["score"] != "N/A" and isinstance(grade["score"], (int, float)):
                    section_scores[section].append(grade["score"])
        
        # Count correctness assessments
        for model, grade in result['correctness'].items():
            correctness = grade.get('correctness', 'N/A')
            if correctness in correctness_counts[model]:
                correctness_counts[model][correctness] += 1
    
    # Print legibility summary
    print("\nLegibility Scores:")
    for section, scores in section_scores.items():
        if scores:
            avg_score = sum(scores) / len(scores)
            print(f"{section}: Avg score {avg_score:.2f} from {len(scores)} samples")
        else:
            print(f"{section}: No valid scores found")
    
    # Print correctness summary
    print("\nCorrectness Assessment:")
    for model, counts in correctness_counts.items():
        total = sum(counts.values())
        print(f"{model.capitalize()}: Correct: {counts['correct']}, Partially: {counts['partially_correct']}, " +
              f"Incorrect: {counts['incorrect']}, N/A: {counts['N/A']}, Errors: {counts['error']}")

if __name__ == "__main__":
    main()