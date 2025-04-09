## Overview

### `get_gpqa_d.py`

Gets gpqa_diamond dataset from Hugging Face.

### `r1_paraphrased.py`

Gets r1 response and reasoning for gpqa_diamond questions, paraphrases the first 25% of reasoning trace using Claude and GPT-4o, generates new responses and reasoning using the paraphrase as prefill, and saves everything to r1_rollouts/cutoff_{cutoff_portion}_[openrouter|deepseek_openrouter]/r1_faithful_cot_{timestamp}_{question[:30]}.md

Uses DeepSeek API with OpenRouter fallback. You can change cutoff_portion in the script.

### `r1_run.py`

Gets r1 response and reasoning for gpqa_diamond questions, saves to r1_rollouts/r1_only/r1_response_{timestamp}_{question[:30]}.md

### `autograder.py`

Grades rollouts in r1_rollouts/ for legibility and correctness and saves results to scores/ and answers/ directories by default.

Run with:

```bash
python autograder.py --dir <directory> --scores-output <scores_output> --answers-output <answers_output> --limit <limit> --max-chars <max_chars>
```

### `run_autograder.sh`

Runs autograder.py for all rollouts in r1_rollouts/. Skips files that already have scores and answers unless --override is set.

Run with:
```bash
bash run_autograder.sh [--override]
```

### `claude_answers.py`

Takes questions and reasoning traces from a subdirectory of r1_rollouts/ and generates answers to the questions using each reasoning trace (including partial and paraphrased partials), grades correctness of the answers, and saves to claude_answers/ and claude_answers/scores/ directories. In `generate` mode, it only generates answers, and in `grade` mode, it only grades existing answers.

Run with:
```bash
python claude_answers.py --mode <mode> --dir <directory> --limit <limit> --results <results_file> --dataset <dataset_file>
```

### `get_claude_baseline.py`

Generates a baseline for gpqa_diamond using Claude and grades correctness of the answers, and saves to claude_answers/ and claude_answers/scores/ directories.

Run with:
```bash
python get_claude_baseline.py
```

### `analyze_scores.py`

Makes plots. In `regular` mode, it makes plots of scores from scores/ directory. In `claude` mode, it makes plots of scores from a specific Claude answers score file.

Run with:
```bash
python analyze_scores.py --dir <directory> --pattern <pattern> --compare --plots --claude-file <claude_file> --analysis-type <analysis_type>
```