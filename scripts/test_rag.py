from rag.retrieval import retrieve_documents

question = "What products does EngagePro provide?"

documents = retrieve_documents(question)

print(f"\nRetrieved {len(documents)} documents\n")

for i, doc in enumerate(documents, start=1):

    print("=" * 70)
    print(f"Document {i}")
    print("=" * 70)

    print(doc.page_content)
    print("\nMetadata:", doc.metadata)
    print()