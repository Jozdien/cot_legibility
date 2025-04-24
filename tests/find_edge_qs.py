import json
import numpy as np
with open('../claude_answers/scores/claude_baseline_scores.json', 'r') as f:
    claude_scores = json.load(f)
    claude_scores = claude_scores['detailed_results']
with open('../scores/cutoff_0.25_deepseek_openrouter_scores.json', 'r') as f:
    deepseek_scores = json.load(f)

grading = lambda x: 2 if x == 'correct' else 1 if x == 'partially_correct' else 0
grades = {}
legibility_grades = {}

for (idx, q_data) in enumerate(claude_scores.values()):
    question = q_data['question'].strip()
    actual_answer = q_data['actual_answer']
    claude_grade = grading(q_data['grade']['correctness'])
    grades[question] = {
        'claude': claude_grade,
        'deepseek': None,
        'actual_answer': actual_answer
    }

for q_data in deepseek_scores:
    question = q_data['question'].strip()
    deepseek_grade = grading(q_data['correctness']['deepseek']['correctness'])
    grades[question]['deepseek'] = deepseek_grade
    legibility_ds_response = q_data['legibility']['deepseek_response']['score'] if 'deepseek_response' in q_data['legibility'] else None
    legibility_ds_reasoning = q_data['legibility']['deepseek_reasoning']['score'] if 'deepseek_reasoning' in q_data['legibility'] else None
    legibility_cutoff_response = q_data['legibility']['cutoff_response']['score'] if 'cutoff_response' in q_data['legibility'] else None
    legibility_cutoff_reasoning = q_data['legibility']['cutoff_reasoning']['score'] if 'cutoff_reasoning' in q_data['legibility'] else None
    legibility_anthropic_response = q_data['legibility']['anthropic_response']['score'] if 'anthropic_response' in q_data['legibility'] else None
    legibility_anthropic_reasoning = q_data['legibility']['anthropic_reasoning']['score'] if 'anthropic_reasoning' in q_data['legibility'] else None
    legibility_openai_response = q_data['legibility']['openai_response']['score'] if 'openai_response' in q_data['legibility'] else None
    legibility_openai_reasoning = q_data['legibility']['openai_reasoning']['score'] if 'openai_reasoning' in q_data['legibility'] else None
    legibility_grades[question] = {
        'deepseek_response': legibility_ds_response,
        'deepseek_reasoning': legibility_ds_reasoning,
        'cutoff_response': legibility_cutoff_response,
        'cutoff_reasoning': legibility_cutoff_reasoning,
        'anthropic_response': legibility_anthropic_response,
        'anthropic_reasoning': legibility_anthropic_reasoning,
        'openai_response': legibility_openai_response,
        'openai_reasoning': legibility_openai_reasoning,
    }

qs_ds_better = []
qs_ds_better_legibility = []
qs_claude_better = []
qs_claude_better_legibility = []
qs_tie_wrong = []
qs_tie_wrong_legibility = []
qs_tie_partially_correct = []
qs_tie_partially_correct_legibility = []
qs_tie_correct = []
qs_tie_correct_legibility = []
qs_ds_correct = []
qs_ds_correct_legibility = []
qs_ds_incorrect = []
qs_ds_incorrect_legibility = []
for question, grade in grades.items():
    if grade['deepseek'] > grade['claude']:
        qs_ds_better.append(question)
        qs_ds_better_legibility.append(legibility_grades[question])
    if grade['claude'] > grade['deepseek']:
        qs_claude_better.append(question)
        qs_claude_better_legibility.append(legibility_grades[question])
    if grade['deepseek'] == grade['claude'] and grade['deepseek'] == 0:
        qs_tie_wrong.append(question)
        qs_tie_wrong_legibility.append(legibility_grades[question])
    if grade['deepseek'] == grade['claude'] and grade['deepseek'] == 1:
        qs_tie_partially_correct.append(question)
        qs_tie_partially_correct_legibility.append(legibility_grades[question])
    if grade['deepseek'] == grade['claude'] and grade['deepseek'] == 2:
        qs_tie_correct.append(question)
        qs_tie_correct_legibility.append(legibility_grades[question])
    if grade['deepseek'] == 2:
        qs_ds_correct.append(question)
        qs_ds_correct_legibility.append(legibility_grades[question])
    if grade['deepseek'] == 1 or grade['deepseek'] == 0:
        qs_ds_incorrect.append(question)
        qs_ds_incorrect_legibility.append(legibility_grades[question])

