import os
import re
import argparse
from glob import glob
from datasets import load_from_disk

def extract_answer_from_text(text, is_reasoning=False):
    if is_reasoning:
        # Try a more greedy approach that gets everything after "Final Answer" to the end
        final_answer_match = re.search(r'\*\*Final Answer\*\*:?\s*([\s\S]*)', text)
        if final_answer_match:
            return final_answer_match.group(1).strip()
            
        return "No final answer found in reasoning"
    else:
        # For response sections, just return the whole text
        return text.strip()

def get_actual_answer(question_text, dataset):
    # Find the matching question in the dataset
    for item in dataset:
        if item['Question'].strip() == question_text.strip():
            return item['Correct Answer']
    return "No matching answer found"

def process_file(filepath, dataset):
    results = {
        'cutoff': None,
        'anthropic': None,
        'openai': None,
        'actual': None,
        'question': None
    }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Split content into sections based on markdown headers
        sections = content.split('\n# ')
        
        for section in sections:
            if not section.strip():
                continue
                
            section_title = section.split('\n')[0].lower()
            section_content = '\n'.join(section.split('\n')[1:])
            
            if 'original question' in section_title:
                results['question'] = section_content.strip()
                # Get actual answer from dataset
                results['actual'] = get_actual_answer(section_content[:-4].strip(), dataset)
            elif 'cutoff_deepseek_completion response' in section_title:
                results['cutoff'] = extract_answer_from_text(section_content, is_reasoning=False)
            elif 'cutoff_deepseek_completion reasoning' in section_title:
                if not results['cutoff']:  # only use reasoning if we don't have a response
                    results['cutoff'] = extract_answer_from_text(section_content, is_reasoning=True)
            elif 'paraphrased_deepseek_completion_anthropic response' in section_title:
                results['anthropic'] = extract_answer_from_text(section_content, is_reasoning=False)
            elif 'paraphrased_deepseek_completion_anthropic reasoning' in section_title:
                if not results['anthropic']:  # only use reasoning if we don't have a response
                    results['anthropic'] = extract_answer_from_text(section_content, is_reasoning=True)
            elif 'paraphrased_deepseek_completion_openai response' in section_title:
                results['openai'] = extract_answer_from_text(section_content, is_reasoning=False)
            elif 'paraphrased_deepseek_completion_openai reasoning' in section_title:
                if not results['openai']:  # only use reasoning if we don't have a response
                    results['openai'] = extract_answer_from_text(section_content, is_reasoning=True)
    
    return results

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Analyze answers from markdown files and compare with actual answers.')
    parser.add_argument('--dir', type=str, default='r1_rollouts', 
                        help='Directory containing markdown files to analyze (default: r1_rollouts)')
    parser.add_argument('--output', type=str, default='answer_comparisons.md',
                        help='Output file path (default: answer_comparisons.md)')
    args = parser.parse_args()
    
    output_file = args.output
    
    # Load the GPQA dataset
    dataset_path = "data/gpqa_diamond"
    gpqa_dataset = load_from_disk(dataset_path)
    
    # Find all markdown files in the specified directory and its subdirectories
    rollout_files = glob(f'{args.dir}/**/*.md', recursive=True)
    
    print(f"Found {len(rollout_files)} markdown files to analyze in {args.dir}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for filepath in rollout_files:
            results = process_file(filepath, gpqa_dataset)
            
            # Write to file
            f.write(f"## Question from {os.path.basename(filepath)}\n\n")
            f.write(f"**Original Question:**\n{results['question']}\n\n")
            f.write(f"**Cutoff Continuation Answer:**\n{results['cutoff']}\n\n")
            f.write(f"**Anthropic Continuation Answer:**\n{results['anthropic']}\n\n")
            f.write(f"**OpenAI Continuation Answer:**\n{results['openai']}\n\n")
            f.write(f"**Actual Answer:**\n{results['actual']}\n\n")
            f.write("---\n\n")
    
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()