"""
Prompt builder for direct meta-conversational chat responses.
"""

def build_direct_prompt(
    question: str,
    history: str = "",
) -> str:
    """
    Build a prompt for meta-conversational and direct chat queries.
    """

    history_section = ""
    if history.strip():
        history_section = f"""
Conversation History
--------------------

{history.strip()}
"""

    return f"""
You are EngagePro's official AI assistant.

Your task is to answer the user's question directly.
If the user asks about previous questions or topics discussed in the conversation, 
refer to the Conversation History provided below to answer accurately.

Be helpful, friendly, professional, clear, and concise.
{history_section}
User Question
-------------

{question}

Answer
"""
