"""
Safety classifier for user questions.

Detects whether a question should be blocked before entering
the chatbot workflow.
"""

from llm.llm_factory import get_llm

# perform the classification using the LLM and prompt
def classify_safety(question: str) -> str:
    """
    Classify a question as either:

    safe
    or
    blocked
    """

    llm = get_llm(tier="fast") # directing safety classification to gpt-4o-mini.

    prompt = f"""
You are a safety classifier.

Classify the user's question.
If you are unsure, classify the question as safe.

Return ONLY one word.

Category 1:
safe

Questions that are appropriate for an educational or customer support chatbot.

Category 2:
blocked

Questions involving:

- politics            # request political opinions or political persuasion
- religion            # request religious opinions or attempt religious persuasion
- promote racism
- hate speech
- promote discrimination
- explicit sexual content
- NSFW content
- abusive or offensive language
- illegal or harmful activities

Return ONLY one word.

safe

or

blocked

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()