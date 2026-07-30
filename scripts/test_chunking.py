from rag.ingest import load_documents
from rag.chunking import split_documents

documents = load_documents()

chunks = split_documents(documents)

print(f"\nDocuments : {len(documents)}")
print(f"Chunks    : {len(chunks)}")

print("\nFirst 3 Chunks")
print("=" * 70)

for i, chunk in enumerate(chunks[:3], start=1):

    print(f"\nChunk {i}")
    print("-" * 70)

    print(f"Characters : {len(chunk.page_content)}")

    print(f"Page       : {chunk.metadata['page'] + 1}")

    print()

    print(chunk.page_content[:500])