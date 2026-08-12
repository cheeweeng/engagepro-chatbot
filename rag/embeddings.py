# Create and configure the embedding model.

"""
Embedding model factory.
"""

from functools import lru_cache
from langchain_openai import OpenAIEmbeddings

from config import EMBEDDING_MODEL


@lru_cache(maxsize=1)  # Cache the embedding model instance to avoid reloading it multiple times.
def get_embeddings() -> OpenAIEmbeddings:
    """
    Create and return the configured embedding model.
    """

    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL
    )