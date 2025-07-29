import argparse
import concurrent.futures
import logging
import os
import re
from datetime import datetime
from time import perf_counter

from datasets import load_from_disk
from dotenv import load_dotenv
from openai import OpenAI
from tqdm.auto import tqdm

load_dotenv()


def sanitize_filename(text, max_len=30):
    sanitized = re.sub(r"[^a-zA-Z0-9_\s-]", "_", text).strip()
    sanitized = re.sub(r"[\s-]+", "_", sanitized)
    return sanitized[:max_len] if sanitized else "untitled"


def write_to_file(content, file):
    file.write(f"{content}\n\n---\n\n")
    file.flush()


def format_mmlu_pro_question(question_data):
    """Format MMLU-Pro question with multiple choice options."""
    question_text = question_data["question"]
    options = question_data["options"]
    
    # Format as multiple choice question
    formatted = f"{question_text}\n\n"
    for i, option in enumerate(options):
        letter = chr(65 + i)  # A, B, C, ... J
        formatted += f"{letter}. {option}\n"
    
    formatted += "\nPlease select the correct answer (A-J) and explain your reasoning."
    return formatted


def process_question(
    question_data, index, total, output_dir, temperature, logprobs=True, 
    model_name=None, model_display_name=None, dataset_name="gpqa"
):
    try:
        # Format question based on dataset
        if dataset_name == "mmlu_pro":
            question_text = format_mmlu_pro_question(question_data)
            question_preview = question_data["question"]
        else:  # gpqa
            question_text = question_data["Question"]
            question_preview = question_text
            
        safe_question = sanitize_filename(question_preview)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{output_dir}/{model_display_name}_response_{timestamp}_{safe_question}.md"
        logprobs_file = f"{output_dir}/{model_display_name}_logprobs_{timestamp}_{safe_question}.jsonl"
        os.makedirs(output_dir, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            write_to_file(f"# Original Question\n\n{question_text}", f)

            start_time = perf_counter()
            completion = openrouter_client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": question_text}],
                temperature=temperature,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                logprobs=logprobs,
                top_logprobs=20,
            )

            write_to_file(
                f"# {model_display_name} response (via openrouter)\n\n{completion.choices[0].message.content}",
                f,
            )
            
            # Check if the model returns reasoning (like deepseek-r1)
            if hasattr(completion.choices[0].message, 'reasoning') and completion.choices[0].message.reasoning:
                write_to_file(
                    f"# {model_display_name} reasoning (via openrouter)\n\n{completion.choices[0].message.reasoning}",
                    f,
                )

            if logprobs and completion.choices[0].logprobs:
                import json

                with open(logprobs_file, "w", encoding="utf-8") as lf:
                    for token_data in completion.choices[0].logprobs.content:
                        json.dump(
                            {
                                "token": token_data.token,
                                "logprob": token_data.logprob,
                                "bytes": token_data.bytes,
                                "top_logprobs": [
                                    {
                                        "token": tl.token,
                                        "logprob": tl.logprob,
                                        "bytes": tl.bytes,
                                    }
                                    for tl in token_data.top_logprobs
                                ],
                            },
                            lf,
                        )
                        lf.write("\n")

            logging.info(
                f"[{index}/{total}] Processed in {perf_counter() - start_time:.2f}s"
            )
            return output_file
    except Exception as e:
        logging.error(f"[{index}/{total}] Failed: {str(e)}")
        return None


def parse_args():
    parser = argparse.ArgumentParser(description="Run a custom model on dataset questions via OpenRouter")
    parser.add_argument("--model", type=str, required=True, help="Model name on OpenRouter (e.g., 'anthropic/claude-3.5-sonnet')")
    parser.add_argument("--model-display-name", type=str, required=True, help="Display name for the model (e.g., 'claude35')")
    parser.add_argument("--dataset", type=str, choices=["gpqa", "mmlu_pro"], default="gpqa", help="Dataset to use")
    parser.add_argument("--num_questions", type=int, default=200)
    parser.add_argument("--max_workers", type=int, default=30)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--logprobs", action="store_true", help="Request logprobs (if supported by model)")
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Load appropriate dataset
    if args.dataset == "mmlu_pro":
        dataset = load_from_disk("data/mmlu_pro")
        dataset_display = "mmlu_pro"
    else:
        dataset = load_from_disk("data/gpqa_diamond")
        dataset_display = "gpqa"
    
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    global openrouter_client
    openrouter_client = OpenAI(
        base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
    )

    if args.output_dir is None:
        args.output_dir = f"r1_rollouts/{dataset_display}_{args.model_display_name}_temp_{args.temperature}{'_logprobs' if args.logprobs else ''}"

    num_questions = min(args.num_questions, len(dataset))
    
    print(f"Running {args.model} on {num_questions} {args.dataset} questions...")
    print(f"Output directory: {args.output_dir}")
    
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=args.max_workers
    ) as executor:
        futures = [
            executor.submit(
                process_question,
                dataset[i],
                idx + 1,
                num_questions,
                args.output_dir,
                args.temperature,
                args.logprobs,
                args.model,
                args.model_display_name,
                args.dataset,
            )
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