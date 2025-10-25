import json
from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

font_path = Path("fonts/Montserrat-Medium.ttf")
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    plt.rcParams["font.family"] = "Montserrat"

run_dir = Path("runs/20251021_000418_qwq_gpqa")
eval_file = run_dir / "evaluation.json"
inference_file = run_dir / "inference.json"

with open(eval_file) as f:
    eval_data = json.load(f)

with open(inference_file) as f:
    inference_data = json.load(f)

inference_map = {}
for item in inference_data:
    key = (item.get("question_id"), item.get("sample_index", 0))
    inference_map[key] = item

results = eval_data.get("results", [])

question_data = {}
for r in results:
    qid = r.get("question_id")
    if not qid:
        continue

    if "legibility" not in r or not r["legibility"]:
        continue
    if "correctness" not in r or not r["correctness"]:
        continue

    legibility_score = r["legibility"].get("score")
    correctness = r["correctness"].get("correctness")

    sample_index = r.get("sample_index", 0)
    key = (qid, sample_index)
    inference_item = inference_map.get(key)

    if not inference_item:
        continue

    reasoning_length = (
        len(inference_item.get("reasoning", ""))
        if inference_item.get("reasoning")
        else 0
    )

    if legibility_score is None or correctness is None or reasoning_length == 0:
        continue

    normalized_score = legibility_score / (reasoning_length / 1000)

    if correctness == "correct":
        correct_val = 1
    elif correctness == "partially_correct":
        correct_val = 0.5
    else:
        correct_val = 0

    if qid not in question_data:
        question_data[qid] = {"scores": [], "correctness": []}

    question_data[qid]["scores"].append(normalized_score)
    question_data[qid]["correctness"].append(correct_val)

correlations = []
for qid, qdata in question_data.items():
    if len(set(qdata["correctness"])) > 1:
        corr = np.corrcoef(qdata["correctness"], qdata["scores"])[0, 1]
        if not np.isnan(corr):
            correlations.append(corr)

correlations.sort()

plt.rcParams.update(
    {
        "font.size": 14,
        "axes.labelsize": 16,
        "axes.titlesize": 16,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
    }
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(range(len(correlations)), correlations, alpha=0.6, s=50)
ax.axhline(y=0, color="gray", linestyle="--", linewidth=1, alpha=0.5)

mean_corr = np.mean(correlations)
ax.axhline(
    y=mean_corr,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {mean_corr:.3f}",
)

ax.set_xlabel("Questions", fontsize=18)
ax.set_ylabel("Correlation b/w Perf and Legibility", fontsize=18)
ax.legend(fontsize=14)
ax.grid(alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig(
    "/Users/jose/cot_legibility/question_correlations_normalized.pdf",
    dpi=300,
    bbox_inches="tight",
)
print("Saved question_correlations_normalized.pdf")
