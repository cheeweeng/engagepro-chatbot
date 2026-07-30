# Create and configure the embedding model.

"""
Embedding model factory.
"""

from langchain_openai import OpenAIEmbeddings

from config import EMBEDDING_MODEL


def get_embeddings() -> OpenAIEmbeddings:
    """
    Create and return the configured embedding model.
    """

    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL
    )