from datasets import load_from_disk
from pathlib import Path
from typing import Iterator
import random
import json
from .download import download_dataset


class Dataset:
    def __init__(self, name: str, data_dir: str = "data"):
        self.name = name
        self.data_dir = Path(data_dir)
        self._data = None

    def load(self) -> None:
        dataset_map = {
            "gpqa": "gpqa_diamond",
            "mmlu_pro": "mmlu_pro",
            "scienceqa": "scienceqa_hard",
            "chembench": "chembench",
        }

        if self.name not in dataset_map:
            raise ValueError(f"Unknown dataset: {self.name}. Choose from {list(dataset_map.keys())}")

        dataset_path = self.data_dir / dataset_map[self.name]
        if not dataset_path.exists():
            print(f"Dataset not found at {dataset_path}, downloading...")
            download_dataset(dataset_map[self.name], self.data_dir)

        self._data = load_from_disk(str(dataset_path))

    def get_questions(self, num_questions: int | None = None, shuffle: bool = False) -> Iterator[dict]:
        if self._data is None:
            self.load()

        indices = list(range(len(self._data)))
        if shuffle:
            random.shuffle(indices)

        if num_questions is not None:
            indices = indices[:num_questions]

        for idx in indices:
            item = self._data[idx]
            yield self._format_question(idx, item)

    def _format_question(self, idx: int, item: dict) -> dict:
        if self.name == "gpqa":
            return {
                "question_id": f"gpqa_{idx}",
                "question": item["Question"],
                "correct_answer": item.get("Correct Answer"),
                "dataset": "gpqa",
            }
        elif self.name == "mmlu_pro":
            options = "\n".join([f"{chr(65+i)}. {opt}" for i, opt in enumerate(item.get("options", []))])
            return {
                "question_id": f"mmlu_pro_{idx}",
                "question": f"{item['question']}\n\n{options}",
                "correct_answer": item.get("answer"),
                "dataset": "mmlu_pro",
            }
        elif self.name == "scienceqa":
            question_text = item.get("question", "")
            if "choices" in item and item["choices"]:
                options = "\n".join([f"{chr(65+i)}. {choice}" for i, choice in enumerate(item["choices"])])
                question_text = f"{question_text}\n\n{options}"

            return {
                "question_id": f"scienceqa_{idx}",
                "question": question_text,
                "correct_answer": item.get("answer"),
                "dataset": "scienceqa",
            }
        elif self.name == "chembench":
            examples = item.get("examples", [])
            if examples and len(examples) > 0:
                question_text = examples[0].get("input", "")
                correct_answer = examples[0].get("target", "")

                if not correct_answer:
                    target_scores = examples[0].get("target_scores", "")
                    if target_scores:
                        scores_dict = json.loads(target_scores)
                        for answer, score in scores_dict.items():
                            if score == 1.0:
                                correct_answer = answer
                                break
            else:
                question_text = ""
                correct_answer = ""

            return {
                "question_id": f"chembench_{idx}",
                "question": question_text,
                "correct_answer": correct_answer,
                "dataset": "chembench",
            }

        return {"question_id": f"{self.name}_{idx}", "question": str(item), "dataset": self.name}
