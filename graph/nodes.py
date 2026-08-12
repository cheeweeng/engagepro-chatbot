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
from prompts.wiki_prompt import build_wiki_prompt

from guardrails.safety import classify_safety

# ===========================
# RAG Node
# takes the user's latest question, retrieves relevant chunks from the EngagePro knowledge base, 
# uses those documents to construct a grounded prompt, sends the prompt to the configured LLM, 
# and returns the generated response as an AIMessage in the message state
# ===========================

def rag_chat_node(state: ChatState) -> ChatState:
    """
    Generate a grounded response using Retrieval-Augmented Generation (RAG).
    """

    llm = get_llm()

    # Latest user question
    question = state["messages"][-1].content   # reads the latest user message from State

    # Retrieve relevant brochure chunks
    # this calls rag/retrieval.py
    documents = retrieve_documents(question)

    # Build the RAG prompt
    # this calls prompts/rag_prompt.py
    prompt = build_rag_prompt(
        question=question,
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
    question = state["messages"][-1].content

    # Search Wikipedia
    # this calls wiki/wikipedia_search.py
    wikipedia_summary = retrieve_wikipedia_summary(question)

    # Build the prompt
    # this calls prompts/wiki_prompt.py
    prompt = build_wiki_prompt(
        question=question,
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

    question = state["messages"][-1].content

    safety = classify_safety(question)

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

# ==========================================================
# Routing Node
# ==========================================================

def routing_node(state: ChatState) -> ChatState:
    """
    Classify the user's question and store the route.
    """

    question = state["messages"][-1].content

    route = classify_question(question)
    
    return {
        "route": route
    }