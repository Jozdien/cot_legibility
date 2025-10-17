import yaml
from pathlib import Path
from typing import Any

from .models import get_model_config


def load_config(config_path: str | Path) -> dict[str, Any]:
    with open(config_path) as f:
        config = yaml.safe_load(f)

    _validate_config(config)
    _set_defaults(config)
    _resolve_models(config)
    return config


def save_config(config: dict[str, Any], output_path: str | Path) -> None:
    with open(output_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)


def _validate_config(config: dict) -> None:
    required_keys = ["run"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Config missing required key: {key}")

    stages = config["run"].get("stages", [])
    if not stages:
        raise ValueError("Must specify at least one stage in run.stages")

    valid_stages = {"inference", "evaluation", "analysis", "prefill"}
    invalid = set(stages) - valid_stages
    if invalid:
        raise ValueError(f"Invalid stages: {invalid}. Must be one of {valid_stages}")

    if "inference" in stages and "inference" not in config:
        raise ValueError("inference stage specified but no inference config provided")

    if "evaluation" in stages:
        if "evaluation" not in config:
            raise ValueError("evaluation stage specified but no evaluation config provided")
        if "inference" not in stages and not config["evaluation"].get("inference_file"):
            raise ValueError("evaluation without inference requires evaluation.inference_file")

    if "analysis" in stages and "analysis" not in config:
        raise ValueError("analysis stage specified but no analysis config provided")

    if "prefill" in stages:
        if "prefill" not in config:
            raise ValueError("prefill stage specified but no prefill config provided")
        if "evaluation" not in stages and not config["prefill"].get("evaluation_file"):
            raise ValueError("prefill stage requires evaluation stage or prefill.evaluation_file")


def _set_defaults(config: dict) -> None:
    if "inference" in config:
        inf = config["inference"]
        inf.setdefault("concurrency", {}).setdefault("max_workers", 30)
        for model in inf.get("models", []):
            model.setdefault("temperature", 1.0)
            model.setdefault("include_reasoning", False)
        for dataset in inf.get("datasets", []):
            dataset.setdefault("num_questions", None)
            dataset.setdefault("shuffle", False)

    if "evaluation" in config:
        ev = config["evaluation"]
        ev.setdefault("grader_model", "claude-3-7-sonnet-latest")
        ev.setdefault("max_workers", 5)
        ev.setdefault("grade_legibility", True)
        ev.setdefault("grade_correctness", True)
        ev.setdefault("grade_legibility_chunks", False)
        ev.setdefault("chunk_size", 5000)
        ev.setdefault("max_chars_legibility", 5000)

    if "analysis" in config:
        an = config["analysis"]
        an.setdefault("plots", [])
        an.setdefault("statistics", ["summary"])
        if "comparison" not in an:
            an["comparison"] = {"enabled": False}

    if "prefill" in config:
        pf = config["prefill"]
        pf.setdefault("legibility_threshold", 7)
        pf.setdefault("include_reasoning", False)
        pf.setdefault("max_workers", 30)


def _resolve_models(config: dict) -> None:
    if "inference" in config:
        for model in config["inference"].get("models", []):
            if "provider" not in model and "model_id" not in model:
                registry_config = get_model_config(model["name"])
                model.update(registry_config)
