"""
LangGraph nodes.
"""

from langchain_core.messages import AIMessage

from graph.state import ChatState
from llm.llm_factory import get_llm

from rag.retrieval import retrieve_documents
from prompts.rag_prompt import build_rag_prompt


def chat_node(state: ChatState) -> ChatState:
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