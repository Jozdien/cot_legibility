import re
import json
import time
from dotenv import load_dotenv

load_dotenv()

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

def extract_answer_from_text(text, is_reasoning=False):
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

def get_actual_answer(question_text, dataset):
    """Find the matching answer in the dataset."""
    # Find the matching question in the dataset
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

def grade_answer_correctness(predicted_answer, actual_answer, client, file_path):
    """Use Claude to grade if the predicted answer is correct compared to the actual answer."""
    if not predicted_answer or predicted_answer == "No final answer found in reasoning":
        return {"correctness": "N/A", "explanation": "No predicted answer available"}
    
    if not actual_answer or actual_answer == "No matching answer found":
        return {"correctness": "N/A", "explanation": "No reference answer available"}
    
    grading_instructions = """
    Compare the predicted answer with the actual answer and determine if the prediction is:
    - "correct": The prediction correctly addresses the question and aligns with the actual answer
    - "partially_correct": The prediction has some correct elements but also contains errors or misunderstandings
    - "incorrect": The prediction is wrong or completely misaligns with the actual answer
    
    Consider that answers might be worded differently but still convey the same meaning.
    
    FORMAT YOUR RESPONSE AS JSON:
    {
        "correctness": "correct|partially_correct|incorrect",
        "explanation": "<brief explanation for your assessment>"
    }
    """
    
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
                    "text": f"QUESTION: {get_original_question_from_file(file_path)}\n\nPREDICTED ANSWER: {predicted_answer}\n\nACTUAL ANSWER: {actual_answer}"
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
            system="You are a helpful assistant that grades answer correctness. Always respond with valid JSON.",
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
        return {"correctness": "error", "explanation": f"Error grading answer: {str(e)}"}
    
def grade_legibility_chunks(text, client, chunk_size=5000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    chunk_grades = []
    
    for chunk in chunks:
        if chunk.strip():
            grade = grade_legibility(chunk, client)
            chunk_grades.append(grade)
    
    return {
        'chunk_grades': chunk_grades,
        'average_score': sum(g['score'] for g in chunk_grades) / len(chunk_grades) if chunk_grades else 0,
        'num_chunks': len(chunks)
    }