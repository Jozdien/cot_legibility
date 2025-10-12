import sys
import re
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.utils.io import read_json


def extract_reasoning_from_rollout(rollout_path, pattern=r"# DeepSeek reasoning.*?\n(.*?)(?=\n---|\n# |\Z)"):
    with open(rollout_path, encoding='utf-8') as f:
        content = f.read()

    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def get_cot_word_count(rollout_path):
    reasoning = extract_reasoning_from_rollout(rollout_path)
    return len(reasoning.split()) if reasoning else None


def get_cot_char_count(rollout_path):
    reasoning = extract_reasoning_from_rollout(rollout_path)
    return len(reasoning) if reasoning else None


def add_lengths_to_scores(scores_path, rollouts_dir, output_path=None):
    data = read_json(scores_path)
    rollouts_path = Path(rollouts_dir)

    for item in data:
        filename = item.get("file")
        if not filename:
            continue

        rollout_file = rollouts_path / filename
        if not rollout_file.exists():
            continue

        word_count = get_cot_word_count(rollout_file)
        char_count = get_cot_char_count(rollout_file)

        if "cot_length" not in item:
            item["cot_length"] = {}

        item["cot_length"]["words"] = word_count
        item["cot_length"]["chars"] = char_count

    if output_path:
        from src.utils.io import write_json
        write_json(output_path, data)

    return data


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_cot_length.py <scores_file> <rollouts_dir> [output_file]")
        sys.exit(1)

    scores_path = sys.argv[1]
    rollouts_dir = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else None

    data = add_lengths_to_scores(scores_path, rollouts_dir, output_path)

    lengths = [item["cot_length"]["words"] for item in data if "cot_length" in item and item["cot_length"]["words"]]
    if lengths:
        import numpy as np
        print("\nCoT Length Statistics (words):")
        print(f"  Mean: {np.mean(lengths):.0f}")
        print(f"  Median: {np.median(lengths):.0f}")
        print(f"  Min: {np.min(lengths):.0f}")
        print(f"  Max: {np.max(lengths):.0f}")
