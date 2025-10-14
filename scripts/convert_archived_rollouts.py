import argparse
import re
from datetime import datetime, UTC
from pathlib import Path

from dotenv import load_dotenv

from src.inference.datasets import Dataset
from src.utils.config import save_config
from src.utils.io import ensure_dir, write_json
from src.utils.logging import get_logger, setup_logging

load_dotenv()


def parse_markdown_file(md_path: Path) -> dict:
    content = md_path.read_text(encoding="utf-8")

    sections = {}

    question_match = re.search(
        r"# Original Question\s+(.*?)(?=---|\Z)", content, re.DOTALL
    )
    if question_match:
        sections["question"] = question_match.group(1).strip()

    answer_match = re.search(
        r"# [\w\-]+ response.*?\n+(.*?)(?=---|\n#|\Z)", content, re.DOTALL
    )
    if answer_match:
        sections["answer"] = answer_match.group(1).strip()

    reasoning_match = re.search(
        r"# [\w\-]+ reasoning.*?\n+(.*?)(?=---|\n#|\Z)", content, re.DOTALL
    )
    if reasoning_match:
        sections["reasoning"] = reasoning_match.group(1).strip()

    filename_seq_match = re.search(r"_(\d{4})_", md_path.name)
    if filename_seq_match:
        sections["sequence"] = int(filename_seq_match.group(1))

    return sections


def infer_config_from_dirname(dirname: str) -> dict:
    parts = dirname.lower()

    dataset = None
    if "chembench" in parts:
        dataset = "chembench"
    elif "mmlu_pro" in parts:
        dataset = "mmlu_pro"
    elif "gpqa" in parts:
        dataset = "gpqa"
    elif "scienceqa" in parts:
        dataset = "scienceqa"

    if "r1_zero" in parts or "r1-zero" in parts:
        model = "R1-Zero"
    else:
        cleaned = parts
        for ds in ["chembench", "mmlu_pro", "gpqa", "scienceqa"]:
            cleaned = cleaned.replace(f"{ds}_", "")

        cleaned = re.sub(r"_temp.*", "", cleaned)
        cleaned = re.sub(r"_only", "", cleaned)
        cleaned = re.sub(r"_test.*", "", cleaned)
        cleaned = re.sub(r"^test_", "", cleaned)
        cleaned = cleaned.strip("_")

        model = cleaned if cleaned else "r1"

    temp_match = re.search(r"temp[_\s]+([\d.]+)", parts)
    temperature = float(temp_match.group(1)) if temp_match else 1.0

    return {"dataset": dataset, "model": model, "temperature": temperature}


def normalize_text(text: str) -> str:
    return " ".join(text.split()).lower()


def match_question_with_dataset(
    question_text: str, all_questions: list, sequence: int = None
) -> dict:
    question_norm = normalize_text(question_text)

    if sequence is not None and 1 <= sequence <= len(all_questions):
        candidate = all_questions[sequence - 1]
        candidate_norm = normalize_text(candidate["question"])
        if (
            question_norm[:200] in candidate_norm
            or candidate_norm[:200] in question_norm
        ):
            return candidate

    for q in all_questions:
        q_norm = normalize_text(q["question"])
        if len(q_norm) > 50 and len(question_norm) > 50:
            if q_norm[:100] in question_norm or question_norm[:100] in q_norm:
                return q

    return None


