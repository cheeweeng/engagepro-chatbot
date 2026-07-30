# EngagePro Chatbot
## Project Notebook

---

# Project Overview

**Project:**
EngagePro Chatbot

**Objective:**
Develop an interactive chatbot capable of engaging in natural language conversations and responding intelligently to user queries.

---

# Development Journal

## Stage 1 – Assignment Analysis

### Objective
Analyse the assignment requirements and identify the scope, deliverables and assessment criteria before beginning development.

### Assignment Requirements
- Develop an interactive chatbot capable of engaging in natural language conversations.
- Respond intelligently to user queries.
- Apply ethical safeguards to minimise hallucinations and bias.
- Demonstrate the application during a live presentation.
- Submit a technical report describing the design and implementation.

### Key Decisions
- Build the application using the modern LangChain ecosystem.
- Prioritise a simple, maintainable architecture over unnecessary features.
- Implement Retrieval-Augmented Generation (RAG) using the company brochure.
- Add advanced capabilities only if they provide clear value.

### Success Criteria
The chatbot should:
- Answer general conversational questions.
- Answer questions using the EngagePro company brochure.
- Produce factual responses grounded by retrieved documents.
- Demonstrate clean software engineering practices.
- Be easy to explain during the presentation.

### Outcome
Project scope approved.

---

## Stage 2 – System Architecture

## Stage 2 – System Architecture

### Objective
Design a modular architecture that is simple, maintainable and aligned with the modern LangChain ecosystem.

### Architecture

User

↓

Streamlit User Interface

↓

LangGraph Workflow

↓

Intent Routing (future)

↓

General Chat OR RAG

↓

OpenAI GPT

↓

Response

### Design Principles
- Separate UI from business logic.
- Use LangGraph as the workflow engine.
- Store configuration centrally in `config.py`.
- Keep each module focused on a single responsibility.
- Build the application incrementally.

### Ethical Safeguards
- Use Retrieval-Augmented Generation (RAG) to ground responses in the company brochure.
- Clearly separate company knowledge from general knowledge.
- Keep model temperature low to reduce hallucinations.
- Provide document source information where appropriate.
- Avoid generating information not supported by retrieved context.

### Outcome
Architecture approved.

---

## Stage 3 – Technology Stack

### Objective
Select technologies that satisfy the assignment requirements while remaining simple, maintainable and easy to justify.

### Selected Technologies

| Component | Technology | Reason |
|-----------|------------|--------|
| Programming Language | Python 3.11 | Stable, widely supported by AI libraries |
| UI | Streamlit | Simple and rapid web application development |
| Workflow | LangGraph | Recommended workflow framework for LangChain v1 |
| LLM Framework | LangChain v1 | Modern ecosystem with modular architecture |
| LLM | OpenAI GPT | Reliable conversational performance |
| Future Local LLM | LM Studio | Planned optional support through LLM factory |
| Vector Database | ChromaDB | Local, lightweight, no cloud dependency |
| Embedding Model | OpenAI Embeddings | Seamless integration with LangChain |
| PDF Loader | PyPDFLoader | Native LangChain document loader |
| Text Splitter | RecursiveCharacterTextSplitter | Preserves context with configurable overlap |

### Technologies Considered

- Pinecone
- MongoDB Atlas Vector Search
- Classic LangChain chains

### Reasons for Rejection

Pinecone
- Requires cloud infrastructure.
- Unnecessary for a single brochure.

MongoDB Atlas
- More complex than required.

Classic LangChain Chains
- Less flexible than LangGraph for future enhancements.

### Outcome
Technology stack approved.

---


## Iteration 1 – Environment Setup

### Objective
Prepare the development environment and verify that the core technologies work together before building the chatbot.

### Environment
- Created Conda environment:
  - EngageProChatbot
- Python Version:
  - 3.11.15

### Project Structure Created

- app.py
- config.py
- llm/
- graph/
- rag/
- scripts/
- tests/
- prompts/
- vectorstore/
- docs/

### Core Packages Installed
- LangChain v1
- LangGraph
- Streamlit
- OpenAI
- python-dotenv

### Files Created
- config.py
- llm/llm_factory.py
- graph/state.py
- graph/nodes.py
- graph/workflow.py
- scripts/test_llm.py
- scripts/test_graph.py

### Key Design Decisions
- Use Conda instead of a standard virtual environment.
- Use Python 3.11 for compatibility with LangChain.
- Implement an LLM Factory to support future switching between OpenAI and LM Studio.
- Adopt LangGraph's `MessagesState` instead of a custom state.
- Develop using small, testable increments.

### Testing
✅ OpenAI API connection verified.
✅ LangChain working.
✅ LangGraph workflow executed successfully.
✅ GPT response generated through LangGraph.

### Lessons Learned
- Run project modules using:

```bash
python -m module_name
```

instead of

```bash
python file.py
```

- MessagesState provides a future-proof conversation model.
- Verifying each layer independently simplifies debugging.

### Status
✅ Completed

### Git Commit
feat: initialise project environment and LangGraph foundation

---

## Iteration 2 – Streamlit MVP

### Objective
Build a working chatbot UI using Streamlit and integrate it with LangGraph.

### Files Created
- app.py

### Files Modified
- graph/state.py
- graph/nodes.py
- llm/llm_factory.py

### Key Design Decisions
- Refactored to MessagesState.
- Used Streamlit Session State.
- Separated UI from workflow.

### Testing
✅ Streamlit launched.
✅ Chat interface working.
✅ GPT responses generated.
✅ Conversation history preserved.

### Lessons Learned
- Streamlit reruns the script after each interaction.
- Session State preserves conversation history.
- MessagesState is the recommended LangGraph state model.
- Streamlit Session State is essential for maintaining conversation history.
- Separating the UI from the workflow improves maintainability.
- Incremental development reduces debugging complexity.

