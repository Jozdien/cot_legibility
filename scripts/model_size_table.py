import json
from pathlib import Path
import numpy as np

MODEL_SIZES = {
    "R1-Distill-Qwen-14B": "14B",
    "R1-Distill-Qwen-32B": "32B",
    "qwq": "32B",
    "R1": "70B (estimated)",
    "R1-Zero": "70B (estimated)",
    "Qwen3 235B": "235B",
    "claude-3-7-sonnet-latest": "Unknown",
    "claude-sonnet-4-5": "Unknown",
    "claude-sonnet-4": "Unknown",
    "claude-opus-4": "Unknown",
    "claude-opus-4-1": "Unknown",
    "claude-haiku-4-5": "Unknown",
    "Kimi K2": "Unknown",
    "Kimi K2 0905": "Unknown",
    "gpt-4o": "Unknown",
}

def get_model_stats():
    runs_dir = Path("/Users/jose/cot_legibility/runs")
    eval_files = list(runs_dir.glob("*/evaluation.json"))

    model_scores = {}

    for ef in eval_files:
        with open(ef) as f:
            data = json.load(f)

        results = data.get("results", [])
        if not results:
            continue

        model = results[0].get("model")
        if not model:
            dir_name = ef.parent.name
            parts = dir_name.split("_")
            if len(parts) >= 3:
                model = "_".join(parts[2:]).replace("_gpqa", "").replace("_chembench", "").replace("_mmlu_pro", "")
            else:
                continue

        scores = []
        for r in results:
            if "legibility" in r and r["legibility"]:
                score = r["legibility"].get("score")
                if score is not None:
                    scores.append(score)

        if scores:
            if model not in model_scores:
                model_scores[model] = []
            model_scores[model].extend(scores)

    print("Model Statistics for Table:")
    print("="*70)
    print(f"{'Model':<35} {'Size':<15} {'Legibility':<20}")
    print("="*70)

    results = []
    for model in model_scores.keys():
        size = MODEL_SIZES.get(model, "Unknown")
        scores = model_scores[model]
        mean = np.mean(scores)
        std = np.std(scores)
        results.append((model, size, mean, std))

    results.sort(key=lambda x: (x[2]))

    for model, size, mean, std in results:
        legib_str = f"{mean:.2f} ± {std:.2f}"
        print(f"{model:<35} {size:<15} {legib_str:<20}")

if __name__ == "__main__":
    get_model_stats()
