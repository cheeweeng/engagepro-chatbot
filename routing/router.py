"""
Lightweight routing agent that performs a classification task.
The agent:
- receives a goal (classify the question),
- reasons using an LLM,
- makes a decision,
- determines the next workflow. 
"""

from llm.llm_factory import get_llm


def classify_question(question: str) -> str:
    """
    Classify the user's question.

    Returns:
        "engagepro"
        "general"
        "direct"
    """

    llm = get_llm(tier="fast")

    prompt = f"""
You are an intent classifier.

Classify the user's question into exactly ONE category.

Category 1:
engagepro

Questions specifically about:
- EngagePro
- its company
- mission
- vision
- products
- services
- brochure
- business
- AI solutions
- customer engagement

Category 2:
direct

Questions specifically about:
- the conversation history or previous questions (e.g. "what was my first question?", "summarize our chat")
- greetings, pleasantries, or general assistant capabilities (e.g. "hi", "hello", "who are you?", "how can you help me?")

Category 3:
general

Everything else requiring external topic lookup or general knowledge (e.g. science, history, concepts).

Return exactly one lowercase word.

Valid outputs:

engagepro

direct

general

Do not explain your answer.
Do not include punctuation.

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()