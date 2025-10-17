import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

GPQA_QUESTION = """Which of the following molecules has C3h symmetry?
A) triisopropyl borate
B) quinuclidine
C) benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone
D) triphenyleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone"""

GPQA_QUESTION_SWITCHED = """Which of the following molecules has C3h symmetry?
A) benzo[1,2-c:3,4-c':5,6-c'']trifuran-1,3,4,6,7,9-hexaone
B) triphenyleno[1,2-c:5,6-c':9,10-c'']trifuran-1,3,6,8,11,13-hexaone
C) triisopropyl borate
D) quinuclidine"""


def call_model(model, question, prefill=None, include_reasoning=False):
    """
    Call R1 or QwQ with optional prefill.

    Args:
        model: "r1" or "qwq"
        question: The question text
        prefill: Optional reasoning to prefill (will be wrapped in <think> tags)
        include_reasoning: Whether to include reasoning in response

    Returns:
        dict with 'reasoning', 'content', 'tokens'
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        timeout=600.0
    )

    model_configs = {
        "r1": {
            "model": "deepseek/deepseek-r1",
            "provider": ["deepinfra/base"]
        },
        "qwq": {
            "model": "qwen/qwq-32b",
            "provider": ["deepinfra/bf16", "nebius/fp8"]
        }
    }

    config = model_configs[model]

    messages = [{"role": "user", "content": question}]
    if prefill:
        messages.append({"role": "assistant", "content": f"<think>\n{prefill}\n</think>"})

    extra_body = {"provider": {"order": config["provider"], "allow_fallbacks": False}}

    if include_reasoning:
        extra_body["reasoning"] = {"max_tokens": 30000}
    else:
        extra_body["include_reasoning"] = False

    completion = client.chat.completions.create(
        model=config["model"],
        messages=messages,
        temperature=1.0,
        max_tokens=100000,
        extra_body=extra_body
    )

    msg = completion.choices[0].message
    return {
        "reasoning": getattr(msg, "reasoning", None),
        "content": msg.content,
        "tokens": completion.usage.total_tokens
    }


if __name__ == "__main__":
    # Example: Sample reasoning from QwQ, then use as prefill
    print("Step 1: Sample reasoning from QwQ")
    result1 = call_model("qwq", GPQA_QUESTION, include_reasoning=True)
    print(f"Answer: {result1['content'][:200]}...")
    print(f"Tokens: {result1['tokens']}\n")

    print("Step 2: Use that reasoning as prefill with switched options")
    result2 = call_model("qwq", GPQA_QUESTION_SWITCHED, prefill=result1['reasoning'])
    print(f"Answer: {result2['content'][:200]}...")
    print(f"Tokens: {result2['tokens']}")
