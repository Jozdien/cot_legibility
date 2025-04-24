from datasets import load_from_disk

# Load the dataset from disk
dataset = load_from_disk("../data/gpqa_diamond")

# Basic info
print(f"Dataset contains {len(dataset)} questions")
print(f"Fields: {dataset.column_names}")

# Access data examples
print(f"First question: {dataset[0]['Question']}")
print(f"First question's answer: {dataset[0]['Correct Answer']}")

# Slice and dice
subset = dataset.select(range(10))  # Get first 10 examples
print(f"Subset size: {len(subset)}")

# Filter examples
physics_questions = dataset.filter(lambda example: "Physics" in example["High-level domain"].lower())
print(f"Physics questions count: {len(physics_questions)}")

# Convert to pandas if needed
df = dataset.to_pandas()
print(f"Pandas DataFrame shape: {df.shape}")