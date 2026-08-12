# reposnsibility
'''Question

↓

Chroma

↓

Relevant Documents'''

"""
Document retrieval utilities.
"""

from langchain_core.documents import Document

from rag.vectorstore import load_vectorstore


def retrieve_documents(
    question: str,
    k: int = 3,       # number of relevant documents to retrieve
) -> list[Document]:
    """
    Retrieve the most relevant brochure chunks.
    """

    # this calls rag/vectorstore.py
    vectorstore = load_vectorstore()

    # retrieve the most relevant documents from the vectorstore
    return vectorstore.similarity_search(
        question,
        k=k,
    )

