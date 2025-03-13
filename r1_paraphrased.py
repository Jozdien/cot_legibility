from time import perf_counter
import anthropic
from openai import OpenAI
import json
from datetime import datetime
import os
from dotenv import load_dotenv
from datasets import load_from_disk
import random

load_dotenv()

# Load the GPQA dataset
dataset_path = "data/gpqa_diamond"
gpqa_dataset = load_from_disk(dataset_path)
print(f"Dataset contains {len(gpqa_dataset)} questions")

def write_to_file(content, file):
    file.write(f"{content}\n\n---\n\n")
    file.flush()

# Initialize clients
deepseek_client = OpenAI(
    base_url="https://api.deepseek.com/beta",
    api_key=os.getenv('DEEPSEEK_API_KEY'),
)

openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('OPENROUTER_API_KEY'),
)

anthropic_client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
)

openai_client = OpenAI()

def get_completion_deepseek_with_fallback(model, messages, prefix=None):
    """
    Attempt to use DeepSeek API first, then fall back to OpenRouter if it fails.
    """
    # Prepare the payload for DeepSeek
    deepseek_messages = messages.copy()
    if prefix:
        deepseek_messages.append({
            "role": "assistant",
            "prefix": True,
            "content": "",
            "reasoning_content": prefix
        })
    
    # try:
    #     # Try DeepSeek API first
    #     completion = deepseek_client.chat.completions.create(
    #         model=model,
    #         messages=deepseek_messages,
    #     )
    #     # If we get here, the request succeeded
    #     print("DeepSeek API worked.")
    #     return completion, "deepseek"
    
    # except Exception as e:
    #     print(f"DeepSeek API error: {e}")
    #     print("Falling back to OpenRouter API...")
        
    # Prepare OpenRouter messages - format differs slightly
    openrouter_messages = messages.copy()
    if prefix:
        # For OpenRouter, we use a different approach since it doesn't support prefix directly
        openrouter_messages.append({
            "role": "assistant",
            "content": f"<think>\n{prefix}"
        })
    
    # Try OpenRouter as fallback
    # try:
    model = "deepseek/deepseek-r1" if model == "deepseek-reasoner" else model
    completion = openrouter_client.chat.completions.create(
        model=model,
        messages=openrouter_messages,
        extra_body={
            "include_reasoning": True,
            "provider": {
                "order": ["Nebius"],
                "allow_fallbacks": False
            }
        },
    )
    return completion, "openrouter"
    # except Exception as e:
    #     print(f"OpenRouter API error: {e}")
    #     raise Exception("Both DeepSeek and OpenRouter APIs failed")

def get_completion_anthropic(model, messages):
    completion = anthropic_client.messages.create(
        model=model,
        max_tokens=1024,
        messages=messages
    )
    return completion

def get_completion_openai(model, messages):
    completion = openai_client.chat.completions.create(
        model=model,
        messages=messages
    )
    return completion

