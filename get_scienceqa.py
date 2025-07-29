"""
Download and prepare ScienceQA dataset from Hugging Face.
ScienceQA is a multimodal science question dataset with detailed explanations.
We'll focus on the text-only questions that require reasoning.
"""

from datasets import load_dataset
import os

def main():
    print("Downloading ScienceQA dataset from Hugging Face...")
    
    # Load ScienceQA dataset
    # Using derek-thomas/ScienceQA which has science questions with explanations
    dataset = load_dataset("derek-thomas/ScienceQA")
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Filter for text-only questions (no image required) and harder subjects
    # Focus on natural science questions
    def filter_hard_science(example):
        # Skip if image is required
        if example.get('image') is not None:
            return False
        
        # Must be natural science
        subject = example.get('subject', '').lower()
        if 'natural science' not in subject:
            return False
        
        # Focus on harder topics and grades
        grade = example.get('grade', '')
        topic = example.get('topic', '').lower()
        
        # Only keep middle and high school level questions (grades 6-12)
        if isinstance(grade, str):
            # Extract grade number if present
            grade_nums = [g for g in ['6', '7', '8', '9', '10', '11', '12'] if g in grade]
            if grade_nums or 'high' in grade.lower():
                return True
        
        # Skip lower grade questions even if they have advanced topics
        # (they're usually too simple despite the topic name)
        if any(g in str(grade) for g in ['1', '2', '3', '4', '5']):
            return False
            
        return False
    
    # Apply filter
    filtered_train = dataset['train'].filter(filter_hard_science)
    filtered_test = dataset['test'].filter(filter_hard_science)
    filtered_val = dataset['validation'].filter(filter_hard_science)
    
    # Combine all splits for more questions
    from datasets import concatenate_datasets
    all_questions = concatenate_datasets([filtered_train, filtered_test, filtered_val])
    
    # Shuffle the dataset to avoid any ordering bias
    all_questions = all_questions.shuffle(seed=42)
    
    # Save the filtered dataset
    save_path = "data/scienceqa_hard"
    print(f"Saving filtered ScienceQA to {save_path}...")
    
    # ScienceQA structure:
    # - question: The question text
    # - choices: List of answer choices
    # - answer: Index of correct answer
    # - hint: Hint text (if available)
    # - solution: Detailed solution/explanation
    # - subject: Subject area
    # - topic: Specific topic
    # - grade: Grade level
    
    all_questions.save_to_disk(save_path)
    
    print(f"Successfully saved {len(all_questions)} hard science questions")
    print("\nDataset structure:")
    print("- question: The question text")
    print("- choices: List of answer choices")
    print("- answer: Index of correct answer (0-based)")
    print("- solution: Detailed solution/explanation")
    print("- hint: Optional hint")
    print("- subject: Subject area")
    print("- topic: Specific topic")
    
    # Print a sample question
    if len(all_questions) > 0:
        sample = all_questions[0]
        print("\nSample question:")
        print(f"Subject: {sample.get('subject', 'N/A')}")
        print(f"Topic: {sample.get('topic', 'N/A')}")
        print(f"Question: {sample['question'][:100]}...")
        print(f"Choices: {len(sample.get('choices', []))} options")
        print(f"Has solution: {'solution' in sample and bool(sample['solution'])}")

if __name__ == "__main__":
    main()