def convert_rollouts_to_inference(
    archive_subdir: Path, output_dir: Path, config_info: dict, logger
) -> None:
    logger.info(f"Converting rollouts from {archive_subdir}")

    try:
        dataset = Dataset(config_info["dataset"])
        dataset.load()
        all_questions = list(dataset.get_questions(num_questions=None, shuffle=False))
    except Exception as e:
        logger.error(f"Could not load dataset using normal method: {e}")
        logger.info("Attempting to load dataset using pyarrow directly")
        import pyarrow as pa

        arrow_file = Path(f"data/{config_info['dataset']}/data-00000-of-00001.arrow")
        if not arrow_file.exists():
            arrow_file = Path(
                f"data/{config_info['dataset']}_diamond/data-00000-of-00001.arrow"
            )

        if arrow_file.exists():
            with pa.memory_map(str(arrow_file), "r") as source:
                try:
                    table = pa.ipc.open_file(source).read_all()
                except Exception:
                    source.seek(0)
                    table = pa.ipc.open_stream(source).read_all()
            all_questions = []
            for i in range(table.num_rows):
                row = {col: table[col][i].as_py() for col in table.column_names}

                if config_info["dataset"] == "chembench":
                    question_text = (
                        row.get("examples", [{}])[0].get("input", "")
                        if row.get("examples")
                        else ""
                    )
                    answer = (
                        row.get("examples", [{}])[0].get("target", "")
                        if row.get("examples")
                        else ""
                    )
                    all_questions.append(
                        {
                            "question_id": f"chembench_{i}",
                            "question": question_text,
                            "correct_answer": answer,
                            "dataset": "chembench",
                        }
                    )
            logger.info(f"Loaded {len(all_questions)} questions from arrow file")
        else:
            logger.error(f"Could not find arrow file at {arrow_file}")
            raise

    md_files = sorted(archive_subdir.glob("*.md"))
    logger.info(f"Found {len(md_files)} markdown files")

    inference_data = []
    matched_count = 0
    question_id_counts = {}

    for i, md_file in enumerate(md_files):
        parsed = parse_markdown_file(md_file)

        if not parsed.get("question"):
            logger.warning(f"No question found in {md_file.name}, skipping")
            continue

        matched_q = match_question_with_dataset(
            parsed["question"], all_questions, parsed.get("sequence")
        )

        if matched_q:
            question_id = matched_q["question_id"]
            correct_answer = matched_q.get("correct_answer")
            question_text = matched_q["question"]
            matched_count += 1
        else:
            question_id = f"{config_info['dataset']}_{i}"
            correct_answer = None
            question_text = parsed.get("question", "")
            logger.warning(
                f"Could not match question in {md_file.name}, using fallback ID {question_id}"
            )

        sample_index = question_id_counts.get(question_id, 0)
        question_id_counts[question_id] = sample_index + 1

        record = {
            "question_id": question_id,
            "question": question_text,
            "answer": parsed.get("answer", ""),
            "reasoning": parsed.get("reasoning", ""),
            "correct_answer": correct_answer,
            "dataset": config_info["dataset"],
            "sample_index": sample_index,
            "model": config_info["model"],
            "temperature": config_info["temperature"],
            "timestamp": datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
            "metadata": {
                "source": "archive_conversion",
                "original_file": md_file.name,
                "duration_ms": 0,
            },
        }

        inference_data.append(record)

    inference_file = output_dir / "inference.json"
    write_json(inference_file, inference_data)
    logger.info(f"Wrote {len(inference_data)} records to {inference_file}")
    logger.info(
        f"Successfully matched {matched_count}/{len(inference_data)} questions with dataset"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Convert archived rollouts to evaluated runs"
    )
    parser.add_argument(
        "subdir", type=str, help="Subdirectory name inside archive/r1_rollouts/"
    )
    args = parser.parse_args()

    archive_dir = Path("archive/r1_rollouts") / args.subdir
    if not archive_dir.exists():
        print(f"Error: {archive_dir} does not exist")
        return 1

    config_info = infer_config_from_dirname(args.subdir)

    if not config_info["dataset"]:
        print(
            f"\033[1m⚠️  WARNING: Could not infer dataset from directory name '{args.subdir}'\033[0m"
        )
        print("\033[1m⚠️  Defaulting to 'gpqa' dataset\033[0m")
        print(
            "\033[1mDirectory name should contain one of: chembench, mmlu_pro, gpqa, scienceqa\033[0m"
        )
        config_info["dataset"] = "gpqa"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_name = f"{timestamp}_{config_info['model']}_{config_info['dataset']}"
    output_dir = ensure_dir(Path("runs") / run_name)

    setup_logging(output_dir / "run.log")
    logger = get_logger(__name__)

    logger.info(f"Converting archived rollouts: {args.subdir}")
    logger.info(f"Inferred config: {config_info}")
    logger.info(f"Output directory: {output_dir}")

    config = {
        "run": {"name": run_name, "stages": ["evaluation", "analysis"]},
        "evaluation": {
            "inference_file": str(output_dir / "inference.json"),
            "grader_model": "gpt-4o",
            "grade_legibility": True,
            "grade_correctness": True,
            "max_workers": 100,
            "max_chars_legibility": 5000,
        },
        "analysis": {
            "comparison": {"enabled": False},
            "plots": [
                "legibility_scores_boxplot",
                "correctness_assessment",
                "legibility_by_correctness",
                "length_vs_legibility",
            ],
            "statistics": ["summary"],
        },
    }

    save_config(config, output_dir / "config.yaml")

    try:
        convert_rollouts_to_inference(archive_dir, output_dir, config_info, logger)

        logger.info(
            f"\nConversion complete! Inference data written to: {output_dir}/inference.json"
        )
        logger.info("Starting evaluation and analysis...")

        from src.main import main as run_pipeline

        run_pipeline(str(output_dir / "config.yaml"))

        return 0

    except Exception as e:
        logger.error(f"Error during conversion: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    exit(main())