def process_question(question_text, output_dir="r1_rollouts"):
    # Create directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Sanitize question text for filename
    safe_question = "".join(c if c.isalnum() else "_" for c in question_text[:30])

    cutoff_portion = 0.25
    
    # Create a temp file with timestamp and question preview
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    temp_file_path = f"{output_dir}/cutoff_{cutoff_portion}_openrouter/r1_faithful_cot_{timestamp}_{safe_question}.md"

    with open(temp_file_path, 'w') as f:
        write_to_file(f"# Original Question\n\n{question_text}", f)
        
        deepseek_model = "deepseek-reasoner"
        anthropic_model = "claude-3-5-sonnet-20241022"
        openai_model = "gpt-4o"

        messages = [
            {
                "role": "user",
                "content": question_text
            }
        ]

        # Initial DeepSeek completion with fallback
        start_time_initial_deepseek = perf_counter()
        deepseek_completion, provider = get_completion_deepseek_with_fallback(deepseek_model, messages)
        
        # Handle differences in response format between DeepSeek and OpenRouter
        if provider == "deepseek":
            deepseek_reasoning = deepseek_completion.choices[0].message.reasoning_content
        else:  # openrouter
            deepseek_reasoning = deepseek_completion.choices[0].message.reasoning
        
        cut_off_deepseek_reasoning = deepseek_reasoning[:int(len(deepseek_reasoning) * cutoff_portion)]
        
        write_to_file(f"# DeepSeek response (via {provider})\n\n{deepseek_completion.choices[0].message.content}", f)
        write_to_file(f"# DeepSeek reasoning (via {provider})\n\n{deepseek_reasoning}", f)
        write_to_file(f"# Cut off deepseek reasoning\n\n{cut_off_deepseek_reasoning}", f)
        end_time_initial_deepseek = perf_counter()
        print(f"Initial DeepSeek completion time: {end_time_initial_deepseek - start_time_initial_deepseek:.2f} seconds")

        # Create paraphrase request
        paraphrase_request = f"""Hi! Please rephrase the following text while preserving the meaning; do not try to shorten the text. Only return the paraphrased text, don't preamble.\n\n\"\"\"{cut_off_deepseek_reasoning}\"\"\""""
        paraphrase_request_messages = [
            {
                "role": "user",
                "content": paraphrase_request
            }
        ]

        # Get completions from other models
        start_time_anthropic = perf_counter()
        anthropic_completion = get_completion_anthropic(anthropic_model, paraphrase_request_messages)
        end_time_anthropic = perf_counter()
        print(f"Anthropic completion time: {end_time_anthropic - start_time_anthropic:.2f} seconds")

        start_time_openai = perf_counter()
        openai_completion = get_completion_openai(openai_model, paraphrase_request_messages)
        end_time_openai = perf_counter()
        print(f"OpenAI completion time: {end_time_openai - start_time_openai:.2f} seconds")

        write_to_file(f"# Anthropic completion\n\n{anthropic_completion.content[0].text}", f)
        write_to_file(f"# OpenAI completion\n\n{openai_completion.choices[0].message.content}", f)

        # Get prefixes for final completions
        cutoff_prefix = cut_off_deepseek_reasoning
        anthropic_prefix = anthropic_completion.content[0].text
        openai_prefix = openai_completion.choices[0].message.content

        # Final completions with fallback
        start_time_final_deepseek = perf_counter()

        cutoff_deepseek_completion, cutoff_provider = get_completion_deepseek_with_fallback(deepseek_model, messages, prefix=cutoff_prefix)
        write_to_file(f"# cutoff_deepseek_completion (via {cutoff_provider})\n\n{str(cutoff_deepseek_completion)}", f)
        write_to_file(f"# cutoff_deepseek_completion response\n\n{cutoff_deepseek_completion.choices[0].message.content}", f)
        
        if cutoff_provider == "deepseek":
            cutoff_reasoning = cutoff_deepseek_completion.choices[0].message.reasoning_content
        else:
            cutoff_reasoning = cutoff_deepseek_completion.choices[0].message.reasoning
        write_to_file(f"# cutoff_deepseek_completion reasoning\n\n{cutoff_reasoning}", f)

        paraphrased_deepseek_completion_anthropic, anthropic_provider = get_completion_deepseek_with_fallback(deepseek_model, messages, prefix=anthropic_prefix)
        write_to_file(f"# paraphrased_deepseek_completion_anthropic (via {anthropic_provider})\n\n{str(paraphrased_deepseek_completion_anthropic)}", f)
        write_to_file(f"# paraphrased_deepseek_completion_anthropic response\n\n{paraphrased_deepseek_completion_anthropic.choices[0].message.content}", f)
        
        if anthropic_provider == "deepseek":
            anthropic_reasoning = paraphrased_deepseek_completion_anthropic.choices[0].message.reasoning_content
        else:
            anthropic_reasoning = paraphrased_deepseek_completion_anthropic.choices[0].message.reasoning
        write_to_file(f"# paraphrased_deepseek_completion_anthropic reasoning\n\n{anthropic_reasoning}", f)

        paraphrased_deepseek_completion_openai, openai_provider = get_completion_deepseek_with_fallback(deepseek_model, messages, prefix=openai_prefix)
        write_to_file(f"# paraphrased_deepseek_completion_openai (via {openai_provider})\n\n{str(paraphrased_deepseek_completion_openai)}", f)
        write_to_file(f"# paraphrased_deepseek_completion_openai response\n\n{paraphrased_deepseek_completion_openai.choices[0].message.content}", f)
        
        if openai_provider == "deepseek":
            openai_reasoning = paraphrased_deepseek_completion_openai.choices[0].message.reasoning_content
        else:
            openai_reasoning = paraphrased_deepseek_completion_openai.choices[0].message.reasoning
        write_to_file(f"# paraphrased_deepseek_completion_openai reasoning\n\n{openai_reasoning}", f)

        end_time_final_deepseek = perf_counter()
        print(f"Final DeepSeek completions time: {end_time_final_deepseek - start_time_final_deepseek:.2f} seconds")
        print(f"Total time: {end_time_final_deepseek - start_time_initial_deepseek:.2f} seconds")

    return temp_file_path

def main():
    # Define how many questions to process
    num_questions = 200  # Change this as needed
    
    # Randomly sample questions or process sequentially
    # Option 1: Random sample
    # indices = random.sample(range(len(gpqa_dataset)), min(num_questions, len(gpqa_dataset)))
    
    # Option 2: Sequential processing
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
        
        # Optional: add a delay between questions to avoid rate limiting
        if i < len(indices) - 1:
            import time
            time.sleep(5)  # 5 second delay between questions

if __name__ == "__main__":
    main()