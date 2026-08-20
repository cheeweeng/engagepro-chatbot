"""
State definition for the chatbot workflow.
"""

from langgraph.graph import MessagesState

# MessagesState is a pre-built state structure provided by LangGraph for conversations involving messages.
class ChatState(MessagesState):
    """
    Chatbot state.

    Extends LangGraph's built-in MessagesState so we can
    add our own fields later if needed.
    """

    route: str = ""
    safety: str = ""
    standalone_query: str = ""