### Git Commit
feat: build Streamlit chatbot with LangGraph integration
(To be completed)

## Iteration 3.1 – PDF Loading

### Objective
Create the first component of the RAG pipeline by successfully loading the EngagePro company brochure.

### Files Created
- rag/ingest.py

### Files Modified
- config.py (added BROCHURE_FILE if implemented)

### Key Design Decisions
- Used PyPDFLoader to load PDF documents.
- Separated document loading into a dedicated function (`load_documents()`).
- Stored the brochure path in the configuration rather than hard-coding it.
- Chose to validate PDF loading before implementing chunking or embeddings.

### Testing
- Successfully loaded 8-page brochure.
- Verified readable text extraction.
- Confirmed the first page preview displayed correctly.

### Lessons Learned
- RAG development should begin by validating the source documents.
- PyPDFLoader extracts each page as a LangChain `Document`.
- Testing each stage independently simplifies debugging.

### Status
✅ Completed

## Iteration 3.2 – Document Chunking

### Objective
Split the EngagePro brochure into coherent, overlapping chunks suitable for semantic retrieval.

### Files Created
- rag/chunking.py
- scripts/test_chunking.py

### Files Modified
- config.py

### Key Design Decisions
- Used `RecursiveCharacterTextSplitter`.
- Moved `CHUNK_SIZE` and `CHUNK_OVERLAP` into `config.py`.
- Chose a chunk size of **1200 characters** with **200 characters overlap** after inspecting the brochure.
- Separated chunking logic into its own module following the Single Responsibility Principle.

### Testing
✅ Successfully split the 8-page brochure into 15 chunks.

✅ Verified chunk sizes were consistent.

✅ Confirmed chunk overlap preserved context.

### Engineering Rationale
Rather than adopting default chunking parameters from tutorials, the brochure was inspected first to understand its structure. The selected chunk size produced coherent chunks that preserved paragraph boundaries while maintaining enough overlap to improve semantic retrieval.

### Lessons Learned
- Chunking quality has a significant impact on retrieval performance.
- Overlap helps preserve context between adjacent chunks.
- Inspecting chunk output before generating embeddings leads to better design decisions.

### Status
✅ Completed

## Iteration 3.3 – Knowledge Base Construction

### Objective
Create a persistent vector database from the EngagePro company brochure for semantic retrieval.

### Files Created
- rag/embeddings.py
- rag/vectorstore.py
- scripts/test_vectorstore.py

### Files Modified
- config.py
- rag/ingest.py

### Key Design Decisions
- Centralised embedding model configuration in `config.py`.
- Separated embedding generation from vector database management.
- Used ChromaDB as a local persistent vector store.
- Persisted embeddings to disk so indexing only needs to occur when source documents change.

### Testing
✅ Embedding model successfully created.
✅ ChromaDB created successfully.
✅ 15 document chunks indexed.
✅ Vector database persisted locally.
✅ Semantic retrieval successfully returned relevant brochure content.
### Engineering Rationale
The indexing pipeline is separated from runtime retrieval. This avoids regenerating embeddings whenever the chatbot starts, improving efficiency and reducing API usage.

### Lessons Learned
- Embeddings transform text into semantic vectors for similarity search.
- ChromaDB stores vectors locally, allowing the chatbot to reuse the knowledge base without regenerating embeddings.
- Retrieval quality depends heavily on document quality and chunking strategy.
- Separating indexing from runtime retrieval improves efficiency and maintainability.

### Status
✅ Completed

### Definition of Done

- ✅ PDF loaded successfully.
- ✅ Document inspected.
- ✅ Metadata inspected.
- ✅ Document chunked.
- ✅ Chunk quality evaluated.
- ✅ Embeddings generated.
- ✅ ChromaDB created and persisted.
- ✅ Semantic retrieval validated.

Iteration 3 completed successfully.

## Iteration 4.1 – RAG Integration

### Objective
Integrate the knowledge base into the LangGraph chatbot so that responses are grounded in the EngagePro brochure.

### Files Created
- rag/retrieval.py
- prompts/rag_prompt.py
- scripts/test_prompt.py
- scripts/test_rag.py

### Files Modified
- graph/nodes.py

### Key Design Decisions
- Kept the LangGraph workflow unchanged.
- Integrated retrieval inside the existing chat node.
- Separated retrieval, prompt construction and LLM invocation into dedicated modules.
- Used prompt engineering to reduce hallucinations.

### Testing
✅ Retrieval returned relevant brochure chunks.

✅ Prompt constructed successfully.

⬜ Chatbot integration (pending).

### Engineering Rationale
Rather than adding additional LangGraph nodes, retrieval was integrated into the existing chat node. This keeps the workflow simple while preserving modularity through dedicated retrieval and prompt modules.

### Testing

✅ Retrieved relevant brochure documents.

✅ Prompt successfully constructed.

✅ LangGraph integrated with the RAG pipeline.

✅ Chatbot answered EngagePro questions using brochure content.

✅ Chatbot correctly refused to answer questions not supported by the brochure.

### Lessons Learned

- Retrieval quality and prompt design both influence RAG performance.
- An overly restrictive prompt may prevent the model from synthesising relevant information.
- Prompt engineering can improve answer quality without changing the retrieval pipeline.
- Modular design allowed RAG integration by modifying only the chat node.

### Status

✅ Completed

# Architecture Decisions (ADR)

(To be completed)

---

# Testing Log

(To be completed)

---

# Lessons Learned

(To be completed)

---

# Presentation Notes

(To be completed)

---

# Future Improvements

(To be completed)