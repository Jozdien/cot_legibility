# Chain-of-Thought Legibility

## Setup

1. **Install dependencies**:

```bash
uv pip install -r requirements.txt
```

2. **Set up environment variables**:

You should copy `.env.example` to `.env` and fill in the API keys. Which ones are necessary depend on which models you're evaluating—e.g. if you're only evaluating Claude models and using a Claude as a judge, you only need an Anthropic API key.

3. **Test pipeline**:

```bash
./run.sh config/quick_test.yaml
```

4. **Run Streamlit app**

```bash
streamlit run streamlit_app.py
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
├── runs/                     # All pipeline outputs
│   └── YYYYMMDD_HHMMSS_MODEL_DATASET/
│       ├── inference.jsonl
│       ├── evaluation.json
│       ├── plots/
│       └── run.log
└── data/                     # Downloaded datasets
```

## Pipeline Stages

### 1. Inference
- Downloads dataset to `data/`, or simply loads dataset if already present
- Calls model APIs
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

## Available Plots

### Single-Run Plots

Use these in the `plots:` list for analyzing individual runs:

- **`legibility_scores_boxplot`**: Basic boxplot of all legibility scores
- **`correctness_assessment`**: Bar chart showing % correct/partial/incorrect
- **`legibility_by_correctness`**: Boxplots comparing legibility across correctness categories
- **`length_vs_legibility`**: Scatter plot of answer length vs legibility score
- **`legibility_by_difficulty`**: Boxplots grouped by question difficulty (easy/medium/hard). Requires `baseline_file` in config
- **`correctness_vs_legibility_scatter`**: Density scatter plot showing relationship between correctness and legibility with KDE coloring
- **`correctness_vs_legibility_scatter_normalized`**: Same as above but with normalized legibility scores
- **`legibility_progression`**: Boxplots showing how legibility changes through CoT chunks. Requires `grade_legibility_chunks: true` in evaluation config

### Comparison Plots

Use these in `comparison.plot_types:` for analyzing multiple runs:

- **`model_comparison`**: Side-by-side boxplots of Response and Reasoning legibility across models
- **`legibility_comparison`**: Bar chart comparing mean legibility scores with error bars
- **`legibility_by_difficulty_comparison`**: Multi-model version of legibility by difficulty. Requires `baseline_file` in config
- **`correctness_vs_legibility_scatter_comparison`**: Density scatter aggregating all runs
- **`correctness_vs_legibility_scatter_comparison_normalized`**: Same with normalized scores

### Config Notes

```yaml
# Enable separate response/reasoning grading
evaluation:
  grade_response_reasoning_separately: true  # For model_comparison boxplots
  grade_legibility_chunks: true  # For legibility_progression (expensive!)
  chunk_size: 5000

# Provide baseline for difficulty-based plots
analysis:
  baseline_file: "runs/baseline_run/evaluation.json"
```

## Usage Examples

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

## Interactive Explorer

`streamlit_app.py` provides a web interface for exploring results:

- Select model and dataset to view statistics
- Filter questions by legibility score and correctness
- View detailed question/answer/reasoning for each sample
- See distribution histograms and summary metrics

Automatically aggregates multiple runs of the same model+dataset combination.

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