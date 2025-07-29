"""
Download and prepare MMLU-Pro dataset from Hugging Face.
MMLU-Pro is a more challenging version of MMLU with 10 choices per question instead of 4.
"""

from datasets import load_dataset
import os

def main():
    print("Downloading MMLU-Pro dataset from Hugging Face...")
    
    # Load MMLU-Pro dataset
    # Using the TIGER-Lab/MMLU-Pro dataset which has multiple-choice questions with 10 options
    dataset = load_dataset("TIGER-Lab/MMLU-Pro")
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Save the test split (MMLU-Pro's main evaluation set)
    save_path = "data/mmlu_pro"
    print(f"Saving MMLU-Pro test split to {save_path}...")
    
    # MMLU-Pro structure:
    # - question: The question text
    # - options: List of 10 answer options (A-J)
    # - answer: The correct answer letter (A-J)
    # - answer_index: The index of the correct answer (0-9)
    # - cot_content: Chain of thought content (if available)
    # - category: Subject category
    # - src: Source dataset
    
    dataset["test"].save_to_disk(save_path)
    
    print(f"Successfully saved MMLU-Pro dataset with {len(dataset['test'])} questions")
    print("\nDataset structure:")
    print("- question: The question text")
    print("- options: List of 10 answer options (A-J)")
    print("- answer: The correct answer letter (A-J)")
    print("- answer_index: The index of the correct answer (0-9)")
    print("- category: Subject category")
    print("- cot_content: Chain of thought content (if available)")
    
    # Print a sample question
    sample = dataset["test"][0]
    print("\nSample question:")
    print(f"Category: {sample['category']}")
    print(f"Question: {sample['question'][:100]}...")
    print(f"Options: {len(sample['options'])} choices (A-J)")
    print(f"Correct answer: {sample['answer']}")

if __name__ == "__main__":
    main()