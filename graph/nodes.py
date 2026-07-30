"""
LangGraph nodes.
"""

from langchain_core.messages import AIMessage

from graph.state import ChatState
from llm.llm_factory import get_llm

from rag.retrieval import retrieve_documents
from prompts.rag_prompt import build_rag_prompt

from routing.router import classify_question

from wiki.wikipedia_search import retrieve_wikipedia_summary
from prompts.wiki_prompt import build_wiki_prompt

# ===========================
# RAG Node
# ===========================

def rag_chat_node(state: ChatState) -> ChatState:
    """
    Generate a grounded response using Retrieval-Augmented Generation (RAG).
    """

    llm = get_llm()

    # Latest user question
    question = state["messages"][-1].content

    # Retrieve relevant brochure chunks
    documents = retrieve_documents(question)

    # Build the RAG prompt
    prompt = build_rag_prompt(
        question=question,
        documents=documents,
    )

    # Ask the LLM
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
    wikipedia_summary = retrieve_wikipedia_summary(question)

    # Build the prompt
    prompt = build_wiki_prompt(
        question=question,
        wikipedia_summary=wikipedia_summary,
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

    question = state["messages"][-1].content

    route = classify_question(question)
    
    return {
        "route": route
    }