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
    k: int = 3,
) -> list[Document]:
    """
    Retrieve the most relevant brochure chunks.
    """

    vectorstore = load_vectorstore()

    return vectorstore.similarity_search(
        question,
        k=k,
    )

