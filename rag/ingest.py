"""
Load the EngagePro brochure.

This script is responsible for reading the PDF document.
Further processing (chunking, embeddings, vector storage)
will be added in later iterations.
"""

from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

from config import BROCHURE_FILE


def load_documents() -> list[Document]:
    """
    Load the EngagePro brochure.

    Returns:
        list[Document]: The pages extracted from the brochure.
    """

    if not BROCHURE_FILE.exists():
        raise FileNotFoundError(
                f"PDF not found: {BROCHURE_FILE}"
    )

    loader = PyPDFLoader(str(BROCHURE_FILE))

    documents = loader.load()

    return documents


def inspect_documents(documents: list[Document]) -> None:
    """
    Display information about the loaded documents.
    """

    print("\nDocument Summary")
    print("-" * 60)

    print(f"Number of pages : {len(documents)}\n")

    for index, doc in enumerate(documents):

        characters = len(doc.page_content)

        page_number = doc.metadata.get("page", "Unknown")

        print(
            f"Page {page_number + 1}: "
            f"{characters:4d} characters"
        )

    print("\nMetadata Example")
    print("-" * 60)

    print(documents[0].metadata)

if __name__ == "__main__":

    documents = load_documents()

    inspect_documents(documents)

    print("\nFirst page preview\n")
    print("-" * 50)

    print(documents[0].page_content[:1000])

