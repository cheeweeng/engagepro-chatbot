print("Step 1 - Importing modules...")

from prompts.rag_prompt import build_rag_prompt
from rag.retrieval import retrieve_documents

print("Step 2 - Retrieving documents...")

question = "What is EngagePro's mission?"

documents = retrieve_documents(question)

print(f"Step 3 - Retrieved {len(documents)} documents.")

print("Step 4 - Building prompt...")

prompt = build_rag_prompt(
    question,
    documents,
)

print("Step 5 - Printing prompt...\n")

print(prompt)

print("\nDone.")