#!/usr/bin/env python3
"""Test R1 API call to debug logprobs."""

import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("Testing R1 API with logprobs...")

try:
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1",
        messages=[{"role": "user", "content": "What is 2 + 2?"}],
        temperature=0.7,
        logprobs=True,
        top_logprobs=20,
    )
    
    print(f"\nResponse content: {completion.choices[0].message.content}")
    
    # Check if we have logprobs
    if hasattr(completion.choices[0], 'logprobs'):
        print(f"\nLogprobs object exists: {completion.choices[0].logprobs}")
        if completion.choices[0].logprobs:
            print(f"Logprobs type: {type(completion.choices[0].logprobs)}")
            if hasattr(completion.choices[0].logprobs, 'content'):
                print(f"Content exists: {completion.choices[0].logprobs.content is not None}")
                if completion.choices[0].logprobs.content:
                    print(f"Number of tokens: {len(completion.choices[0].logprobs.content)}")
                    # Show first token
                    first_token = completion.choices[0].logprobs.content[0]
                    print(f"\nFirst token: '{first_token.token}'")
                    print(f"First token logprob: {first_token.logprob}")
                    if first_token.top_logprobs:
                        print(f"Number of alternatives: {len(first_token.top_logprobs)}")
                else:
                    print("Content is empty")
        else:
            print("Logprobs is None/False")
    else:
        print("\nNo logprobs attribute on choice")
    
    # Check for reasoning
    if hasattr(completion.choices[0].message, 'reasoning'):
        print(f"\nReasoning exists: {completion.choices[0].message.reasoning is not None}")
        if completion.choices[0].message.reasoning:
            print(f"Reasoning preview: {completion.choices[0].message.reasoning[:100]}...")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()