ds_better_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_ds_better_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_ds_better_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_ds_better_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_ds_better_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_ds_better_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_ds_better_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_ds_better_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_ds_better_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_better_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
ds_better_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_ds_better_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_ds_better_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_ds_better_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_ds_better_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_ds_better_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_ds_better_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_ds_better_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_ds_better_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
claude_better_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_claude_better_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_claude_better_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_claude_better_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_claude_better_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_claude_better_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_claude_better_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_claude_better_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_claude_better_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_claude_better_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
claude_better_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_claude_better_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_claude_better_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_claude_better_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_claude_better_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_claude_better_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_claude_better_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_claude_better_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_claude_better_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
tie_wrong_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_tie_wrong_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_tie_wrong_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_tie_wrong_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_tie_wrong_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_wrong_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
tie_wrong_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_tie_wrong_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_tie_wrong_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_tie_wrong_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_tie_wrong_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_tie_wrong_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
tie_partially_correct_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_tie_partially_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_tie_partially_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_tie_partially_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_tie_partially_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_partially_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
tie_partially_correct_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_tie_partially_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_tie_partially_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_tie_partially_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_tie_partially_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_tie_partially_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
tie_correct_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_tie_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_tie_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_tie_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_tie_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_tie_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_tie_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_tie_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_tie_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_tie_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
tie_correct_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_tie_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_tie_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_tie_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_tie_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_tie_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_tie_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_tie_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_tie_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
ds_correct_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_ds_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_ds_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_ds_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_ds_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_ds_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_ds_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_ds_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_ds_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
ds_correct_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_ds_correct_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_ds_correct_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_ds_correct_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_ds_correct_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_ds_correct_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_ds_correct_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_ds_correct_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_ds_correct_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
ds_incorrect_avg_legibility = {
    "deepseek_response": sum(q_data["deepseek_response"] for q_data in qs_ds_incorrect_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": sum(q_data["deepseek_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": sum(q_data["cutoff_response"] for q_data in qs_ds_incorrect_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": sum(q_data["cutoff_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": sum(q_data["anthropic_response"] for q_data in qs_ds_incorrect_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": sum(q_data["anthropic_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": sum(q_data["openai_response"] for q_data in qs_ds_incorrect_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": sum(q_data["openai_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A") / len([q_data for q_data in qs_ds_incorrect_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}
ds_incorrect_std_legibility = {
    "deepseek_response": np.std([q_data["deepseek_response"] for q_data in qs_ds_incorrect_legibility if q_data["deepseek_response"] is not None and q_data["deepseek_response"] != "N/A"]),
    "deepseek_reasoning": np.std([q_data["deepseek_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["deepseek_reasoning"] is not None and q_data["deepseek_reasoning"] != "N/A"]),
    "cutoff_response": np.std([q_data["cutoff_response"] for q_data in qs_ds_incorrect_legibility if q_data["cutoff_response"] is not None and q_data["cutoff_response"] != "N/A"]),
    "cutoff_reasoning": np.std([q_data["cutoff_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["cutoff_reasoning"] is not None and q_data["cutoff_reasoning"] != "N/A"]),
    "anthropic_response": np.std([q_data["anthropic_response"] for q_data in qs_ds_incorrect_legibility if q_data["anthropic_response"] is not None and q_data["anthropic_response"] != "N/A"]),
    "anthropic_reasoning": np.std([q_data["anthropic_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["anthropic_reasoning"] is not None and q_data["anthropic_reasoning"] != "N/A"]),
    "openai_response": np.std([q_data["openai_response"] for q_data in qs_ds_incorrect_legibility if q_data["openai_response"] is not None and q_data["openai_response"] != "N/A"]),
    "openai_reasoning": np.std([q_data["openai_reasoning"] for q_data in qs_ds_incorrect_legibility if q_data["openai_reasoning"] is not None and q_data["openai_reasoning"] != "N/A"]),
}

num_none_ds = 0
num_na_ds = 0
for i, q in enumerate(qs_ds_better):
    legibility_grades_q = qs_ds_better_legibility[i]
    num_none_ds += list(legibility_grades_q.values()).count(None)
    num_na_ds += list(legibility_grades_q.values()).count('N/A')
    if sum(score for score in legibility_grades_q.values() if score is not None and score != "N/A") > 10:
        # print(q)
        print(qs_ds_better_legibility[i])
        # print("\n\n---\n\n")
print(f"Deepseek: {len(qs_ds_better)} questions, Number of None: {num_none_ds}, Number of N/A: {num_na_ds}")

num_none_claude = 0
num_na_claude = 0
for i, q in enumerate(qs_claude_better):
    legibility_grades_q = qs_claude_better_legibility[i]
    num_none_claude += list(legibility_grades_q.values()).count(None)
    num_na_claude += list(legibility_grades_q.values()).count('N/A')
    if sum(score for score in legibility_grades_q.values() if score is not None and score != "N/A") > 2:
        # print(q)
        print(qs_claude_better_legibility[i])
        # print("\n\n---\n\n")
print(f"Claude: {len(qs_claude_better)} questions, Number of None: {num_none_claude}, Number of N/A: {num_na_claude}")

num_none_tie = 0
num_na_tie = 0
for i, q in enumerate(qs_tie_wrong):
    legibility_grades_q = qs_tie_wrong_legibility[i]
    num_none_tie += list(legibility_grades_q.values()).count(None)
    num_na_tie += list(legibility_grades_q.values()).count('N/A')
    if sum(score for score in legibility_grades_q.values() if score is not None and score != "N/A") > 2:
        # print(q)
        print(qs_tie_wrong_legibility[i])
        # print("\n\n---\n\n")
print(f"Tie: {len(qs_tie_wrong)} questions, Number of None: {num_none_tie}, Number of N/A: {num_na_tie}")
for i, q in enumerate(qs_tie_partially_correct):
    legibility_grades_q = qs_tie_partially_correct_legibility[i]
    num_none_tie += list(legibility_grades_q.values()).count(None)
    num_na_tie += list(legibility_grades_q.values()).count('N/A')
    if sum(score for score in legibility_grades_q.values() if score is not None and score != "N/A") > 2:
        # print(q)
        print(qs_tie_partially_correct_legibility[i])
        # print("\n\n---\n\n")
print(f"Tie: {len(qs_tie_partially_correct)} questions, Number of None: {num_none_tie}, Number of N/A: {num_na_tie}")
for i, q in enumerate(qs_tie_correct):
    legibility_grades_q = qs_tie_correct_legibility[i]
    num_none_tie += list(legibility_grades_q.values()).count(None)
    num_na_tie += list(legibility_grades_q.values()).count('N/A')
    if sum(score for score in legibility_grades_q.values() if score is not None and score != "N/A") > 2:
        # print(q)
        print(qs_tie_correct_legibility[i])
        # print("\n\n---\n\n")
print(f"Tie: {len(qs_tie_correct)} questions, Number of None: {num_none_tie}, Number of N/A: {num_na_tie}")

for key in ds_better_avg_legibility:
    print(f"{key}:")
    print(f"Deepseek better: Avg: {ds_better_avg_legibility[key]}, Std: {ds_better_std_legibility[key]}")
    print(f"Claude better: Avg: {claude_better_avg_legibility[key]}, Std: {claude_better_std_legibility[key]}")
    print(f"Tie wrong: Avg: {tie_wrong_avg_legibility[key]}, Std: {tie_wrong_std_legibility[key]}")
    print(f"Tie partially correct: Avg: {tie_partially_correct_avg_legibility[key]}, Std: {tie_partially_correct_std_legibility[key]}")
    print(f"Tie correct: Avg: {tie_correct_avg_legibility[key]}, Std: {tie_correct_std_legibility[key]}")
    print(f"Deepseek correct: Avg: {ds_correct_avg_legibility[key]}, Std: {ds_correct_std_legibility[key]}")
    print(f"Deepseek incorrect: Avg: {ds_incorrect_avg_legibility[key]}, Std: {ds_incorrect_std_legibility[key]}")
    print("\n")
