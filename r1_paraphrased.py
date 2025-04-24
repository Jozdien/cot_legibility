import os
import re
import logging
import anthropic
import argparse
import concurrent.futures
from openai import OpenAI
from tqdm.auto import tqdm
from datetime import datetime
from time import perf_counter
from dotenv import load_dotenv
from datasets import load_from_disk

load_dotenv()

# --- Configuration ---
DATASET_PATH = "data/gpqa_diamond"
OUTPUT_DIR_BASE = "r1_rollouts"
DEEPSEEK_MODEL = "deepseek-reasoner"
ANTHROPIC_MODEL = "claude-3-7-sonnet-latest" # Example: Using Opus for paraphrase
OPENAI_MODEL = "gpt-4o"

# --- Initialize Clients ---
# Use a dictionary for easier management if more clients are added
clients = {
    "deepseek": OpenAI(
        base_url="https://api.deepseek.com/beta",
        api_key=os.getenv('DEEPSEEK_API_KEY'),
    ),
    "openrouter": OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv('OPENROUTER_API_KEY'),
    ),
    "anthropic": anthropic.Anthropic(
        api_key=os.getenv('ANTHROPIC_API_KEY'),
    ),
    "openai": OpenAI(api_key=os.getenv('OPENAI_API_KEY')) # Assuming OPENAI_API_KEY is set
}

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Helper Functions ---

def sanitize_filename(text, max_len=30):
    """Sanitizes text to be safe for filenames."""
    # Remove non-alphanumeric characters, replace spaces with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_\s-]', '_', text).strip()
    sanitized = re.sub(r'\s+', '_', sanitized)
    sanitized = re.sub(r'-', '_', sanitized)
    # Truncate and ensure it's not empty
    truncated = sanitized[:max_len]
    return truncated if truncated else "untitled"

def write_to_file(content, file):
    """Appends content block to the specified file."""
    file.write(f"{content}\n\n---\n\n")
    file.flush()

def extract_reasoning(completion, provider):
    """Extracts reasoning content based on the provider."""
    if provider == "deepseek":
        # Check if reasoning_content exists and is not None
        return getattr(getattr(completion.choices[0].message, 'reasoning_content', None), 'strip', lambda: "")() or ""
    elif provider == "openrouter":
        # Check if reasoning exists and is not None
        return getattr(getattr(completion.choices[0].message, 'reasoning', None), 'strip', lambda: "")() or ""
    else:
        logging.warning(f"Unknown provider '{provider}' for reasoning extraction.")
        return "" # Return empty string if provider unknown or reasoning missing

def get_completion_deepseek_with_fallback(model, messages, prefix=None, openrouter_only=False, openrouter_temperature=1):
    """Attempts DeepSeek API, falls back to OpenRouter, or uses OpenRouter directly."""
    start_time = perf_counter()

    # --- Attempt DeepSeek (if not openrouter_only) ---
    if not openrouter_only:
        deepseek_messages = messages.copy()
        if prefix:
            deepseek_messages.append({"role": "assistant", "prefix": True, "content": "", "reasoning_content": prefix})

        try:
            completion = clients["deepseek"].chat.completions.create(
                model=model,
                messages=deepseek_messages,
            )
            provider = "deepseek"
            logging.info(f"DeepSeek API ({model}) succeeded in {perf_counter() - start_time:.2f}s.")
            return completion, provider
        except Exception as e:
            logging.warning(f"DeepSeek API error for model {model}: {e}. Falling back to OpenRouter.")

    # --- Use OpenRouter (fallback or direct) ---
    openrouter_messages = messages.copy()
    if prefix:
        openrouter_messages.append({"role": "assistant", "content": f"<think>\n{prefix}"})

    try:
        # Map DeepSeek model names if necessary for OpenRouter
        openrouter_model_name = "deepseek/deepseek-r1" if model == "deepseek-reasoner" else model # Adjust if needed
        completion = clients["openrouter"].chat.completions.create(
            model=openrouter_model_name,
            messages=openrouter_messages,
            temperature=openrouter_temperature,
            extra_body={
                "include_reasoning": True,
                # Provider preference might change/be removed depending on OpenRouter API updates
                "provider": {"order": ["Nebius"], "allow_fallbacks": False}
            },
        )
        provider = "openrouter"
        logging.info(f"OpenRouter API ({openrouter_model_name}) succeeded in {perf_counter() - start_time:.2f}s.")
        return completion, provider
    except Exception as e:
        error_msg = f"OpenRouter API error for model {openrouter_model_name}" if openrouter_only else f"Both DeepSeek and OpenRouter failed for model {model}"
        logging.error(f"{error_msg}: {e}")
        raise Exception(error_msg) from e # Re-raise to be caught by the main loop

