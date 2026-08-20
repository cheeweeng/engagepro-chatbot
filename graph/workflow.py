"""
Build the chatbot workflow, orchestrates the overall workflow (control flow)
by deciding the sequence in which the nodes are executed and 
how the chatbot transitions from one node to another based on the state.
"""

from langgraph.graph import StateGraph, START, END

from graph.state import ChatState

from graph.nodes import (
    contextualize_query_node,
    safety_node,
    blocked_node,
    routing_node,
    rag_chat_node,
    general_chat_node,
    direct_chat_node,
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
# Build the workflow graph
builder = StateGraph(ChatState)

# Add nodes to the graph
builder.add_node("contextualize_query", contextualize_query_node)

builder.add_node("safety", safety_node)

builder.add_node("blocked", blocked_node)

builder.add_node("router", routing_node)

builder.add_node("rag_chat", rag_chat_node)

builder.add_node("general_chat", general_chat_node)

builder.add_node("direct_chat", direct_chat_node)

# The workflow sequence is determined by the graph edges
# the workflow starts with contextualize query node
builder.add_edge(START, "contextualize_query")  

builder.add_edge("contextualize_query", "safety") # then proceed to safety evaluation            

builder.add_conditional_edges(               # if the safety node returns "safe", go to the router node, 
    "safety",                                # otherwise go to the blocked node
    route_safety,
    {
        "safe": "router",
        "blocked": "blocked"
    }
)

builder.add_conditional_edges(              # if router node returns "engagepro", go to the rag_chat node,
    "router",                               # if router node returns "general", go to the general_chat node
    route_question,
    {
        "engagepro": "rag_chat",
        "general": "general_chat",
        "direct": "direct_chat"
    },
)

# define the end of each possible path
builder.add_edge("blocked", END)

builder.add_edge("rag_chat", END)

builder.add_edge("general_chat", END)

builder.add_edge("direct_chat", END)

# compile the graph into a workflow
graph = builder.compile()