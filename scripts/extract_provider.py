import sys
import re
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.utils.io import read_json


def extract_provider_from_rollout(rollout_path, section="deepseek"):
    with open(rollout_path, encoding='utf-8') as f:
        content = f.read()

    patterns = {
        "deepseek": r"# DeepSeek (?:response|reasoning) \((?:via|with) (.*?)\)",
        "cutoff": r"# cutoff_deepseek_completion(?: \((?:via|with) (.*?)\))?",
        "anthropic": r"# paraphrased_deepseek_completion_anthropic(?: \((?:via|with) (.*?)\))?",
        "openai": r"# paraphrased_deepseek_completion_openai(?: \((?:via|with) (.*?)\))?"
    }

    pattern = patterns.get(section)
    if not pattern:
        return None

    match = re.search(pattern, content)
    if match and match.groups():
        return match.group(1).lower() if match.group(1) else "unknown"
    return "not_found"


def analyze_providers(scores_path, rollouts_dir):
    data = read_json(scores_path)
    rollouts_path = Path(rollouts_dir)

    provider_counts = {"openrouter": 0, "deepseek": 0, "unknown": 0, "not_found": 0}

    for item in data:
        filename = item.get("file")
        if not filename:
            continue

        rollout_file = rollouts_path / filename
        if not rollout_file.exists():
            continue

        provider = extract_provider_from_rollout(rollout_file)

        if provider and "openrouter" in provider:
            provider_counts["openrouter"] += 1
        elif provider and "deepseek" in provider:
            provider_counts["deepseek"] += 1
        elif provider == "not_found":
            provider_counts["not_found"] += 1
        else:
            provider_counts["unknown"] += 1

    print("\nProvider Distribution:")
    total = sum(provider_counts.values())
    for provider, count in provider_counts.items():
        pct = (count / total * 100) if total > 0 else 0
        print(f"  {provider}: {count} ({pct:.1f}%)")

    return provider_counts


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_provider.py <scores_file> <rollouts_dir>")
        sys.exit(1)

    scores_path = sys.argv[1]
    rollouts_dir = sys.argv[2]

    analyze_providers(scores_path, rollouts_dir)
