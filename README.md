# CoT Faithfulness Research Pipeline

Refactored pipeline for analyzing Chain-of-Thought reasoning legibility and correctness in large language models.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Download a dataset (if needed)
python get_gpqa_d.py

# Run quick test
./run.sh config/quick_test.yaml

# Run full pipeline
./run.sh config/default.yaml
```

## Structure

```
cot_faithfulness/
├── run.sh                    # Single entry point for all pipelines
├── config/                   # YAML configuration files
│   ├── default.yaml         # Full parameter set
│   ├── quick_test.yaml      # Minimal test (5 questions)
│   └── examples/            # Example configs
├── src/                      # All source code
│   ├── inference/           # Generate model responses
│   ├── evaluation/          # Grade responses
│   ├── analysis/            # Generate plots
│   └── utils/               # Shared utilities
├── data/                     # Downloaded datasets
├── runs/                     # All pipeline outputs
│   └── YYYYMMDD_HHMMSS_MODEL_DATASET/
│       ├── inference.jsonl
│       ├── evaluation.json
│       ├── plots/
│       └── run.log
└── archive/                  # Old data from previous codebase
```

## Pipeline Stages

### 1. Inference
- Loads dataset from `data/`
- Calls model APIs (OpenRouter, Anthropic, OpenAI)
- Streams results to `inference.jsonl`

### 2. Evaluation
- Loads `inference.jsonl`
- Grades legibility (1-10 scale, higher = more illegible)
- Grades correctness (correct/partially_correct/incorrect)
- Computes statistics
- Saves to `evaluation.json`

### 3. Analysis
- Loads `evaluation.json`
- Generates plots (boxplots, bar charts, scatter plots)
- Supports comparison across multiple runs

## Configuration

All pipelines are configured via YAML files. Key sections:

```yaml
run:
  stages: [inference, evaluation, analysis]  # Which stages to run

inference:
  models:
    - name: "R1"
      provider: "openrouter"
      model_id: "deepseek/deepseek-r1"
      temperature: 1.0
      include_reasoning: true
  datasets:
    - name: "gpqa"              # gpqa, mmlu_pro, scienceqa, chembench
      num_questions: 200
      shuffle: true
  concurrency:
    max_workers: 30

evaluation:
  grader_model: "claude-3-7-sonnet-latest"
  max_workers: 5
  grade_legibility: true
  grade_correctness: true

analysis:
  plots:
    - legibility_scores_boxplot
    - correctness_assessment
    - legibility_by_correctness
  comparison:
    enabled: false
```

## Usage Examples

### Test a single model
```bash
./run.sh config/quick_test.yaml
# Creates: runs/20250730_120345_R1_gpqa/
```

### Test multiple models
```bash
./run.sh config/examples/multi_model.yaml
# Creates separate directories for each model
```

### Run only evaluation on existing inference
```yaml
# config/regrade.yaml
run:
  stages: [evaluation]

evaluation:
  inference_file: "runs/20250730_120345_R1_gpqa/inference.jsonl"
  grader_model: "gpt-4"
  ...
```

### Compare multiple runs
```yaml
# config/examples/analysis_only.yaml
run:
  stages: [analysis]

analysis:
  comparison:
    enabled: true
    runs:
      - "runs/20250730_120345_R1_gpqa/evaluation.json"
      - "runs/20250730_140521_claude35_gpqa/evaluation.json"
    plot_types:
      - model_comparison
      - legibility_comparison
```

## Supported Datasets

- **GPQA-Diamond**: Graduate-level science questions (~200)
- **MMLU-Pro**: Multiple choice (10 options, 12K questions)
- **ScienceQA**: High school science with hints (~1K filtered)
- **ChemBench**: Advanced chemistry problems (~1K+)

Download with: `python get_<dataset>.py`

## Supported Providers

- **OpenRouter**: Most models via unified API
- **Anthropic**: Direct Claude API
- **OpenAI**: Direct GPT API

Set API keys in `.env`:
```
OPENROUTER_API_KEY=...
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
```

## Output Formats

### inference.jsonl
```json
{"question_id": "gpqa_0", "question": "...", "answer": "...", "reasoning": "...", "model": "R1", "dataset": "gpqa", "temperature": 1.0, "timestamp": "...", "metadata": {...}}
```

### evaluation.json
```json
{
  "metadata": {...},
  "results": [
    {
      "question_id": "gpqa_0",
      "legibility": {"score": 3.5, "explanation": "..."},
      "correctness": {"grade": "correct", "explanation": "..."}
    }
  ],
  "statistics": {
    "legibility": {"mean": 3.2, "std": 1.1, ...},
    "correctness": {"correct": 150, "correct_pct": 75.0, ...}
  }
}
```

## Extending

### Add a new dataset
1. Add loader in `src/inference/datasets.py`
2. Update `_format_question()` method

### Add a new provider
1. Create provider class in `src/inference/providers.py`
2. Implement `generate()` method
3. Update `get_provider()` function

### Add a new plot
1. Add function in `src/analysis/plots.py`
2. Register in `PLOT_FUNCTIONS` or `COMPARISON_PLOT_FUNCTIONS`
3. Use in config: `plots: [your_new_plot]`

## Migration from Old Codebase

Old data is preserved in `archive/`:
- `archive/r1_rollouts/` - Model responses (markdown format)
- `archive/scores/` - Grading results (JSON)
- `archive/answers/` - Human-readable analysis (markdown)
- `archive/plots/` - Generated plots

To re-analyze old results with new plots, convert data format or use archived results as reference.
