from datasets import load_dataset, concatenate_datasets
from pathlib import Path


def download_gpqa(save_path: Path):
    print(f"Downloading GPQA Diamond to {save_path}...")
    dataset = load_dataset("Idavidrein/gpqa", data_files="gpqa_diamond.csv", split="train")
    dataset.save_to_disk(str(save_path))
    print(f"Saved {len(dataset)} questions")


def download_mmlu_pro(save_path: Path):
    print(f"Downloading MMLU-Pro to {save_path}...")
    dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="test")
    dataset.save_to_disk(str(save_path))
    print(f"Saved {len(dataset)} questions")


def download_scienceqa(save_path: Path):
    print(f"Downloading ScienceQA to {save_path}...")
    dataset = load_dataset("derek-thomas/ScienceQA")

    def is_hard_science(example):
        if example.get("image") is not None:
            return False
        subject = example.get("subject", "").lower()
        if "natural science" not in subject:
            return False
        grade = str(example.get("grade", ""))
        return any(g in grade for g in ["6", "7", "8", "9", "10", "11", "12", "high"])

    filtered = concatenate_datasets([
        dataset["train"].filter(is_hard_science),
        dataset["test"].filter(is_hard_science),
        dataset["validation"].filter(is_hard_science),
    ]).shuffle(seed=42)

    filtered.save_to_disk(str(save_path))
    print(f"Saved {len(filtered)} questions")


def download_chembench(save_path: Path):
    print(f"Downloading ChemBench to {save_path}...")
    configs = [
        "analytical_chemistry",
        "chemical_preference",
        "general_chemistry",
        "inorganic_chemistry",
        "materials_science",
        "organic_chemistry",
        "physical_chemistry",
        "technical_chemistry",
        "toxicity_and_safety",
    ]

    all_data = []
    for config in configs:
        try:
            dataset_config = load_dataset("jablonkagroup/ChemBench", config)
            splits = list(dataset_config.keys())
            if splits:
                data = dataset_config[splits[0]]
                for item in data:
                    item["chem_subfield"] = config
                all_data.extend(data)
        except Exception as e:
            print(f"Skipping {config}: {e}")

    from datasets import Dataset
    dataset = Dataset.from_list(all_data)
    dataset.save_to_disk(str(save_path))
    print(f"Saved {len(dataset)} questions")


DOWNLOAD_FUNCTIONS = {
    "gpqa_diamond": download_gpqa,
    "mmlu_pro": download_mmlu_pro,
    "scienceqa_hard": download_scienceqa,
    "chembench": download_chembench,
}


def download_dataset(name: str, data_dir: Path):
    dataset_path = data_dir / name
    if name not in DOWNLOAD_FUNCTIONS:
        raise ValueError(f"No download function for {name}")

    data_dir.mkdir(parents=True, exist_ok=True)
    DOWNLOAD_FUNCTIONS[name](dataset_path)
