import json
from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

RUN_NAME = "20251019_202534_qwq_gpqa"

RUNS_DIR = Path("runs")

font_path = Path("fonts/Montserrat-Regular.ttf")
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    plt.rcParams["font.family"] = "Montserrat"
plt.rcParams["hatch.linewidth"] = 1

eval_file = RUNS_DIR / RUN_NAME / "evaluation.json"

with open(eval_file) as f:
    data = json.load(f)

chunk_scores_by_position = {}

for r in data.get("results", []):
    chunks = r.get("legibility_chunks", [])
    for chunk in chunks:
        pos = chunk.get("start_pos", 0)
        score = chunk.get("score")
        if isinstance(score, (int, float)):
            if pos not in chunk_scores_by_position:
                chunk_scores_by_position[pos] = []
            chunk_scores_by_position[pos].append(score)

if not chunk_scores_by_position:
    print("No chunk data found")
    exit(1)

positions = sorted(chunk_scores_by_position.keys())
scores_list = [chunk_scores_by_position[p] for p in positions]

fig, ax = plt.subplots(figsize=(10, 6))

bp = ax.boxplot(
    scores_list,
    positions=range(len(positions)),
    patch_artist=True,
    boxprops=dict(facecolor="#3498db", color="#3498db", alpha=0.6),
    medianprops=dict(color="#3498db"),
)

ax.set_xlabel("Characters")
ax.set_ylabel("Illegibility Score")
ax.set_xticks(range(len(positions)))
ax.set_xticklabels(positions)
ax.grid(True)

plt.tight_layout()
plt.savefig("legibility_progression.pdf", dpi=300, bbox_inches="tight")
plt.savefig("legibility_progression.png", dpi=150)
print("Saved legibility_progression.pdf and legibility_progression.png")
