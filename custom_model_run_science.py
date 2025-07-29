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
    """Write content to file with proper flushing to prevent corruption."""
    try:
        file.write(f"{content}\n\n---\n\n")
        file.flush()
        os.fsync(file.fileno())  # Force write to disk
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        raise


def format_mmlu_pro_question(question_data):
    """Format MMLU-Pro question with multiple choice options."""
    question_text = question_data["question"]
    options = question_data["options"]
    
    formatted = f"{question_text}\n\n"
    for i, option in enumerate(options):
        letter = chr(65 + i)  # A, B, C, ... J
        formatted += f"{letter}. {option}\n"
    
    formatted += "\nPlease select the correct answer (A-J) and explain your reasoning."
    return formatted


def format_scienceqa_question(question_data):
    """Format ScienceQA question with hint if available."""
    question_text = question_data["question"]
    choices = question_data.get("choices", [])
    hint = question_data.get("hint", "")
    
    formatted = f"{question_text}\n\n"
    
    # Add hint if available
    if hint and hint.strip():
        formatted += f"Hint: {hint}\n\n"
    
    # Add choices
    for i, choice in enumerate(choices):
        letter = chr(65 + i)  # A, B, C, ...
        formatted += f"{letter}. {choice}\n"
    
    formatted += "\nPlease select the correct answer and provide detailed reasoning for your choice."
    return formatted


def format_chembench_question(question_data):
    """Format ChemBench question - adapt based on actual structure."""
    # ChemBench has questions nested in 'examples' list
    if "examples" in question_data and len(question_data["examples"]) > 0:
        example = question_data["examples"][0]
        question_text = example.get("input", "")
        
        # Check if there are multiple choice options in target_scores
        target_scores = example.get("target_scores", "")
        if target_scores:
            try:
                import json
                scores_dict = json.loads(target_scores)
                # Extract options from scores dict
                options = list(scores_dict.keys())
                
                formatted = f"{question_text}\n\n"
                for i, option in enumerate(options):
                    letter = chr(65 + i)
                    formatted += f"{letter}. {option}\n"
                formatted += "\nPlease select the correct answer and show your complete reasoning process."
                return formatted
            except:
                pass
        
        # If no multiple choice, treat as open-ended
        if question_text:
            return f"{question_text}\n\nPlease provide a detailed answer with complete reasoning and calculations where applicable."
    
    # Fallback if structure is different
    question_text = question_data.get("question", question_data.get("input", ""))
    if question_text:
        return f"{question_text}\n\nPlease provide a detailed answer with complete reasoning and calculations where applicable."
    
    return "Please provide a detailed answer with complete reasoning and calculations where applicable."


def format_question_for_dataset(question_data, dataset_name):
    """Route to appropriate formatter based on dataset."""
    formatters = {
        "mmlu_pro": format_mmlu_pro_question,
        "scienceqa": format_scienceqa_question,
        "chembench": format_chembench_question,
        "gpqa": lambda q: q["Question"],  # Original GPQA format
    }
    
    formatter = formatters.get(dataset_name, lambda q: str(q))
    return formatter(question_data)


def get_question_preview(question_data, dataset_name):
    """Get a short preview of the question for filename."""
    if dataset_name == "gpqa":
        return question_data["Question"]
    elif dataset_name == "scienceqa":
        return question_data["question"]
    elif dataset_name == "chembench":
        # ChemBench has questions in examples[0].input
        if "examples" in question_data and len(question_data["examples"]) > 0:
            return question_data["examples"][0].get("input", "unknown")
        return question_data.get("question", "unknown")
    elif dataset_name == "mmlu_pro":
        return question_data.get("question", "unknown")
    else:
        return question_data.get("question", "unknown")


