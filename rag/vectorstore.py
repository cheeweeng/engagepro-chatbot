# Build, save, and load the Chroma vector database

"""
ChromaDB vector store utilities.
"""

from langchain_core.documents import Document
from langchain_chroma import Chroma

from config import COLLECTION_NAME, CHROMA_DB_DIR
from rag.embeddings import get_embeddings

# create the database
def build_vectorstore(
    chunks: list[Document],
) -> Chroma:
    """
    Create and persist a Chroma vector store.
    """

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DB_DIR),
        collection_name=COLLECTION_NAME,
    )

    return vectorstore

# reuse the existing database
def load_vectorstore() -> Chroma:
    """
    Load an existing Chroma vector store.
    """

    embeddings = get_embeddings()

    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DB_DIR),
        embedding_function=embeddings,
    )