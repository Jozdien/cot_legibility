import os
import time
from abc import ABC, abstractmethod
from openai import OpenAI


class Provider(ABC):
    @abstractmethod
    def generate(self, question: str, model_config: dict, prefill: str | None = None) -> dict:
        pass


class OpenRouterProvider(Provider):
    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment")

        import httpx
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            timeout=600.0,
            http_client=httpx.Client(
                event_hooks={
                    "response": [self._log_response]
                }
            )
        )
        self.last_response_text = None

    def _log_response(self, response):
        self.last_response_text = response.text

    def generate(self, question: str, model_config: dict, prefill: str | None = None) -> dict:
        start_time = time.time()

        extra_body = {}
        if model_config.get("include_reasoning"):
            reasoning_config = {}
            if "reasoning_effort" in model_config:
                reasoning_config["effort"] = model_config["reasoning_effort"]
            if "reasoning_budget_tokens" in model_config:
                reasoning_config["max_tokens"] = model_config["reasoning_budget_tokens"]
            if reasoning_config:
                extra_body["reasoning"] = reasoning_config
            else:
                extra_body["include_reasoning"] = True

        if "openrouter_provider" in model_config:
            provider_config = model_config["openrouter_provider"]
            if isinstance(provider_config, str):
                extra_body["provider"] = {"order": [provider_config], "allow_fallbacks": False}
            elif isinstance(provider_config, list):
                extra_body["provider"] = {"order": provider_config, "allow_fallbacks": False}
            elif isinstance(provider_config, dict):
                extra_body["provider"] = provider_config

        messages = [{"role": "user", "content": question}]
        if prefill:
            messages.append({"role": "assistant", "content": f"<think>\n{prefill}\n</think>"})

        kwargs = {
            "model": model_config["model_id"],
            "messages": messages,
            "temperature": model_config.get("temperature", 1.0),
            "extra_body": extra_body,
        }
        if "max_tokens" in model_config:
            kwargs["max_tokens"] = model_config["max_tokens"]

        try:
            completion = self.client.chat.completions.create(**kwargs)
        except Exception as e:
            error_details = {
                "error_type": type(e).__name__,
                "error_message": str(e),
                "model": model_config["model_id"],
                "temperature": model_config.get("temperature"),
            }

            if self.last_response_text:
                error_details["response_body_start"] = self.last_response_text[:1000]
                error_details["response_body_end"] = self.last_response_text[-1000:]
                error_details["response_length"] = len(self.last_response_text)

            if hasattr(e, 'response'):
                try:
                    error_details["status_code"] = e.response.status_code
                    error_details["response_headers"] = dict(e.response.headers)
                except Exception:
                    pass

            if hasattr(e, 'body'):
                try:
                    error_details["error_body"] = str(e.body)[:1000]
                except Exception:
                    pass

            import json
            error_msg = f"OpenRouter API error: {json.dumps(error_details, indent=2)}"
            raise Exception(error_msg)

        duration_ms = int((time.time() - start_time) * 1000)

        answer = completion.choices[0].message.content or ""
        reasoning = getattr(completion.choices[0].message, "reasoning", None)

        result = {"answer": answer, "duration_ms": duration_ms}

        if reasoning:
            result["reasoning"] = reasoning

        if hasattr(completion, "usage"):
            result["tokens"] = completion.usage.total_tokens

        if hasattr(completion, "model"):
            result["provider_model"] = completion.model

        if hasattr(completion, "provider"):
            result["openrouter_provider"] = completion.provider

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

    def generate(self, question: str, model_config: dict, prefill: str | None = None) -> dict:
        start_time = time.time()

        if self.provider_name == "anthropic":
            thinking_config = {}
            if model_config.get("include_reasoning"):
                default_max_tokens = 16000
                reasoning_budget = model_config.get("reasoning_budget_tokens", 10000)
                thinking_config["thinking"] = {"type": "enabled", "budget_tokens": reasoning_budget}
            else:
                default_max_tokens = 4096

            max_tokens = model_config.get("max_tokens", default_max_tokens)

            messages = [{"role": "user", "content": question}]
            if prefill:
                messages.append({"role": "assistant", "content": f"<think>\n{prefill}\n</think>"})

            response = self.client.messages.create(
                model=model_config["model_id"],
                max_tokens=max_tokens,
                temperature=model_config.get("temperature", 1.0),
                messages=messages,
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
            messages = [{"role": "user", "content": question}]
            if prefill:
                messages.append({"role": "assistant", "content": f"<think>\n{prefill}\n</think>"})

            kwargs = {
                "model": model_config["model_id"],
                "messages": messages,
                "temperature": model_config.get("temperature", 1.0),
            }
            if "max_tokens" in model_config:
                kwargs["max_tokens"] = model_config["max_tokens"]

            response = self.client.chat.completions.create(**kwargs)
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
