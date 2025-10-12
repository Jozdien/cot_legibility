import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import re
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from src.utils.io import read_json


def setup_matplotlib(font_path="fonts/Montserrat-Regular.ttf"):
    if Path(font_path).exists():
        fm.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = "Montserrat"


def extract_reasoning_chunks(rollout_path, chunk_size=5000):
    with open(rollout_path, encoding='utf-8') as f:
        content = f.read()

    pattern = r"# DeepSeek reasoning.*?\n(.*?)(?=\n---|\n# |\Z)"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return None

    reasoning = match.group(1).strip()
    chunks = []

    for i in range(0, len(reasoning), chunk_size):
        chunks.append(reasoning[i:i + chunk_size])

    return chunks


def grade_chunks_with_grader(chunks, grader, max_chars=5000):
    grades = []
    for chunk in chunks:
        text = chunk[:max_chars] if len(chunk) > max_chars else chunk
        try:
            grade = grader.grade_legibility(text, max_chars)
            grades.append(grade.get("score", None))
        except Exception:
            grades.append(None)
    return grades


def analyze_chunk_progression(scores_path, rollouts_dir, output_path, chunk_size=5000):
    setup_matplotlib()

    from src.evaluation.grader import Grader

    data = read_json(scores_path)
    rollouts_path = Path(rollouts_dir)
    grader = Grader()

    all_chunks = {}

    for item in data:
        filename = item.get("file")
        if not filename:
            continue

        rollout_file = rollouts_path / filename
        if not rollout_file.exists():
            continue

        chunks = extract_reasoning_chunks(rollout_file, chunk_size)
        if not chunks:
            continue

        grades = grade_chunks_with_grader(chunks, grader)

        for i, grade in enumerate(grades):
            if grade is not None:
                if i not in all_chunks:
                    all_chunks[i] = []
                all_chunks[i].append(grade)

    if not all_chunks:
        print("No chunks found")
        return

    chunk_positions = sorted(all_chunks.keys())
    chunk_data = [all_chunks[i] for i in chunk_positions]

    fig, ax = plt.subplots(figsize=(12, 6))

    bp = ax.boxplot(chunk_data, positions=chunk_positions, patch_artist=True, widths=0.6)

    for box in bp["boxes"]:
        box.set(facecolor="#3498db", alpha=0.8)

    ax.set_xlabel("Chunk Position (characters)")
    ax.set_ylabel("Illegibility Score", fontsize=12)
    ax.set_title("Illegibility Progression Through Reasoning", fontsize=14)
    ax.set_ylim(0, 10)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    x_labels = [i * chunk_size for i in chunk_positions]
    ax.set_xticks(chunk_positions)
    ax.set_xticklabels(x_labels)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python plot_chunks.py <scores_file> <rollouts_dir> <output_file> [chunk_size]")
        sys.exit(1)

    scores_path = sys.argv[1]
    rollouts_dir = sys.argv[2]
    output_path = sys.argv[3]
    chunk_size = int(sys.argv[4]) if len(sys.argv) > 4 else 5000

    analyze_chunk_progression(scores_path, rollouts_dir, output_path, chunk_size)
