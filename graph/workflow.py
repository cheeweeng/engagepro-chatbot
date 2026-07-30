"""
Build the chatbot workflow.
"""

from langgraph.graph import StateGraph, START, END

from graph.state import ChatState

from graph.nodes import (
    routing_node,
    rag_chat_node,
    general_chat_node,
)

def route_question(state: ChatState) -> str:
    """
    Return the route selected by the routing node.
    This function simply tells LangGraph which edge to follow.
    """

    return state["route"]

builder = StateGraph(ChatState)

builder.add_node("router", routing_node)

builder.add_node("rag_chat", rag_chat_node)

builder.add_node("general_chat", general_chat_node)

builder.add_edge(START, "router")

builder.add_conditional_edges(
    "router",
    route_question,
    {
        "engagepro": "rag_chat",
        "general": "general_chat",
    },
)

builder.add_edge("rag_chat", END)

builder.add_edge("general_chat", END)

graph = builder.compile()