def get_completion_anthropic(model, messages):
    start_time = perf_counter()
    completion = clients["anthropic"].messages.create(
        model=model,
        max_tokens=1500, # Increased max_tokens slightly
        messages=messages
    )
    logging.info(f"Anthropic API ({model}) succeeded in {perf_counter() - start_time:.2f}s.")
    return completion

def get_completion_openai(model, messages):
    start_time = perf_counter()
    completion = clients["openai"].chat.completions.create(
        model=model,
        messages=messages
    )
    logging.info(f"OpenAI API ({model}) succeeded in {perf_counter() - start_time:.2f}s.")
    return completion

def check_if_output_exists(output_subdir, safe_question_prefix):
    """Checks if a file matching the question prefix exists in the output directory."""
    if not os.path.exists(output_subdir):
        return False
    try:
        for filename in os.listdir(output_subdir):
            # Check if filename ends with the specific pattern _safequestion.md
            if filename.endswith(f"_{safe_question_prefix}.md"):
                # More robust check: use regex to match the full pattern
                # pattern = re.compile(r"r1_faithful_cot_\d{8}_\d{6}_" + re.escape(safe_question_prefix) + r"\.md")
                # if pattern.match(filename):
                # For simplicity, the endswith check is kept as per the original request's implication.
                 return True
    except OSError as e:
        logging.error(f"Error checking directory {output_subdir}: {e}")
    return False


