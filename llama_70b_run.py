import os
import re
import logging
import argparse
import concurrent.futures
from openai import OpenAI
from tqdm.auto import tqdm
from datetime import datetime
from time import perf_counter
from dotenv import load_dotenv
from datasets import load_from_disk

load_dotenv()

def sanitize_filename(text, max_len=30):
    sanitized = re.sub(r'[^a-zA-Z0-9_\s-]', '_', text).strip()
    sanitized = re.sub(r'[\s-]+', '_', sanitized)
    return sanitized[:max_len] if sanitized else "untitled"

def write_to_file(content, file):
    file.write(f"{content}\n\n---\n\n")
    file.flush()

def process_question(question_text, index, total, output_dir, temperature):
    safe_question = sanitize_filename(question_text)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{output_dir}/r1_response_{timestamp}_{safe_question}.md"
    os.makedirs(output_dir, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        write_to_file(f"# Original Question\n\n{question_text}", f)
        
        start_time = perf_counter()
        completion = openrouter_client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": "Reason about the question at length and in exhaustive detail (at least 5000 words), and then answer the question."
                },
                {
                    "role": "user",
                    "content": question_text
                }
            ],
            temperature=temperature,
            # extra_body={
            #     "include_reasoning": True,
            #     "provider": {"order": ["Nebius"], "allow_fallbacks": False}
            # }
        )
        
        write_to_file(f"# DeepSeek response (via openrouter)\n\n{completion.choices[0].message.content}", f)
        write_to_file(f"# DeepSeek reasoning (via openrouter)\n\n{completion.choices[0].message.reasoning}", f)
        
        logging.info(f"[{index}/{total}] Processed in {perf_counter() - start_time:.2f}s")
        return output_file

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_questions', type=int, default=200)
    parser.add_argument('--max_workers', type=int, default=10)
    parser.add_argument('--output_dir', type=str, default=None)
    parser.add_argument('--temperature', type=float, default=1.0)
    return parser.parse_args()

def main():
    args = parse_args()
    gpqa_dataset = load_from_disk("data/gpqa_diamond")
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    global openrouter_client
    openrouter_client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv('OPENROUTER_API_KEY')
    )

    if args.output_dir is None:
        args.output_dir = f"r1_rollouts/llama_70b_only_temp_{args.temperature}"

    num_questions = min(args.num_questions, len(gpqa_dataset))
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = [
            executor.submit(process_question, 
                          gpqa_dataset[i]['Question'], 
                          idx + 1, 
                          num_questions,
                          args.output_dir,
                          args.temperature)
            for idx, i in enumerate(range(num_questions))
        ]

        success = 0
        with tqdm(total=num_questions, desc="Processing") as pbar:
            for future in concurrent.futures.as_completed(futures):
                if future.result():
                    success += 1
                pbar.update(1)

    logging.info(f"Completed {success}/{num_questions} questions successfully")

if __name__ == "__main__":
    main()