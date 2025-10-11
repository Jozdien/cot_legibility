import os
import time
from abc import ABC, abstractmethod
from openai import OpenAI


class Provider(ABC):
    @abstractmethod
    def generate(self, question: str, model_config: dict) -> dict:
        pass


class OpenRouterProvider(Provider):
    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment")
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    def generate(self, question: str, model_config: dict) -> dict:
        start_time = time.time()

        extra_body = {}
        if model_config.get("include_reasoning"):
            extra_body["include_reasoning"] = True

        completion = self.client.chat.completions.create(
            model=model_config["model_id"],
            messages=[{"role": "user", "content": question}],
            temperature=model_config.get("temperature", 1.0),
            extra_body=extra_body,
        )

        duration_ms = int((time.time() - start_time) * 1000)

        answer = completion.choices[0].message.content or ""
        reasoning = getattr(completion.choices[0].message, "reasoning", None)

        result = {"answer": answer, "duration_ms": duration_ms}

        if reasoning:
            result["reasoning"] = reasoning

        if hasattr(completion, "usage"):
            result["tokens"] = completion.usage.total_tokens

        return result


class DirectAPIProvider(Provider):
    def __init__(self, provider_name: str):
        self.provider_name = provider_name
        if provider_name == "anthropic":
            import anthropic

            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in environment")
            self.client = anthropic.Anthropic(api_key=api_key)
        elif provider_name == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment")
            self.client = OpenAI(api_key=api_key)
        else:
            raise ValueError(f"Unknown provider: {provider_name}")

    def generate(self, question: str, model_config: dict) -> dict:
        start_time = time.time()

        if self.provider_name == "anthropic":
            thinking_config = {}
            max_tokens = 16000
            if model_config.get("include_reasoning"):
                thinking_config["thinking"] = {"type": "enabled", "budget_tokens": 10000}
            else:
                max_tokens = 4096

            response = self.client.messages.create(
                model=model_config["model_id"],
                max_tokens=max_tokens,
                temperature=model_config.get("temperature", 1.0),
                messages=[{"role": "user", "content": question}],
                **thinking_config,
            )

            answer = ""
            reasoning = ""
            for block in response.content:
                if block.type == "thinking":
                    reasoning += block.thinking
                elif block.type == "text":
                    answer += block.text

            tokens = response.usage.input_tokens + response.usage.output_tokens
        else:
            response = self.client.chat.completions.create(
                model=model_config["model_id"],
                messages=[{"role": "user", "content": question}],
                temperature=model_config.get("temperature", 1.0),
            )
            answer = response.choices[0].message.content or ""
            tokens = response.usage.total_tokens if hasattr(response, "usage") else None

        duration_ms = int((time.time() - start_time) * 1000)

        result = {"answer": answer, "duration_ms": duration_ms}
        if self.provider_name == "anthropic" and reasoning:
            result["reasoning"] = reasoning
        if tokens:
            result["tokens"] = tokens

        return result


def get_provider(provider_name: str) -> Provider:
    if provider_name == "openrouter":
        return OpenRouterProvider()
    elif provider_name in ["anthropic", "openai"]:
        return DirectAPIProvider(provider_name)
    else:
        raise ValueError(f"Unknown provider: {provider_name}")
