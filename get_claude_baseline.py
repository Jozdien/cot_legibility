import os
import json
import time
import anthropic
from datasets import load_from_disk
from tqdm import tqdm
import logging
from dotenv import load_dotenv
import concurrent.futures

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_original_question_from_file(file_path):
    """Extract the original question from the dataset file"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get("question", "Question not found")
    except Exception as e:
        logging.error(f"Error reading question from file {file_path}: {e}")
        return "Error retrieving question"

def get_claude_answer(question, client, model="claude-3-7-sonnet-20250219", thinking=True, max_retries=3):
    """Get an answer from Claude for a given question"""
    retry_count = 0
    while retry_count < max_retries:
        try:
            if thinking:
                response = client.messages.create(
                    model=model,
                    max_tokens=20000,
                    thinking={
                        "type": "enabled",
                        "budget_tokens": 16000
                    },
                    messages=[
                        {"role": "user", "content": f"{question}"}
                    ]
                )
            else:
                response = client.messages.create(
                    model=model,
                    max_tokens=4000,
                    temperature=1,
                    messages=[
                        {"role": "user", "content": f"{question}"}
                    ]
                )
            text_content = next((block.text for block in response.content if block.type == 'text'), None)
            thinking_content = next((block.thinking for block in response.content if block.type == 'thinking'), None)
            return text_content, thinking_content
        except Exception as e:
            retry_count += 1
            logging.warning(f"Error getting answer, retry {retry_count}/{max_retries}: {e}")
            time.sleep(5 * retry_count)  # Exponential backoff
    
    return "ERROR: Failed to get answer after multiple attempts"

def grade_answer_correctness(question, predicted_answer, actual_answer, client, question_id=None):
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
                    "text": f"QUESTION: {question}\n\nPREDICTED ANSWER: {predicted_answer}\n\nACTUAL ANSWER: {actual_answer}"
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
        
        logging.info(f"Grading for q{question_id} - API call time: {end_time - start_time:.2f}s, Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
        
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
        logging.error(f"Error grading answer for q{question_id}: {e}")
        return {"correctness": "error", "explanation": f"Error grading answer: {str(e)}"}

def save_answers_to_file(answers, filename="claude_answers.json"):
    """Save Claude's answers to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(answers, f, indent=2)
    logging.info(f"Saved answers to {filename}")

def save_scores_to_file(scores, filename="claude_scores.json"):
    """Save scores to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(scores, f, indent=2)
    logging.info(f"Saved scores to {filename}")

def process_question(item, client, idx):
    """Process a single question with Claude"""
    question_id = item.get("Question ID", f"q{idx}")
    question = item["Question"]
    correct_answer = item["Correct Answer"]
    
    logging.info(f"Processing question {question_id}")
    
    # Get Claude's answer
    claude_answer, claude_thinking = get_claude_answer(question, client)
    
    # Store the answer
    answer_result = {
        "question": question,
        "answer": claude_answer,
        "reasoning": claude_thinking
    }
    
    # Grade the answer correctness
    grade_result = grade_answer_correctness(question, claude_answer, correct_answer, client, question_id)
    
    return question_id, answer_result, grade_result

def main():
    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Load the dataset
    dataset = load_from_disk("data/gpqa_diamond")
    logging.info(f"Loaded dataset with {len(dataset)} questions")
    limit = 100
    workers = 5  # Number of concurrent workers

    # Initialize results dictionaries
    claude_answers = {}
    claude_scores = {
        "detailed_results": {},
        "summary": {
            "Claude Baseline": {
                "correct": 0,
                "partially_correct": 0,
                "incorrect": 0,
                "N/A": 0,
                "error": 0
            }
        },
        "percentages": {
            "Claude Baseline": {}
        }
    }
    
    processed_count = 0
    failed_count = 0
    total_to_run = min(limit, len(dataset)) if limit else len(dataset)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_item = {
            executor.submit(process_question, item, client, idx): (idx, item)
            for idx, item in enumerate(dataset) if not limit or idx < limit
        }
        
        for future in tqdm(concurrent.futures.as_completed(future_to_item), 
                         total=total_to_run, 
                         desc="Processing questions"):
            try:
                question_id, answer_result, grade_result = future.result()
                
                # Store results
                claude_answers[question_id] = answer_result
                claude_scores["detailed_results"][question_id] = {
                    "question": answer_result["question"],
                    "actual_answer": future_to_item[future][1]["Correct Answer"],
                    "grade": grade_result
                }
                
                # Update summary counts
                correctness = grade_result.get("correctness", "error")
                claude_scores["summary"]["Claude Baseline"][correctness] += 1
                
                processed_count += 1
                
            except Exception as e:
                failed_count += 1
                logging.error(f"Error processing question: {e}")
            
            logging.info(f"Progress: {processed_count + failed_count}/{total_to_run} "
                      f"({processed_count} successful, {failed_count} failed)")
    
    # Calculate percentages
    total_valid = sum(count for key, count in claude_scores["summary"]["Claude Baseline"].items() 
                     if key not in ["N/A", "error"])
    if total_valid > 0:
        claude_scores["percentages"]["Claude Baseline"] = {
            "correct_pct": round(claude_scores["summary"]["Claude Baseline"]["correct"] / total_valid * 100, 1),
            "partially_pct": round(claude_scores["summary"]["Claude Baseline"]["partially_correct"] / total_valid * 100, 1),
            "incorrect_pct": round(claude_scores["summary"]["Claude Baseline"]["incorrect"] / total_valid * 100, 1),
            "total_valid": total_valid,
            "total_NA": claude_scores["summary"]["Claude Baseline"]["N/A"],
            "total_error": claude_scores["summary"]["Claude Baseline"]["error"]
        }
    
    # Save results to files
    save_answers_to_file(claude_answers, "claude_answers/temp_1_claude_baseline_answers.json")
    save_scores_to_file(claude_scores, "claude_answers/scores/temp_1_claude_baseline_scores.json")
    
    logging.info(f"Analysis complete. Successfully processed: {processed_count}")
    logging.info(f"Failed: {failed_count}")

if __name__ == "__main__":
    main()