def process_question(question_text, index, total, cutoff_portion, output_subdir, openrouter_only, openrouter_temperature):
    """Processes a single question: gets completions, paraphrases, and final rollouts."""
    process_start_time = perf_counter()
    logging.info(f"[{index}/{total}] Starting processing: {question_text[:60]}...")

    safe_question_prefix = sanitize_filename(question_text)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = os.path.join(output_subdir, f"r1_faithful_cot_{timestamp}_{safe_question_prefix}.md")

    try:
        os.makedirs(output_subdir, exist_ok=True) # Ensure dir exists before writing

        with open(output_file_path, 'w', encoding='utf-8') as f: # Use UTF-8 encoding
            write_to_file(f"# Original Question\n\n{question_text}", f)

            messages = [{"role": "user", "content": question_text}]

            # 1. Initial DeepSeek/OpenRouter completion
            initial_completion, initial_provider = get_completion_deepseek_with_fallback(
                DEEPSEEK_MODEL, messages, openrouter_only=openrouter_only, openrouter_temperature=openrouter_temperature
            )
            initial_response = initial_completion.choices[0].message.content or ""
            initial_reasoning = extract_reasoning(initial_completion, initial_provider)

            if not initial_reasoning:
                 logging.warning(f"[{index}/{total}] Initial reasoning from {initial_provider} was empty.")
                 # Decide how to handle empty reasoning: skip?, use response?, use placeholder?
                 # For now, we'll proceed, but cutoff/paraphrase might be meaningless.
                 cutoff_reasoning = ""
            else:
                 cutoff_point = int(len(initial_reasoning) * cutoff_portion)
                 cutoff_reasoning = initial_reasoning[:cutoff_point]

            # Using header format from second file
            write_to_file(f"# DeepSeek response (via {initial_provider})\n\n{initial_response}", f)
            write_to_file(f"# DeepSeek reasoning (via {initial_provider})\n\n{initial_reasoning}", f)
            write_to_file(f"# Cut off deepseek reasoning\n\n{cutoff_reasoning}", f)

            # 2. Paraphrase the cut-off reasoning
            paraphrase_request_messages = [{
                "role": "user",
                "content": f"Please rephrase the following text while preserving the meaning. Do not try to shorten the text significantly. Only return the paraphrased text, without any preamble or explanation.\n\n---\n{cutoff_reasoning}\n---"
            }]

            # Get paraphrases only if there's reasoning to paraphrase
            anthropic_paraphrase = ""
            openai_paraphrase = ""
            if cutoff_reasoning:
                try:
                    anthropic_completion = get_completion_anthropic(ANTHROPIC_MODEL, paraphrase_request_messages)
                    # Extract text carefully, handling potential list structure
                    if anthropic_completion.content and isinstance(anthropic_completion.content, list):
                         anthropic_paraphrase = anthropic_completion.content[0].text or ""
                    write_to_file(f"# Anthropic completion\n\n{anthropic_paraphrase}", f)
                except Exception as e:
                    logging.error(f"[{index}/{total}] Anthropic paraphrase failed: {e}")
                    write_to_file(f"# Anthropic completion\n\nERROR: {e}", f)

                try:
                    openai_completion = get_completion_openai(OPENAI_MODEL, paraphrase_request_messages)
                    openai_paraphrase = openai_completion.choices[0].message.content or ""
                    write_to_file(f"# OpenAI completion\n\n{openai_paraphrase}", f)
                except Exception as e:
                    logging.error(f"[{index}/{total}] OpenAI paraphrase failed: {e}")
                    write_to_file(f"# OpenAI completion\n\nERROR: {e}", f)
            else:
                 logging.warning(f"[{index}/{total}] Skipping paraphrase due to empty cut-off reasoning.")
                 write_to_file(f"# Paraphrasing Skipped (Empty Input)", f)


            # 3. Final DeepSeek/OpenRouter completions using prefixes
            prefixes = {
                "cutoff": cutoff_reasoning,
                "anthropic_paraphrase": anthropic_paraphrase,
                "openai_paraphrase": openai_paraphrase
            }
            final_results = {}

            for name, prefix_content in prefixes.items():
                if not prefix_content and name != "cutoff": # Allow empty cutoff prefix if original reasoning was empty
                    logging.warning(f"[{index}/{total}] Skipping final completion for '{name}' due to empty prefix.")
                    if name == "anthropic_paraphrase":
                        write_to_file(f"# paraphrased_deepseek_completion_anthropic - SKIPPED (Empty Prefix)", f)
                    elif name == "openai_paraphrase":
                        write_to_file(f"# paraphrased_deepseek_completion_openai - SKIPPED (Empty Prefix)", f)
                    else:
                        write_to_file(f"# {name}_deepseek_completion - SKIPPED (Empty Prefix)", f)
                    continue
                try:
                    start_final = perf_counter()
                    final_completion, final_provider = get_completion_deepseek_with_fallback(
                        DEEPSEEK_MODEL, messages, prefix=prefix_content, openrouter_only=openrouter_only, openrouter_temperature=openrouter_temperature
                    )
                    final_response = final_completion.choices[0].message.content or ""
                    final_reasoning = extract_reasoning(final_completion, final_provider)

                    # Using exact header format from second file
                    if name == "cutoff":
                        write_to_file(f"# cutoff_deepseek_completion (via {final_provider})\n\n{str(final_completion)}", f)
                        write_to_file(f"# cutoff_deepseek_completion response\n\n{final_response}", f)
                        write_to_file(f"# cutoff_deepseek_completion reasoning\n\n{final_reasoning}", f)
                    elif name == "anthropic_paraphrase":
                        write_to_file(f"# paraphrased_deepseek_completion_anthropic (via {final_provider})\n\n{str(final_completion)}", f)
                        write_to_file(f"# paraphrased_deepseek_completion_anthropic response\n\n{final_response}", f)
                        write_to_file(f"# paraphrased_deepseek_completion_anthropic reasoning\n\n{final_reasoning}", f)
                    elif name == "openai_paraphrase":
                        write_to_file(f"# paraphrased_deepseek_completion_openai (via {final_provider})\n\n{str(final_completion)}", f)
                        write_to_file(f"# paraphrased_deepseek_completion_openai response\n\n{final_response}", f)
                        write_to_file(f"# paraphrased_deepseek_completion_openai reasoning\n\n{final_reasoning}", f)

                    final_results[name] = {'response': final_response, 'reasoning': final_reasoning, 'provider': final_provider}
                    logging.info(f"[{index}/{total}] Final completion '{name}' took {perf_counter() - start_final:.2f}s")

                except Exception as e:
                    logging.error(f"[{index}/{total}] Final completion with prefix '{name}' failed: {e}")
                    write_to_file(f"# {name}_deepseek_completion - ERROR\n\n{e}", f)


        total_time = perf_counter() - process_start_time
        logging.info(f"[{index}/{total}] Successfully processed. Total time: {total_time:.2f}s. Output: {output_file_path}")
        return output_file_path

    except Exception as e:
        logging.exception(f"[{index}/{total}] UNHANDLED error processing question: {question_text[:60]}... - {e}")
        # Optionally delete the potentially incomplete file
        if os.path.exists(output_file_path):
             try: os.remove(output_file_path)
             except OSError: pass
        return None # Indicate failure
    
