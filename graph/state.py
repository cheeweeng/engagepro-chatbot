"""
State definition for the chatbot workflow.
"""

from langgraph.graph import MessagesState


class ChatState(MessagesState):
    """
    Chatbot state.

    Extends LangGraph's built-in MessagesState so we can
    add our own fields later if needed.
    """

    route: str = ""