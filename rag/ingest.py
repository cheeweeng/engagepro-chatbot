"""
Load the EngagePro brochure.

This script is responsible for reading the PDF document,
and convert its pages into LangChain Document objects.
Chunking, embeddings, vector storage and retrieval are handled by separate modules.
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

    # Check if the brochure file exists. If not, raise an error.
    if not BROCHURE_FILE.exists():
        raise FileNotFoundError(
                f"PDF not found: {BROCHURE_FILE}"
    )

    # Load the PDF using PyPDFLoader, which reads the PDF and splits it into individual pages.
    loader = PyPDFLoader(str(BROCHURE_FILE))

    documents = loader.load()

    return documents

# development/inspection utility
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

# Developer inspection of PDF extraction
if __name__ == "__main__":

    documents = load_documents()

    inspect_documents(documents)

    print("\nFirst page preview\n")
    print("-" * 50)

    print(documents[0].page_content[:1000])

