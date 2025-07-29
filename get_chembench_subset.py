"""
Download specific subsets of ChemBench dataset.
Useful if you want to focus on particular chemistry subfields.
"""

from datasets import load_dataset
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Download specific ChemBench subsets")
    parser.add_argument("--configs", nargs="+", 
                       choices=['analytical_chemistry', 'chemical_preference', 'general_chemistry',
                               'inorganic_chemistry', 'materials_science', 'organic_chemistry',
                               'physical_chemistry', 'technical_chemistry', 'toxicity_and_safety'],
                       help="Specific configurations to download")
    parser.add_argument("--output", type=str, default="data/chembench_subset",
                       help="Output directory name")
    args = parser.parse_args()
    
    # Use all configs if none specified
    configs = args.configs or [
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
    
    print(f"Downloading ChemBench subsets: {configs}")
    
    all_data = []
    
    for config in configs:
        print(f"\nLoading {config}...")
        try:
            dataset_config = load_dataset("jablonkagroup/ChemBench", config)
            splits = list(dataset_config.keys())
            if splits:
                data = dataset_config[splits[0]]
                print(f"  - Loaded {len(data)} questions from {config}")
                for item in data:
                    item['chem_subfield'] = config
                all_data.extend(data)
        except Exception as e:
            print(f"  - Error loading {config}: {e}")
    
    print(f"\nTotal questions loaded: {len(all_data)}")
    
    # Convert to dataset and save
    from datasets import Dataset
    dataset = Dataset.from_list(all_data)
    
    os.makedirs("data", exist_ok=True)
    dataset.save_to_disk(args.output)
    
    print(f"Saved to {args.output}")
    
    # Print sample
    if len(all_data) > 0:
        print("\nSample question:")
        sample = all_data[0]
        for key, value in sample.items():
            if isinstance(value, str) and len(value) > 100:
                print(f"{key}: {value[:100]}...")
            else:
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()