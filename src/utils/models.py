MODEL_REGISTRY = {
    "gpt-4o": {"provider": "openai", "model_id": "gpt-4o"},
    "gpt-4o-mini": {"provider": "openai", "model_id": "gpt-4o-mini"},
    "gpt-4-turbo": {"provider": "openai", "model_id": "gpt-4-turbo"},
    "claude-3-7-sonnet-latest": {
        "provider": "anthropic",
        "model_id": "claude-3-7-sonnet-20250219",
    },
    "claude-3-5-sonnet-latest": {
        "provider": "anthropic",
        "model_id": "claude-3-5-sonnet-20241022",
    },
    "claude-3-opus-latest": {
        "provider": "anthropic",
        "model_id": "claude-3-opus-20240229",
    },
    "R1": {
        "provider": "openrouter",
        "model_id": "deepseek/deepseek-r1",
        "openrouter_provider": ["targon/fp8", "Nebius"],
    },
    "qwq": {
        "provider": "openrouter",
        "model_id": "qwen/qwq-32b",
        "openrouter_provider": ["deepinfra/bf16", "nebius/fp8"],
    },
    "o3-mini": {"provider": "openrouter", "model_id": "openai/o3-mini"},
}


def get_model_config(model_name: str) -> dict:
    if model_name not in MODEL_REGISTRY:
        raise ValueError(
            f"Model '{model_name}' not found in registry. Available: {list(MODEL_REGISTRY.keys())}"
        )
    return MODEL_REGISTRY[model_name].copy()
