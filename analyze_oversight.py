import os
import re
import json
import time
import anthropic
import argparse
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
)

# Define the sections we want to analyze
SECTIONS_TO_ANALYZE = [
    "# DeepSeek reasoning",
    "# Cut off deepseek reasoning",
    "# cutoff_deepseek_completion reasoning",
    "# Anthropic completion",
    "# OpenAI completion",
    "# paraphrased_deepseek_completion_anthropic reasoning",
    "# paraphrased_deepseek_completion_openai reasoning"
]

def extract_section(content, section_marker):
    """Extract a specific section from the content."""
    pattern = f"{re.escape(section_marker)}.*?\\n\\n(.*?)(?=\\n\\n(?:---|#)|$)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_original_question(content):
    """Extract the original question from the content."""
    return extract_section(content, "# Original Question")

def analyze_reasoning_with_claude(question, reasoning):
    """
    Send the question and reasoning to Claude and ask if it can derive the answer.
    """
    prompt = f"""Please answer the following question:
{question}

Here's some prior reasoning related to the question that might help:
{reasoning}
"""

    # Add exponential backoff for rate limiting
    max_retries = 5
    base_delay = 2
    
    for attempt in range(max_retries):
        try:
            response = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1000,
                temperature=0,
                # system="You are a helpful AI assistant analyzing reasoning traces to determine if they lead to a conclusive answer.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            if attempt < max_retries - 1:
                sleep_time = base_delay ** attempt
                print(f"Rate limited or error. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                return f"Error after {max_retries} attempts: {str(e)}"

def process_rollout_file(file_path):
    """Process a single rollout file and analyze all reasoning sections."""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_question = extract_original_question(content)
    if not original_question:
        print(f"Original question not found in {file_path}")
        return None
    
    results = {
        "file_path": file_path,
        "original_question": original_question,
        "answers": {}
    }
    
    for section in SECTIONS_TO_ANALYZE:
        section_name = section.replace("# ", "").strip()
        reasoning = extract_section(content, section)
        
        if reasoning:
            print(f"  Analyzing {section_name}...")
            answer = analyze_reasoning_with_claude(original_question, reasoning)
            # Store both the reasoning trace and the answer
            results["answers"][section_name] = {
                "reasoning_trace": reasoning,
                "answer": answer
            }
        else:
            print(f"  Section {section_name} not found")
            results["answers"][section_name] = {
                "reasoning_trace": None,
                "answer": "Section not found in file"
            }
    
    return results

def process_directory(directory_path, limit=None):
    """Process a limited number of rollout files in a directory and its subdirectories."""
    all_results = {}
    
    # Get the name of the directory for the output file
    dir_name = os.path.basename(directory_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"claude_answers_{dir_name}_{timestamp}.json"
    
    # Walk through all subdirectories
    files_processed = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Process the file
                results = process_rollout_file(file_path)
                if results:
                    all_results[file_path] = results
                
                # Save results incrementally to avoid losing progress
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(all_results, f, indent=2)
                
                files_processed += 1
                # Check if we've reached the limit
                if limit is not None and files_processed >= limit:
                    print(f"Reached limit of {limit} files. Stopping.")
                    break
        
        # Also check the limit after processing files in a directory
        if limit is not None and files_processed >= limit:
            break
                    
    print(f"Analysis complete. Results saved to {output_file}")
    
    # Also create a more readable markdown summary
    # create_markdown_summary(all_results, f"claude_answers_{dir_name}_{timestamp}.md")
    
    return all_results

def create_markdown_summary(results, output_file):
    """Create a markdown summary of the analysis results."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Claude 3.7 Reasoning Analysis Summary\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for file_path, result in results.items():
            file_name = os.path.basename(file_path)
            f.write(f"## {file_name}\n\n")
            f.write(f"**Original Question:**\n{result['original_question']}\n\n")
            
            for section_name, answer in result['answers'].items():
                f.write(f"### {section_name}\n\n")
                f.write(f"{answer}\n\n")
            
            f.write("---\n\n")

def main():
    """Main function to run the script."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Analyze reasoning traces with Claude 3.7')
    parser.add_argument('--dir', type=str, default='r1_rollouts/cutoff_0.5_openrouter',
                        help='Full path to the directory to process')
    parser.add_argument('--limit', type=int, default=None,
                        help='Maximum number of files to process (default: no limit)')
    args = parser.parse_args()
    
    # Check if the directory exists
    if not os.path.exists(args.dir):
        print(f"Directory {args.dir} not found")
        return
    
    print(f"Processing directory: {args.dir}")
    process_directory(args.dir, args.limit)

if __name__ == "__main__":
    main()