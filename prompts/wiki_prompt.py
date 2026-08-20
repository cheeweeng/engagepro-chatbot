"""
Prompt builder for Wikipedia responses.
"""

def build_wiki_prompt(
    question: str,
    wikipedia_summary: str,
    history: str = "",
) -> str:
    """
    Build a prompt using Wikipedia information and optional conversation history.
    """

    history_section = ""
    if history.strip():
        history_section = f"""
Conversation History
--------------------

{history.strip()}
"""

    return f"""
You are EngagePro's AI customer support assistant.

Use ONLY the Wikipedia information below to answer the customer's question.
Do not use your own knowledge.
If the information is insufficient,
say so honestly instead of guessing.

Be friendly,
professional,
clear,
and concise.
{history_section}
Wikipedia Information
---------------------

{wikipedia_summary}

Customer Question
-----------------

{question}

Answer
"""