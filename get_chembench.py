"""
Download and prepare ChemBench dataset.
ChemBench is a comprehensive chemistry benchmark with questions ranging from 
general chemistry to advanced topics like quantum chemistry and materials science.
"""

from datasets import load_dataset
import os
import json

def main():
    print("Downloading ChemBench dataset from jablonkagroup/ChemBench...")
    
    # ChemBench has multiple configurations for different chemistry subfields
    configs = [
        'analytical_chemistry',
        'chemical_preference', 
        'general_chemistry',
        'inorganic_chemistry',
        'materials_science',
        'organic_chemistry',
        'physical_chemistry',
        'technical_chemistry',
        'toxicity_and_safety'
    ]
    
    print(f"Available ChemBench configurations: {configs}")
    
    # Load all configurations and combine them
    all_data = []
    
    for config in configs:
        print(f"\nLoading {config}...")
        try:
            dataset_config = load_dataset("jablonkagroup/ChemBench", config)
            # Get the first available split from this config
            splits = list(dataset_config.keys())
            if splits:
                data = dataset_config[splits[0]]
                print(f"  - Loaded {len(data)} questions from {config}")
                # Add config info to each question
                for item in data:
                    item['chem_subfield'] = config
                all_data.extend(data)
        except Exception as e:
            print(f"  - Error loading {config}: {e}")
    
    print(f"\nTotal questions loaded: {len(all_data)}")
    
    # Convert to a dataset format
    from datasets import Dataset
    dataset = Dataset.from_list(all_data)
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Filter for harder questions that require multi-step reasoning
    def filter_hard_questions(example):
        # Filter for questions that require reasoning
        # Skip trivial fact-based questions
        question_text = example.get('question', '').lower() if 'question' in example else str(example).lower()
        
        # Look for indicators of complex questions
        reasoning_indicators = [
            'calculate', 'determine', 'explain', 'derive', 'predict',
            'mechanism', 'synthesis', 'analyze', 'compare', 'design',
            'propose', 'justify', 'evaluate', 'consider the following',
            'multi-step', 'given that', 'if...then', 'assuming'
        ]
        
        # Check if question likely requires reasoning
        has_reasoning = any(indicator in question_text for indicator in reasoning_indicators)
        
        # Also keep questions with longer text (usually more complex)
        is_long = len(question_text) > 150
        
        # Prioritize certain subfields known for complexity
        complex_subfields = ['physical_chemistry', 'organic_chemistry', 'analytical_chemistry', 'materials_science']
        is_complex_field = example.get('chem_subfield', '') in complex_subfields
        
        return has_reasoning or is_long or is_complex_field
    
    print(f"\nFiltering for complex questions requiring reasoning...")
    
    # Apply filtering
    filtered_data = dataset.filter(filter_hard_questions)
    print(f"Questions after filtering: {len(filtered_data)}")
    
    # Save the dataset
    save_path = "data/chembench"
    print(f"Saving ChemBench to {save_path}...")
    
    # Expected structure (may vary):
    # - question: The question text
    # - choices: List of answer choices (if multiple choice)
    # - answer: Correct answer
    # - explanation: Detailed explanation (if available)
    # - topic: Chemistry topic
    # - difficulty: Difficulty level
    
    filtered_data.save_to_disk(save_path)
    
    print(f"Successfully saved {len(filtered_data)} chemistry questions")
    print("\nDataset structure:")
    
    # Print actual structure based on first example
    if len(filtered_data) > 0:
        sample = filtered_data[0]
        print("Fields available:")
        for key in sample.keys():
            value_type = type(sample[key]).__name__
            print(f"- {key}: {value_type}")
        
        print("\nSample question:")
        print(f"Subfield: {sample.get('chem_subfield', 'N/A')}")
        
        # Print question - handle different possible field names
        question_field = None
        for field in ['question', 'text', 'prompt', 'input']:
            if field in sample:
                question_field = field
                break
        
        if question_field:
            print(f"Question ({question_field}): {str(sample[question_field])[:200]}...")
        else:
            print(f"First text field: {str(list(sample.values())[0])[:200]}...")
        
        # Check for choices/options
        for field in ['choices', 'options', 'answers']:
            if field in sample and isinstance(sample[field], list):
                print(f"{field}: {len(sample[field])} options")
                
        # Check answer format
        for field in ['answer', 'correct_answer', 'solution', 'target']:
            if field in sample:
                print(f"{field} type: {type(sample[field]).__name__}")
                if isinstance(sample[field], str) and len(sample[field]) < 50:
                    print(f"{field} value: {sample[field]}")

if __name__ == "__main__":
    main()