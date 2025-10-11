import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from .utils.config import load_config
from .utils.io import ensure_dir
from .utils.logging import get_logger, setup_logging

load_dotenv()


def generate_run_name(config: dict, model_name: str | None = None, dataset_name: str | None = None) -> str:
    if config["run"].get("name"):
        return config["run"]["name"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if model_name and dataset_name:
        return f"{timestamp}_{model_name}_{dataset_name}"
    elif config["run"]["stages"] == ["analysis"]:
        return f"{timestamp}_analysis"
    else:
        return f"{timestamp}_run"


def run_inference(config: dict, output_dir: Path, logger) -> None:
    from .inference.runner import run_inference_stage

    logger.info("Starting inference stage")
    run_inference_stage(config["inference"], output_dir, logger)
    logger.info("Inference stage complete")


def run_evaluation(config: dict, output_dir: Path, logger) -> None:
    from .evaluation.grader import run_evaluation_stage

    logger.info("Starting evaluation stage")
    run_evaluation_stage(config["evaluation"], output_dir, logger)
    logger.info("Evaluation stage complete")


def run_analysis(config: dict, output_dir: Path, logger) -> None:
    from .analysis.plots import run_analysis_stage

    logger.info("Starting analysis stage")
    run_analysis_stage(config["analysis"], output_dir, logger)
    logger.info("Analysis stage complete")


def main(config_path: str) -> None:
    config = load_config(config_path)
    stages = config["run"]["stages"]

    if stages == ["analysis"] and config["analysis"]["comparison"]["enabled"]:
        run_name = generate_run_name(config)
        output_dir = ensure_dir(Path("runs") / run_name)
        setup_logging(output_dir / "run.log")
        logger = get_logger(__name__)

        logger.info(f"Starting analysis-only run: {run_name}")
        logger.info(f"Config: {config_path}")
        run_analysis(config, output_dir, logger)
        logger.info(f"Analysis complete. Results in {output_dir}")
        return

    if "inference" in stages:
        models = config["inference"]["models"]
        datasets = config["inference"]["datasets"]

        for model in models:
            for dataset in datasets:
                run_name = generate_run_name(config, model["name"], dataset["name"])
                output_dir = ensure_dir(Path("runs") / run_name)
                setup_logging(output_dir / "run.log")
                logger = get_logger(__name__)

                logger.info(f"Starting run: {run_name}")
                logger.info(f"Config: {config_path}")
                logger.info(f"Model: {model['name']}, Dataset: {dataset['name']}")

                model_config = {"models": [model], "datasets": [dataset], "concurrency": config["inference"]["concurrency"]}

                if "inference" in stages:
                    run_inference({"inference": model_config}, output_dir, logger)

                if "evaluation" in stages:
                    run_evaluation(config, output_dir, logger)

                if "analysis" in stages:
                    run_analysis(config, output_dir, logger)

                logger.info(f"Run complete. Results in {output_dir}")
    else:
        run_name = generate_run_name(config)
        output_dir = ensure_dir(Path("runs") / run_name)
        setup_logging(output_dir / "run.log")
        logger = get_logger(__name__)

        logger.info(f"Starting run: {run_name}")
        logger.info(f"Config: {config_path}")

        if "evaluation" in stages:
            run_evaluation(config, output_dir, logger)

        if "analysis" in stages:
            run_analysis(config, output_dir, logger)

        logger.info(f"Run complete. Results in {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m src.main <config_path>")
        sys.exit(1)

    main(sys.argv[1])
