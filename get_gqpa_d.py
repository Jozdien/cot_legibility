from datasets import load_dataset
import os

# Create directory if it doesn't exist
os.makedirs("data/gpqa_diamond", exist_ok=True)

# Download the dataset
dataset = load_dataset("Idavidrein/gpqa", data_files="gpqa_diamond.csv", split="train")

# Save dataset locally
dataset.save_to_disk("data/gpqa_diamond")

# To load it back later:
from datasets import load_from_disk
loaded_dataset = load_from_disk("data/gpqa_diamond")
print(f"Dataset contains {len(loaded_dataset)} questions")

# Simple query function
def query_by_keyword(keyword):
    return [item for item in loaded_dataset if keyword.lower() in item['question'].lower()]