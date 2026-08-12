# Build, save, and load the Chroma vector database

"""
ChromaDB vector store utilities.
"""
from functools import lru_cache
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

    # this calls rag/embeddings.py
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,                   # brochure chunks to be embedded and stored in the vector database
        embedding=embeddings,               # the embedding model to use for creating vector embeddings
        persist_directory=str(CHROMA_DB_DIR),
        collection_name=COLLECTION_NAME,
    )

    return vectorstore

# reuse the existing database
# loads an existing index from disk or builds one from scratch if it doesn't exist yet
@lru_cache(maxsize=1)           # Python caches the result of load_vectorstore() to avoid reloading the vectorstore multiple times.
def load_vectorstore() -> Chroma:
    """
    Load an existing Chroma vector store. Automatically builds index
    if directory does not exist yet.
    """

    # Check if the Chroma database directory exists. If not, build the vector store from scratch.
    if not CHROMA_DB_DIR.exists():
        from rag.ingest import load_documents
        from rag.chunking import split_documents

        docs = load_documents()          # reads in raw source documents
        chunks = split_documents(docs)   # chunks the documents into smaller pieces for embedding
        return build_vectorstore(chunks)

    embeddings = get_embeddings()

    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DB_DIR),
        embedding_function=embeddings,
    )