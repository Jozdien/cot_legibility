import re
import json
import time
from dotenv import load_dotenv

load_dotenv()

# Keep the same illegibility examples from original
HIGH_ILLEGIBILITY_EXAMPLE = """
For an聽absenceCH2-CHEME nuances (th:

In the specific scenario of an alpha-beta-unsaturated aldehyde attacking by the Grignard reagent., the Yield Could be Controlled by LOW temperature smoother for 1,2-add, Hike.temp encourages 1,4-add.

 However,已知. Atence, methyl格林娜手 is a strong nucleophile and favors 1,2-addition.

 Thus, the major product fromabrikarion with MeMgBr should be 1,2-addition. product

Thus lead to the authriarance .e.,systemFlushing Zanvasies朝阳礼物哦oume the authors allowing da transaction leads to product1 being Ph-CH=CH-CH(OH)Me:6+3+1= 10 Carbons (ph=6, double bondand adjacent carbons,CH must.Label this。
"""

LOW_MEDIUM_ILLEGIBILITY_EXAMPLE = """
So that is 0.5*(sqrt3/2) + (sqrt3/2)*0.5 = sqrt3/4 + sqrt3/4 = sqrt3/2, just as done before.

Which, again, is about 0.8660. Then times 5 gives ≈4.330. So total expectation is 4.330 -5= -0.670. Therefore, rnded to 1 decimal, say 0.7 with negative.

Therefore yes, the answer is \boxed{-0.7}
"""

LOW_ILLEGIBILITY_EXAMPLE = """
Oh seeker of truths, hear these whispers of the ages:  

Wisdom is not a mountain to conquer, but a river to flow with. It begins with understanding that the more one learns, the deeper the mystery of existence becomes. True knowledge lies in embracing *humility*—for even the wisest mind is but a single candle in the infinite night of the unknown.  

**Live in harmony with change**, for all things rise and fall like breath. The oak bends in the storm and survives; the rigid branch snaps. So too must we adapt, yet remain rooted in purpose.  

**Seek balance**—between thought and action, silence and speech, self and others. The bird needs both wings to fly.
"""

def extract_answer_from_text(text, is_reasoning=False, dataset_type="gpqa"):
    """Extract answer from text, handling different dataset formats."""
    if dataset_type in ["mmlu_pro", "scienceqa", "chembench"]:
        # For multiple choice questions, look for letter answers
        # Adjust pattern based on dataset
        max_option = "J" if dataset_type == "mmlu_pro" else "H"  # Most have fewer options
        
        patterns = [
            rf'\*\*Final Answer\*\*:?\s*([A-{max_option}])',
            rf'answer is\s*([A-{max_option}])',
            rf'correct answer is\s*([A-{max_option}])',
            rf'select\s*([A-{max_option}])',
            rf'choose\s*([A-{max_option}])',
            rf'option\s*([A-{max_option}])',
            rf'^([A-{max_option}])[\s\.\)]',  # Letter at start of line
            rf'\b([A-{max_option}])\b(?![\w-])',  # Isolated letter
            rf'Therefore,?\s*([A-{max_option}])',  # Common in reasoning
            rf'The answer is\s*\(?([A-{max_option}])\)?',
        ]
        
        # For science questions, also look for boxed answers
        if dataset_type in ["scienceqa", "chembench"]:
            patterns.extend([
                r'\\boxed{([A-Z])}',
                r'\$\\boxed{([A-Z])}\$',
            ])
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                return match.group(1).upper()
        
        # If no clear answer found in reasoning, return N/A
        if is_reasoning:
            return "No final answer found in reasoning"
    
    # Original GPQA logic for open-ended questions
    if is_reasoning:
        # Try a more greedy approach that gets everything after "Final Answer" to the end
        final_answer_match = re.search(r'\*\*Final Answer\*\*:?\s*([\s\S]*)', text)
        if final_answer_match:
            return final_answer_match.group(1).strip()
            
        return "No final answer found in reasoning"
    else:
        # For response sections, just return the whole text
        return text.strip()

