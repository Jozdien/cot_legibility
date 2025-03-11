import os
import re
import glob
import json
import anthropic
import argparse
from dotenv import load_dotenv
import time

load_dotenv()

def extract_sections(file_path):
    """Extract the specified sections from a transcript file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    sections = {}
    section_patterns = [
        r"# cutoff_deepseek_completion response\n\n(.*?)(?=\n\n---\n\n)",
        r"# cutoff_deepseek_completion reasoning\n\n(.*?)(?=\n\n---\n\n)",
        r"# paraphrased_deepseek_completion_anthropic response\n\n(.*?)(?=\n\n---\n\n)",
        r"# paraphrased_deepseek_completion_anthropic reasoning\n\n(.*?)(?=\n\n---\n\n)",
        r"# paraphrased_deepseek_completion_openai response\n\n(.*?)(?=\n\n---\n\n)",
        r"# paraphrased_deepseek_completion_openai reasoning\n\n(.*?)(?=\n\n---\n\n)"
    ]
    
    section_names = [
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

# Example texts for different legibility scores
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

def grade_legibility(text, client, max_chars=5000):
    """Use Claude 3.7 Sonnet to grade the legibility of text with prompt caching."""
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

def process_transcript_file(file_path, client):
    """Process a single transcript file and grade each section."""
    print(f"\nProcessing: {file_path}")
    
    sections = extract_sections(file_path)
    results = {"file": os.path.basename(file_path), "sections": {}}
    
    for section_name, text in sections.items():
        print(f"  Grading {section_name}...")
        
        # Check if text is empty or just whitespace
        if not text or text.strip() == "":
            grade = {"score": "N/A", "explanation": "No text content available in this section"}
            print(f"    Score: N/A - No text content available")
        else:
            grade = grade_legibility(text, client)
            print(f"    Score: {grade['score']} - {grade['explanation'][:50]}...")
        
        results["sections"][section_name] = grade
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Grade legibility of transcript sections')
    parser.add_argument('--dir', type=str, default='r1_rollouts/cutoff_openrouter_api', 
                        help='Directory containing transcript files')
    parser.add_argument('--pattern', type=str, default='*.md',
                        help='File pattern to match')
    parser.add_argument('--output', type=str, default=None,
                        help='Output file for scores (defaults to directory_name_legibility_scores.json)')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit number of files to process')
    parser.add_argument('--max_chars', type=int, default=5000,
                        help='Maximum characters to use from each text section')
    
    args = parser.parse_args()
    
    # Generate output filename based on directory name if not specified
    if args.output is None:
        dir_name = os.path.basename(args.dir.rstrip('/'))
        args.output = f"scores/{dir_name}_legibility_scores.json"
    
    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Find all matching files
    file_pattern = os.path.join(args.dir, args.pattern)
    files = glob.glob(file_pattern)
    
    if args.limit:
        files = files[:args.limit]
    
    print(f"Found {len(files)} transcript files to process")
    
    all_results = []
    for file_path in files:
        try:
            result = process_transcript_file(file_path, client)
            all_results.append(result)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Save results to file
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nResults saved to {args.output}")
    
    # Print a summary
    print("\nSummary:")
    section_scores = {
        "cutoff_response": [], 
        "cutoff_reasoning": [],
        "anthropic_response": [], 
        "anthropic_reasoning": [],
        "openai_response": [], 
        "openai_reasoning": []
    }
    
    section_na_counts = {section: 0 for section in section_scores}
    
    for result in all_results:
        for section, score_data in result["sections"].items():
            if section in section_scores:
                if score_data["score"] == "N/A":
                    section_na_counts[section] += 1
                elif isinstance(score_data["score"], (int, float)):
                    section_scores[section].append(score_data["score"])
    
    for section, scores in section_scores.items():
        na_count = section_na_counts[section]
        if scores:
            avg_score = sum(scores) / len(scores)
            print(f"{section}: Avg score {avg_score:.2f} from {len(scores)} samples (N/A: {na_count})")
        else:
            print(f"{section}: No valid scores found (N/A: {na_count})")

if __name__ == "__main__":
    main()