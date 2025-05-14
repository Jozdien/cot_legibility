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

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--indices', type=int, nargs='+', required=True,
                      help='Question indices to sample from dataset')
    parser.add_argument('--samples', type=int, required=True,
                      help='Number of samples to generate per question')
    parser.add_argument('--max_workers', type=int, default=30)
    parser.add_argument('--output_dir', type=str, default=None)
    parser.add_argument('--temperature', type=float, default=1.0)
    return parser.parse_args()

def sanitize_filename(text, max_len=30):
    sanitized = re.sub(r'[^a-zA-Z0-9_\s-]', '_', text).strip()
    sanitized = re.sub(r'[\s-]+', '_', sanitized)
    return sanitized[:max_len] if sanitized else "untitled"

def process_question(question_text, question_idx, sample_idx, total_samples, output_dir, temperature):
    try:
        safe_question = sanitize_filename(question_text)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{output_dir}/q{question_idx}_sample{sample_idx}_{timestamp}_{safe_question}.md"
        os.makedirs(output_dir, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            start_time = perf_counter()
            completion = openrouter_client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=[{"role": "user", "content": question_text}],
                temperature=temperature,
                extra_body={
                    "include_reasoning": True,
                    "provider": {"order": ["Nebius"], "allow_fallbacks": False}
                }
            )
            
            f.write(f"# Original Question\n\n{question_text}\n\n---\n\n")
            f.write(f"# DeepSeek response (via openrouter)\n\n{completion.choices[0].message.content}\n\n---\n\n")
            f.write(f"# DeepSeek reasoning (via openrouter)\n\n{completion.choices[0].message.reasoning}\n")
            
            logging.info(f"[Q{question_idx} S{sample_idx}/{total_samples}] Processed in {perf_counter() - start_time:.2f}s")
            return output_file
    except Exception as e:
        logging.error(f"[Q{question_idx} S{sample_idx}/{total_samples}] Failed: {str(e)}")
        return None

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
        args.output_dir = f"r1_rollouts/q_repeat_temp_{args.temperature}"

    total_tasks = len(args.indices) * args.samples
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = []
        for idx in args.indices:
            question = gpqa_dataset[idx]['Question']
            for sample in range(args.samples):
                futures.append(
                    executor.submit(process_question,
                                  question,
                                  idx,
                                  sample + 1,
                                  args.samples,
                                  args.output_dir,
                                  args.temperature)
                )

        success = 0
        with tqdm(total=total_tasks, desc="Processing") as pbar:
            for future in concurrent.futures.as_completed(futures):
                if future.result():
                    success += 1
                pbar.update(1)

    logging.info(f"Completed {success}/{total_tasks} samples successfully")

if __name__ == "__main__":
    main()