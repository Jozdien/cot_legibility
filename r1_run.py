from time import perf_counter
from openai import OpenAI
from datetime import datetime
import os
from dotenv import load_dotenv
from datasets import load_from_disk

load_dotenv()

# Load the GPQA dataset
dataset_path = "data/gpqa_diamond"
gpqa_dataset = load_from_disk(dataset_path)
print(f"Dataset contains {len(gpqa_dataset)} questions")

def write_to_file(content, file):
    file.write(f"{content}\n\n---\n\n")
    file.flush()

# Initialize OpenRouter client
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('OPENROUTER_API_KEY'),
)

def get_completion(model, messages):
    completion = openrouter_client.chat.completions.create(
        model=model,
        messages=messages,
        extra_body={
            "include_reasoning": True,
            "provider": {
                "order": ["Nebius"],
                "allow_fallbacks": False
            }
        },
    )
    return completion

def process_question(question_text, output_dir="r1_simple_responses"):
    # Create directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Sanitize question text for filename
    safe_question = "".join(c if c.isalnum() else "_" for c in question_text[:30])
    
    # Create a file with timestamp and question preview
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{output_dir}/r1_response_{timestamp}_{safe_question}.md"

    with open(file_path, 'w') as f:
        write_to_file(f"# Original Question\n\n{question_text}", f)
        
        model = "deepseek/deepseek-r1"
        messages = [{"role": "user", "content": question_text}]

        # Get completion
        start_time = perf_counter()
        completion = get_completion(model, messages)
        end_time = perf_counter()
        
        # Write response and reasoning
        write_to_file(f"# R1 response\n\n{completion.choices[0].message.content}", f)
        write_to_file(f"# R1 reasoning\n\n{completion.choices[0].message.reasoning}", f)
        
        print(f"Completion time: {end_time - start_time:.2f} seconds")

    return file_path

def main():
    # Define how many questions to process
    num_questions = 200  # Change this as needed
    
    # Process sequentially
    indices = range(min(num_questions, len(gpqa_dataset)))
    
    for i, idx in enumerate(indices):
        question = gpqa_dataset[idx]['Question']
        print(f"\nProcessing question {i+1}/{len(indices)}: {question[:50]}...")
        
        try:
            output_file = process_question(question)
            print(f"Results written to: {output_file}")
        except Exception as e:
            print(f"Error processing question: {e}")
            continue
        
        # Add delay between questions to avoid rate limiting
        if i < len(indices) - 1:
            import time
            time.sleep(5)  # 5 second delay between questions

if __name__ == "__main__":
    main()