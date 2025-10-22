MODEL_REGISTRY = {
    "gpt-4o": {"provider": "openai", "model_id": "gpt-4o"},
    "gpt-4o-mini": {"provider": "openai", "model_id": "gpt-4o-mini"},
    "gpt-4-turbo": {"provider": "openai", "model_id": "gpt-4-turbo"},
    "claude-sonnet-4-5": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-5-20250929",
    },
    "claude-sonnet-4": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-20250514",
    },
    "claude-opus-4": {
        "provider": "anthropic",
        "model_id": "claude-opus-4-20250514",
    },
    "claude-opus-4-1": {
        "provider": "anthropic",
        "model_id": "claude-opus-4-1-20250805",
    },
    "claude-haiku-4-5": {
        "provider": "anthropic",
        "model_id": "claude-haiku-4-5-20251001",
    },
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
        "openrouter_provider": ["targon/fp8", "Nebius", "deepinfra/base"],
    },
    "qwq": {
        "provider": "openrouter",
        "model_id": "qwen/qwq-32b",
        "openrouter_provider": ["deepinfra/bf16", "nebius/fp8"],
    },
    "Qwen3 235B": {
        "provider": "openrouter",
        "model_id": "qwen/qwen3-235b-a22b-thinking-2507",
        "openrouter_provider": ["chutes/bf16"],
    },
    "Kimi K2": {
        "provider": "openrouter",
        "model_id": "moonshotai/kimi-k2",
        "openrouter_provider": ["novita/fp8", "moonshotai/fp8"],
    },
    "Kimi K2 0905": {
        "provider": "openrouter",
        "model_id": "moonshotai/kimi-k2-0905",
        "openrouter_provider": ["chutes/fp8"],
    },
    "R1-Distill-Llama-70B": {
        "provider": "openrouter",
        "model_id": "deepseek/deepseek-r1-distill-llama-70b",
        "openrouter_provider": ["chutes/bf16", "deepinfra/fp8"],
    },
    "R1-Distill-Qwen-32B": {
        "provider": "openrouter",
        "model_id": "deepseek/deepseek-r1-distill-qwen-32b",
        "openrouter_provider": [],
    },
    "R1-Distill-Qwen-14B": {
        "provider": "openrouter",
        "model_id": "deepseek/deepseek-r1-distill-qwen-14b",
        "openrouter_provider": [],
    },
    "o3-mini": {"provider": "openrouter", "model_id": "openai/o3-mini"},
}


def get_model_config(model_name: str) -> dict:
    if model_name not in MODEL_REGISTRY:
        raise ValueError(
            f"Model '{model_name}' not found in registry. Available: {list(MODEL_REGISTRY.keys())}"
        )
    return MODEL_REGISTRY[model_name].copy()
