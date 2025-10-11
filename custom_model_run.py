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


def process_question(
    question_text,
    index,
    total,
    output_dir,
    temperature,
    logprobs=True,
    model_name=None,
    model_display_name=None,
):
    try:
        safe_question = sanitize_filename(question_text)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = (
            f"{output_dir}/{model_display_name}_response_{timestamp}_{safe_question}.md"
        )
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
                extra_body={
                    "include_reasoning": True,
                    # Provider preference might change/be removed depending on OpenRouter API updates
                    "provider": {"order": ["Nebius"], "allow_fallbacks": False},
                },
            )

            write_to_file(
                f"# {model_display_name} response (via openrouter)\n\n{completion.choices[0].message.content}",
                f,
            )

            # Check if the model returns reasoning (like deepseek-r1)
            if (
                hasattr(completion.choices[0].message, "reasoning")
                and completion.choices[0].message.reasoning
            ):
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
    parser = argparse.ArgumentParser(
        description="Run a custom model on GPQA questions via OpenRouter"
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Model name on OpenRouter (e.g., 'anthropic/claude-3.5-sonnet')",
    )
    parser.add_argument(
        "--model-display-name",
        type=str,
        required=True,
        help="Display name for the model (e.g., 'claude35')",
    )
    parser.add_argument("--num_questions", type=int, default=200)
    parser.add_argument("--max_workers", type=int, default=30)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument(
        "--logprobs",
        action="store_true",
        help="Request logprobs (if supported by model)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    gpqa_dataset = load_from_disk("data/gpqa_diamond")
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    global openrouter_client
    openrouter_client = OpenAI(
        base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
    )

    if args.output_dir is None:
        args.output_dir = f"r1_rollouts/{args.model_display_name}_temp_{args.temperature}{'_logprobs' if args.logprobs else ''}"

    num_questions = min(args.num_questions, len(gpqa_dataset))
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=args.max_workers
    ) as executor:
        futures = [
            executor.submit(
                process_question,
                gpqa_dataset[i]["Question"],
                idx + 1,
                num_questions,
                args.output_dir,
                args.temperature,
                args.logprobs,
                args.model,
                args.model_display_name,
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
