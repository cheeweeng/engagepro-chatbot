"""
LangGraph nodes.
nodes.py contains the implementation of the individual tasks, 
such as Safety Guardrail, Routing, RAG, blocked response and General Chat
"""

from langchain_core.messages import AIMessage

from graph.state import ChatState
from llm.llm_factory import get_llm

from rag.retrieval import retrieve_documents
from prompts.rag_prompt import build_rag_prompt

from routing.router import classify_question

from wiki.wikipedia_search import retrieve_wikipedia_summary
from prompts import (
    build_rag_prompt,
    build_wiki_prompt,
    build_direct_prompt,
)

from guardrails.safety import classify_safety

# ===========================
# Helper function to format up to 4 recent message turns for prompts.
# ===========================
def format_recent_history(messages: list, max_turns: int = 4) -> str:
    """
    Format up to max_turns of recent conversation messages into string format.
    """
    recent_messages = messages[-max_turns:]
    formatted = []
    for msg in recent_messages:
        role = "User" if msg.type == "human" else "Assistant"
        formatted.append(f"{role}: {msg.content}")
    return "\n".join(formatted)


# ===========================
# Query Contextualization Node
# If conversation history exists (more than 1 turn), 
# it takes past messages and rephrases follow-up pronouns
# ===========================

def contextualize_query_node(state: ChatState) -> ChatState:
    """
    Rephrase the latest user message into a standalone question if conversation history exists.
    """
    messages = state.get("messages", [])
    if not messages:
        return {"standalone_query": ""}

    latest_question = messages[-1].content

    # If this is the first turn, no rephrasing needed
    if len(messages) <= 1:
        return {"standalone_query": latest_question}

    # Format recent history (excluding the current latest question)
    history_str = format_recent_history(messages[:-1], max_turns=4)

    llm = get_llm(tier="fast")

    prompt = f"""Given the conversation history and the latest user question, 
rephrase the latest user question into a standalone question that can be understood 
WITHOUT the conversation history. Do NOT answer the question, just rephrase it if needed.
If the question is already standalone, return it as is.

Conversation History:
{history_str}

Latest Question: {latest_question}

Standalone Question:"""

    response = llm.invoke(prompt)
    standalone = response.content.strip()

    return {"standalone_query": standalone or latest_question}

# ===========================
# RAG Node
# takes the user's question, retrieves relevant chunks from the EngagePro knowledge base, 
# uses those documents to construct a grounded prompt, sends the prompt to the configured LLM, 
# and returns the generated response as an AIMessage in the message state
# ===========================

def rag_chat_node(state: ChatState) -> ChatState:
    """
    Generate a grounded response using Retrieval-Augmented Generation (RAG).
    """

    llm = get_llm()

    # Latest user question
    query = state.get("standalone_query") or state["messages"][-1].content   # reads the latest user message from State

    # Retrieve relevant brochure chunks
    # this calls rag/retrieval.py
    documents = retrieve_documents(query)

    # Build the RAG prompt
    # this calls prompts/rag_prompt.py
    prompt = build_rag_prompt(
        question=query,
        documents=documents,
    )

    # GPT generates the response
    response = llm.invoke(prompt)

    return {
        "messages": [
            AIMessage(content=response.content)
        ]
    }


# ===========================
# General Chat Node
# ===========================

def general_chat_node(state: ChatState) -> ChatState:
    """
    Answer general and technical questions using Wikipedia.
    """

    llm = get_llm()

    # Latest user question
    query = state.get("standalone_query") or state["messages"][-1].content

    # Search Wikipedia
    # this calls wiki/wikipedia_search.py
    wikipedia_summary = retrieve_wikipedia_summary(query)

    # Build the prompt
    # this calls prompts/wiki_prompt.py
    prompt = build_wiki_prompt(
        question=query,
        wikipedia_summary=wikipedia_summary,
    )

    # GPT generates the response
    response = llm.invoke(prompt)

    return {
        "messages": [
            AIMessage(content=response.content)
        ]
    }

# ===========================
# Safety Node
# ===========================

def safety_node(state: ChatState) -> ChatState:
    """
    Classify whether the user's question is safe.
    """

    query = state.get("standalone_query") or state["messages"][-1].content

    safety = classify_safety(query)

    return {
        "safety": safety
    }

# ===========================
# Blocked Node
# ===========================

def blocked_node(state: ChatState) -> ChatState:
    """
    Return a response for blocked questions.
    """

    return {
        "messages": [
            AIMessage(
                content=(
                    "I'm sorry, but I cannot assist with requests involving "
                    "politics, religion, hate speech, racism, discrimination,"
                    "abusive language, or explicit sexual content.\n\n"
                    "Please ask a question about EngagePro or another "
                    "general educational topic."
                )
            )
        ]
    }

# ===========================
# Direct Chat Node (Meta-Conversational)
# ===========================

def direct_chat_node(state: ChatState) -> ChatState:
    """
    Answer meta-conversational and direct chat questions using conversation history.
    """

    llm = get_llm()

    latest_question = state["messages"][-1].content

    # Format recent history (up to 6 turns for rich meta-chat context)
    history_str = format_recent_history(state["messages"][:-1], max_turns=6)

    # Build direct prompt
    prompt = build_direct_prompt(
        question=latest_question,
        history=history_str,
    )

    # Ask the LLM
    response = llm.invoke(prompt)

    return {
        "messages": [
            AIMessage(content=response.content)
        ]
    }

# ==========================================================
# Routing Node
# ==========================================================

def routing_node(state: ChatState) -> ChatState:
    """
    Classify the user's question and store the route.
    """

    query = state.get("standalone_query") or state["messages"][-1].content

    route = classify_question(query)
    
    return {
        "route": route
    }