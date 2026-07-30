"""
Build the chatbot workflow.
"""

from langgraph.graph import StateGraph, START, END

from graph.state import ChatState
from graph.nodes import chat_node


builder = StateGraph(ChatState)

builder.add_node("chat", chat_node)

builder.add_edge(START, "chat")
builder.add_edge("chat", END)

graph = builder.compile()