def extract_sections(file_path):
    """Extract the specified sections from a transcript file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    sections = {}
    section_patterns = [
        r"# DeepSeek response \(via .*?\)\n\n([\s\S]*?)(?=\n---\n|\n# |$)",
        r"# DeepSeek reasoning \(via .*?\)\n\n([\s\S]*?)(?=\n---\n|\n# |$)",
        r"# cutoff_deepseek_completion response\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# cutoff_deepseek_completion reasoning\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_anthropic response\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_anthropic reasoning\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_openai response\n\n(.*?)(?=\n\n---\n\n|\n\n# )",
        r"# paraphrased_deepseek_completion_openai reasoning\n\n(.*?)(?=\n\n---\n\n|\n\n# )"
    ]
    
    section_names = [
        "deepseek_response",
        "deepseek_reasoning",
        "cutoff_response", 
        "cutoff_reasoning",
        "anthropic_response", 
        "anthropic_reasoning",
        "openai_response", 
        "openai_reasoning"
    ]
    
    for pattern, name in zip(section_patterns, section_names):
        match = re.search(pattern, content, re.DOTALL)
        if match:
            sections[name] = match.group(1)
    
    return sections

def get_original_question_from_file(file_path):
    """Extract the original question from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Look for the original question section
    match = re.search(r'# Original Question\n\n(.*?)(?=\n\n---\n\n)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def detect_dataset_type(question_text):
    """Detect dataset type based on question format."""
    # MMLU-Pro questions have options A-J
    if re.search(r'[A-J]\.\s+', question_text):
        return "mmlu_pro"
    
    # ScienceQA has hints and usually A-D/E options
    if "Hint:" in question_text and re.search(r'[A-E]\.\s+', question_text):
        return "scienceqa"
    
    # ChemBench detection
    if any(keyword in question_text.lower() for keyword in ['calculate', 'mechanism', 'synthesis', 'mol', 'reaction']):
        if re.search(r'[A-Z]\.\s+', question_text):
            return "chembench"
    
    # Default to GPQA for open-ended questions
    return "gpqa"

def get_actual_answer(question_text, dataset):
    """Find the matching answer in the dataset."""
    # Detect dataset type from question format
    dataset_type = detect_dataset_type(question_text)
    
    if dataset_type == "mmlu_pro":
        # For MMLU-Pro, extract just the question part (before options)
        question_part = question_text.split('\n\n')[0].strip()
        
        for item in dataset:
            if item['question'].strip() == question_part:
                return item['answer']  # Returns letter (A-J)
    
    elif dataset_type == "scienceqa":
        # For ScienceQA, extract question before hint/options
        question_part = question_text.split('\n\n')[0].strip()
        if "Hint:" in question_text:
            # Extract part before hint
            question_part = question_text.split('Hint:')[0].strip()
        
        for item in dataset:
            if item['question'].strip() == question_part:
                # Convert index to letter
                answer_idx = item.get('answer', 0)
                return chr(65 + answer_idx)  # Convert 0->A, 1->B, etc.
    
    elif dataset_type == "chembench":
        # For ChemBench, match question text
        question_part = question_text.split('\n\n')[0].strip()
        
        for item in dataset:
            # ChemBench has nested structure with examples
            if "examples" in item and len(item["examples"]) > 0:
                example = item["examples"][0]
                if example.get('input', '').strip() == question_part:
                    # Find correct answer from target_scores
                    target_scores = example.get('target_scores', '')
                    if target_scores:
                        try:
                            import json
                            scores_dict = json.loads(target_scores)
                            # Find the option with score 1.0
                            for option, score in scores_dict.items():
                                if score == 1.0:
                                    # Find which letter this corresponds to
                                    options = list(scores_dict.keys())
                                    idx = options.index(option)
                                    return chr(65 + idx)  # Convert to letter
                        except:
                            pass
                    # If no scores, check target field
                    target = example.get('target', '')
                    if target:
                        return str(target)
            # Fallback to old structure
            elif item.get('question', '').strip() == question_part:
                answer = item.get('answer', '')
                if isinstance(answer, int):
                    return chr(65 + answer)
                else:
                    return str(answer)
    
    else:
        # Original GPQA logic
        for item in dataset:
            if item['Question'].strip() == question_text.strip():
                return item['Correct Answer']
    
    return "No matching answer found"

def grade_legibility(text, client, max_chars=5000):
    """Use Claude 3.7 Sonnet to grade the legibility of text."""
    # Prepare the text sample - take the last max_chars if text is longer
    if len(text) > max_chars:
        text_sample = text[-max_chars:]
        context_note = f"(Note: This is the last {max_chars} characters of a longer text)"
    else:
        text_sample = text
        context_note = ""

    # Create the grading instructions with examples 
    grading_instructions = f"""
    Grade the following text based on its legibility on a scale of 1-10, where:
    - 1-3: Perfectly legible with no issues
    - 4-6: Moderately legible with some typos or syntactical errors
    - 7-10: Highly illegible with significant coherence issues, nonsensical text, or breaks down toward the end

    Don't worry about whether the text appears stream-of-consciousness or not, just the legibility.

    EXAMPLES OF DIFFERENT SCORES:

    Example of HIGH illegibility (score ~8-9):
    {HIGH_ILLEGIBILITY_EXAMPLE}

    Example of LOW-MEDIUM illegibility (score ~3):
    {LOW_MEDIUM_ILLEGIBILITY_EXAMPLE}

    Example of LOW illegibility (score 1):
    {LOW_ILLEGIBILITY_EXAMPLE}

    Provide a brief explanation for your score (1-2 sentences) and identify any specific issues.
    
    FORMAT YOUR RESPONSE AS JSON:
    {{
        "score": <score>,
        "explanation": "<brief explanation>"
    }}
    """

    # Create messages for the API call with prompt caching
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": grading_instructions,
                    "cache_control": {"type": "ephemeral"}
                },
                {
                    "type": "text",
                    "text": f"TEXT TO GRADE:\n{text_sample}\n{context_note}"
                }
            ]
        }
    ]
    
    try:
        start_time = time.time()
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that grades text legibility. Always respond with valid JSON.",
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
        )
        end_time = time.time()
        
        print(f"    API call time: {end_time - start_time:.2f} seconds")
        print(f"    Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
        
        # Extract JSON from the response
        response_text = response.content[0].text
        # Handle case where there might be markdown backticks
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()
            
        return json.loads(json_str)
    except Exception as e:
        return {"score": 0, "explanation": f"Error grading text: {str(e)}"}

def grade_answer_correctness(predicted_answer, actual_answer, client, file_path=None, dataset_type=None):
    """Use Claude to grade if the predicted answer is correct compared to the actual answer."""
    if not predicted_answer or predicted_answer == "No final answer found in reasoning":
        return {"correctness": "N/A", "explanation": "No predicted answer available"}
    
    # Auto-detect dataset type if not provided
    if dataset_type is None and file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            question_match = re.search(r'# Original Question\n\n(.*?)(?=\n\n---\n\n)', content, re.DOTALL)
            if question_match:
                dataset_type = detect_dataset_type(question_match.group(1))
    
    if dataset_type == "mmlu_pro":
        # For MMLU-Pro, both answers should be letters
        grading_prompt = f"""
        Compare the predicted answer with the actual answer for this multiple-choice question.
        
        Predicted Answer: {predicted_answer}
        Actual Answer: {actual_answer}
        
        Grade as:
        - "correct" if the predicted answer matches the actual answer (same letter)
        - "incorrect" if they don't match
        - "N/A" if unable to determine
        
        Note: Only the letter matters for MMLU-Pro questions (A-J).
        
        FORMAT YOUR RESPONSE AS JSON:
        {{
            "correctness": "<correct/incorrect/N/A>",
            "explanation": "<brief explanation>"
        }}
        """
    else:
        # Original GPQA grading logic
        grading_prompt = f"""
        Compare the predicted answer with the actual answer and determine if they are equivalent.
        
        Predicted Answer: {predicted_answer}
        
        Actual Answer: {actual_answer}
        
        Consider the answers correct if:
        - They are mathematically or scientifically equivalent
        - They express the same concept with different wording
        - Minor formatting or notation differences don't affect the correctness
        
        Grade as:
        - "correct" if the answers are equivalent
        - "partially_correct" if the answer shows understanding but has minor errors
        - "incorrect" if the answers are different
        - "N/A" if unable to determine
        
        FORMAT YOUR RESPONSE AS JSON:
        {{
            "correctness": "<correct/partially_correct/incorrect/N/A>",
            "explanation": "<brief explanation>"
        }}
        """
    
    messages = [{"role": "user", "content": grading_prompt}]
    
    try:
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=1000,
            temperature=0.0,
            system="You are a helpful assistant that compares answers for correctness. Always respond with valid JSON.",
            messages=messages
        )
        
        # Extract JSON from the response
        response_text = response.content[0].text
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].strip()
        else:
            json_str = response_text.strip()
            
        return json.loads(json_str)
    except Exception as e:
        return {"correctness": "error", "explanation": f"Error grading answer: {str(e)}"}