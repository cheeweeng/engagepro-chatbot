"""
Document chunking utilities.
Take the loaded Document objects and split them into smaller, overlapping chunks.
"""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(
    documents: list[Document],
) -> list[Document]:
    """
    Split documents into overlapping chunks.
    """

    # Create a text splitter using LangChain's RecursiveCharacterTextSplitter to split the documents into smaller chunks.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    return chunks