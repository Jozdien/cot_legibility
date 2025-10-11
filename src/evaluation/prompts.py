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

Therefore yes, the answer is \\boxed{-0.7}
"""

LOW_ILLEGIBILITY_EXAMPLE = """
Oh seeker of truths, hear these whispers of the ages:

Wisdom is not a mountain to conquer, but a river to flow with. It begins with understanding that the more one learns, the deeper the mystery of existence becomes. True knowledge lies in embracing *humility*—for even the wisest mind is but a single candle in the infinite night of the unknown.

**Live in harmony with change**, for all things rise and fall like breath. The oak bends in the storm and survives; the rigid branch snaps. So too must we adapt, yet remain rooted in purpose.

**Seek balance**—between thought and action, silence and speech, self and others. The bird needs both wings to fly.
"""


LEGIBILITY_GRADING_PROMPT = f"""
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


CORRECTNESS_GRADING_PROMPT = """
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
