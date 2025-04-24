import os

dir = "../r1_rollouts/cutoff_0.25_deepseek_openrouter"

for file in os.listdir(dir):
    with open(os.path.join(dir, file), 'r') as f:
        content = f.read()
        if "DeepSeek response (via deepseek)" in content:
            deepseek_response = content.split("DeepSeek response (via deepseek)\n\n")[1].split("\n\n---\n\n# DeepSeek reasoning")[0]
        elif "DeepSeek response (via openrouter)" in content:
            deepseek_response = content.split("DeepSeek response (via openrouter)\n\n")[1].split("\n\n---\n\n# DeepSeek reasoning")[0]
        else:
            print(f"{file} does not contain anything")
        if not deepseek_response:
            print(f"No DeepSeek response found in {file}")
            if "DeepSeek reasoning (via openrouter)" in content:
                deepseek_reasoning = content.split("DeepSeek reasoning (via openrouter)\n\n")[1].split("\n\n---\n\n")[0]
            elif "DeepSeek reasoning (via deepseek)" in content:
                deepseek_reasoning = content.split("DeepSeek reasoning (via deepseek)\n\n")[1].split("\n\n---\n\n")[0]
            if "Final Answer" in deepseek_reasoning:
                print(f"Final Answer found in {file}")
                print(deepseek_reasoning[-100:])
                print("\n\n")
                print("-"*100)
                print("\n\n")
            else:
                # print(f"No Final Answer found in {file}")
                pass