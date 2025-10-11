# Analysis Scripts

## Statistical Analysis

### `statistical_tests.py`
Mann-Whitney U tests, Cohen's d, chi-square tests for comparing distributions.

```bash
python scripts/statistical_tests.py runs/my_run/evaluation.json [model] [metric]
```

## Data Extraction

### `extract_cot_length.py`
Extract reasoning lengths from rollout files.

```bash
python scripts/extract_cot_length.py runs/my_run/evaluation.json runs/my_run/rollouts [output.json]
```

### `extract_provider.py`
Identify which API provider was used for each response.

```bash
python scripts/extract_provider.py runs/my_run/evaluation.json runs/my_run/rollouts
```

### `normalize_scores.py`
Normalize legibility scores by CoT length.

```bash
python scripts/normalize_scores.py runs/my_run/evaluation_with_lengths.json [output.json]
```

## Advanced Plotting

### `plot_with_baseline.py`
Plot legibility grouped by baseline run correctness (easy/medium/hard questions).

```bash
python scripts/plot_with_baseline.py baseline.json output.png run1.json run2.json
```

### `plot_density_scatter.py`
Scatter plot with kernel density estimation coloring.

```bash
python scripts/plot_density_scatter.py runs/my_run/evaluation.json output.png [model] [metric] [use_normalized]
```

### `plot_faceted.py`
Separate subplot for each question.

```bash
python scripts/plot_faceted.py runs/my_run/evaluation.json output.png [model] [metric]
```

### `plot_chunks.py`
Analyze how legibility changes through the reasoning chain.

```bash
python scripts/plot_chunks.py runs/my_run/evaluation.json runs/my_run/rollouts output.png [chunk_size]
```

## Analysis Utilities

### `find_edge_cases.py`
Find questions where models perform very differently.

```bash
python scripts/find_edge_cases.py file1.json file2.json [threshold] [legibility_file.json]
```

### `cross_file_analysis.py`
Compare consistency across multiple runs.

```bash
python scripts/cross_file_analysis.py run1.json run2.json run3.json
```

### `compare_graders.py`
Compare outputs from different grader models.

```bash
python scripts/compare_graders.py grader1_output.json grader2_output.json
```

### `threshold_analysis.py`
Analyze percentage of scores above thresholds.

```bash
python scripts/threshold_analysis.py runs/my_run/evaluation.json 5 [model] [metric]
python scripts/threshold_analysis.py runs/my_run/evaluation.json 3,5,7 [model] [metric]
```

## Typical Workflow

1. Extract CoT lengths: `python scripts/extract_cot_length.py ...`
2. Normalize scores: `python scripts/normalize_scores.py ...`
3. Run statistical tests: `python scripts/statistical_tests.py ...`
4. Create visualizations: `python scripts/plot_*.py ...`
5. Find edge cases: `python scripts/find_edge_cases.py ...`
