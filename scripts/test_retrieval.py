from rag.vectorstore import load_vectorstore

vectorstore = load_vectorstore()

results = vectorstore.similarity_search(
    "What is EngagePro's mission?",
    k=3,
)

print("\nRetrieved Documents")
print("=" * 70)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 70)

    print(doc.page_content[:500])

    print("\nMetadata:")

    print(doc.metadata)