def parse_args():
    parser = argparse.ArgumentParser(description="Process questions with DeepSeek and OpenRouter")
    parser.add_argument('--num_questions', type=int, default=20, help='Number of questions to process')
    parser.add_argument('--max_concurrent_workers', type=int, default=40, help='Number of concurrent workers')
    parser.add_argument('--cutoff_portion', type=float, default=0.25, help='Portion of initial reasoning to keep/paraphrase')
    parser.add_argument('--openrouter_only', action='store_true', help='Use OpenRouter only')
    parser.add_argument('--override_existing', action='store_true', help='Process all questions, even if output files exist')
    parser.add_argument('--output_subdir', type=str, default=None, help='Output subdirectory name')
    parser.add_argument('--openrouter_temperature', type=float, default=1, help='Temperature for OpenRouter')
    return parser.parse_args()

def main():
    args = parse_args()

    # --- Load Dataset ---
    try:
        gpqa_dataset = load_from_disk(DATASET_PATH)
        logging.info(f"Dataset loaded from {DATASET_PATH}. Contains {len(gpqa_dataset)} questions.")
    except Exception as e:
        logging.error(f"Failed to load dataset from {DATASET_PATH}: {e}")
        return

    # --- Determine Output Directory ---
    api_source_tag = "openrouter" if args.openrouter_only else "deepseek_openrouter"
    if args.output_subdir:
        output_subdir = os.path.join(OUTPUT_DIR_BASE, args.output_subdir)
    else:
        output_subdir = os.path.join(OUTPUT_DIR_BASE, f"cutoff_{args.cutoff_portion}_{api_source_tag}")
    logging.info(f"Output will be saved to: {output_subdir}")
    # No need to create dir here, process_question handles it.

    # --- Prepare List of Questions to Process ---
    questions_to_process = []
    indices_to_consider = list(range(min(args.num_questions, len(gpqa_dataset))))
    skipped_count = 0

    for i, dataset_index in enumerate(indices_to_consider):
        question_data = gpqa_dataset[dataset_index]
        question_text = question_data['Question']
        current_index = i + 1 # User-friendly 1-based index

        if not args.override_existing:
            safe_q_prefix = sanitize_filename(question_text)
            if check_if_output_exists(output_subdir, safe_q_prefix):
                logging.info(f"[{current_index}/{len(indices_to_consider)}] Skipping question (output exists): {question_text[:60]}...")
                skipped_count += 1
                continue # Skip to the next question

        # If not overriding or file doesn't exist, add to list
        questions_to_process.append(
            (current_index, question_text) # Pass only needed info
        )

    total_to_run = len(questions_to_process)
    if skipped_count > 0:
        logging.info(f"Skipped {skipped_count} questions because output files already exist (override_existing=False).")
    if total_to_run == 0:
        logging.info("No questions left to process.")
        return
    logging.info(f"Starting processing for {total_to_run} questions...")


    # --- Process Questions Concurrently ---
    processed_count = 0
    failed_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_concurrent_workers) as executor:
        # Create futures
        future_to_info = {
            executor.submit(
                process_question,
                q_text,
                idx,          # Pass the 1-based index for logging
                total_to_run, # Pass the count of questions actually being run
                args.cutoff_portion,
                output_subdir,
                args.openrouter_only,
                args.openrouter_temperature
            ): (idx, q_text)
            for idx, q_text in questions_to_process
        }

        # Process completed futures
        with tqdm(total=total_to_run, desc="Processing questions") as pbar:
            for future in concurrent.futures.as_completed(future_to_info):
                idx, q_text = future_to_info[future]
                try:
                    result_path = future.result()
                    if result_path:
                        processed_count += 1
                    else:
                        failed_count += 1
                except Exception as e:
                    failed_count += 1
                    logging.error(f"[{idx}/{total_to_run}] Future returned an unexpected error for question: {q_text[:60]}... - {e}", exc_info=True)
                pbar.update(1)

    logging.info(f"\n--- Processing Complete ---")
    logging.info(f"Attempted: {total_to_run} questions")
    logging.info(f"Successfully processed: {processed_count}")
    logging.info(f"Failed: {failed_count}")
    logging.info(f"Skipped (already existed): {skipped_count}")
    logging.info(f"Output directory: {output_subdir}")

if __name__ == "__main__":
    main()