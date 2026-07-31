"""
Build the chatbot workflow.
"""

from langgraph.graph import StateGraph, START, END

from graph.state import ChatState

from graph.nodes import (
    safety_node,
    blocked_node,
    routing_node,
    rag_chat_node,
    general_chat_node,
)

def route_safety(state: ChatState) -> str:
    """
    Return the safety classification.
    """

    return state["safety"]

def route_question(state: ChatState) -> str:
    """
    Return the route selected by the routing node.
    This function simply tells LangGraph which edge to follow.
    """

    return state["route"]

builder = StateGraph(ChatState)

builder.add_node("safety", safety_node)

builder.add_node("blocked", blocked_node)

builder.add_node("router", routing_node)

builder.add_node("rag_chat", rag_chat_node)

builder.add_node("general_chat", general_chat_node)

builder.add_edge(START, "safety")

builder.add_conditional_edges(
    "safety",
    route_safety,
    {
        "safe": "router",
        "blocked": "blocked"
    }
)

builder.add_conditional_edges(
    "router",
    route_question,
    {
        "engagepro": "rag_chat",
        "general": "general_chat",
    },
)

builder.add_edge("blocked", END)

builder.add_edge("rag_chat", END)

builder.add_edge("general_chat", END)

graph = builder.compile()