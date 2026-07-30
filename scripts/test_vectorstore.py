from rag.ingest import load_documents
from rag.chunking import split_documents
from rag.vectorstore import build_vectorstore

documents = load_documents()

chunks = split_documents(documents)

vectorstore = build_vectorstore(chunks)

print("Vector store created successfully.")

print(f"Number of chunks indexed: {len(chunks)}")