def process_question(
    question_data, index, total, output_dir, temperature, logprobs=True, 
    model_name=None, model_display_name=None, dataset_name="gpqa"
):
    try:
        # Format question based on dataset
        question_text = format_question_for_dataset(question_data, dataset_name)
        question_preview = get_question_preview(question_data, dataset_name)
            
        safe_question = sanitize_filename(question_preview)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Add microseconds and index to ensure uniqueness
        unique_id = f"{timestamp}_{datetime.now().microsecond:06d}_{index:04d}"
        output_file = f"{output_dir}/{model_display_name}_response_{unique_id}_{safe_question}.md"
        logprobs_file = f"{output_dir}/{model_display_name}_logprobs_{unique_id}_{safe_question}.jsonl"
        os.makedirs(output_dir, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            try:
                write_to_file(f"# Original Question\n\n{question_text}", f)
                
                # Add dataset-specific context if available
                if dataset_name == "scienceqa":
                    if "subject" in question_data:
                        write_to_file(f"# Subject: {question_data['subject']}", f)
                    if "topic" in question_data:
                        write_to_file(f"# Topic: {question_data['topic']}", f)
            except Exception as e:
                logging.error(f"Error writing initial content for {output_file}: {e}")
                raise

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

            # Write response with length check and validation
            response_content = completion.choices[0].message.content
            if response_content:
                # Clean up any potential corruption patterns
                if response_content.startswith("# ") or response_content.startswith("## "):
                    logging.warning(f"Response starts with markdown header, cleaning up")
                    response_content = response_content.lstrip("#").strip()
                
                # Check for repeated header patterns (sign of corruption)
                header_pattern = f"# {model_display_name} response (via openrouter)"
                if header_pattern in response_content:
                    logging.warning(f"Response contains header pattern, likely corrupted")
                    # Try to extract clean content
                    parts = response_content.split(header_pattern)
                    response_content = parts[0] if parts[0] else parts[-1]
                
                # Truncate extremely long responses to prevent file corruption
                if len(response_content) > 100000:  # 100KB limit
                    logging.warning(f"Response truncated from {len(response_content)} to 100000 chars")
                    response_content = response_content[:100000] + "\n\n[TRUNCATED DUE TO LENGTH]"
                
                write_to_file(
                    f"# {model_display_name} response (via openrouter)\n\n{response_content}",
                    f,
                )
            
            # Check if the model returns reasoning (like deepseek-r1)
            if hasattr(completion.choices[0].message, 'reasoning') and completion.choices[0].message.reasoning:
                reasoning_content = completion.choices[0].message.reasoning
                # Truncate extremely long reasoning to prevent file corruption
                if len(reasoning_content) > 200000:  # 200KB limit for reasoning
                    logging.warning(f"Reasoning truncated from {len(reasoning_content)} to 200000 chars")
                    reasoning_content = reasoning_content[:200000] + "\n\n[TRUNCATED DUE TO LENGTH]"
                
                write_to_file(
                    f"# {model_display_name} reasoning (via openrouter)\n\n{reasoning_content}",
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
    parser = argparse.ArgumentParser(description="Run a custom model on science dataset questions via OpenRouter")
    parser.add_argument("--model", type=str, required=True, help="Model name on OpenRouter")
    parser.add_argument("--model-display-name", type=str, required=True, help="Display name for the model")
    parser.add_argument("--dataset", type=str, 
                       choices=["gpqa", "mmlu_pro", "scienceqa", "chembench"], 
                       default="scienceqa", 
                       help="Dataset to use")
    parser.add_argument("--num_questions", type=int, default=200)
    parser.add_argument("--max_workers", type=int, default=30)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--logprobs", action="store_true", help="Request logprobs if supported")
    parser.add_argument("--subject-filter", type=str, default=None, 
                       help="Filter by subject (for ScienceQA)")
    parser.add_argument("--topic-filter", type=str, default=None,
                       help="Filter by topic (for ScienceQA)")
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Load appropriate dataset
    dataset_paths = {
        "gpqa": "data/gpqa_diamond",
        "mmlu_pro": "data/mmlu_pro",
        "scienceqa": "data/scienceqa_hard",
        "chembench": "data/chembench"
    }
    
    dataset_path = dataset_paths.get(args.dataset)
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        print(f"Please run get_{args.dataset}.py first to download the dataset.")
        return
    
    dataset = load_from_disk(dataset_path)
    
    # Shuffle dataset to get a good mix of questions
    dataset = dataset.shuffle(seed=42)
    
    # Apply additional filters if specified
    if args.dataset == "scienceqa" and (args.subject_filter or args.topic_filter):
        if args.subject_filter:
            dataset = dataset.filter(lambda x: args.subject_filter.lower() in x.get('subject', '').lower())
        if args.topic_filter:
            dataset = dataset.filter(lambda x: args.topic_filter.lower() in x.get('topic', '').lower())
    
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    global openrouter_client
    openrouter_client = OpenAI(
        base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
    )

    if args.output_dir is None:
        args.output_dir = f"r1_rollouts/{args.dataset}_{args.model_display_name}_temp_{args.temperature}{'_logprobs' if args.logprobs else ''}"

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