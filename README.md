# EngagePro Chatbot

An AI-powered customer support chatbot developed as part of the **Large Language Model Applications (LLMA)** module at **Ngee Ann Polytechnic School of InfoComm Technology**.

The chatbot answers **EngagePro-specific questions** using Retrieval-Augmented Generation (RAG), responds to **general or technical questions** using information retrieved from Wikipedia, and handles **meta-conversational queries** directly using conversation history.

---

## Project Overview

The objective of this project is to develop an interactive chatbot capable of engaging in natural language multi-turn conversations while providing accurate and grounded responses.

The chatbot combines:

- Retrieval-Augmented Generation (RAG) for company knowledge
- Wikipedia retrieval for general and technical knowledge
- Multi-turn query contextualization for conversational continuity
- Direct meta-conversational handling for chat history inquiries
- Model tiering strategy (`gpt-4o-mini` for classification/routing/contextualization, `gpt-4.1` for generation)
- In-memory performance caching (`@lru_cache`) for vector database & embeddings
- LangGraph for workflow orchestration
- Real-time streaming Streamlit web interface
- Responsible AI safety guardrails

---

## Features

- Interactive Streamlit chat interface with real-time response streaming
- EngagePro knowledge base using RAG
- Chroma vector database with in-memory caching
- OpenAI embeddings (`text-embedding-3-small`) with in-memory caching
- LangGraph workflow orchestration
- Dual-tier LLM architecture (`gpt-4.1` & `gpt-4o-mini`)
- History-aware query contextualization node for multi-turn RAG retrieval
- Direct meta-conversational chat handler for session history queries
- LLM-based routing agent (3-way intent classification)
- Wikipedia integration for general knowledge
- Responsible AI guardrails implemented using a dedicated LangGraph Safety Node
- Prompt engineering to minimise hallucinations

---

## System Architecture

```
                                 User
                                   │
                                   ▼
                               main.py
                                   │
                                   ▼
                             Streamlit UI
                                   │
                                   ▼
                           LangGraph Workflow
                                   │
                                   ▼
                 Query Contextualizer Node (GPT-4o-mini)
                                   │
                                   ▼
                  Safety Guardrail Node (GPT-4o-mini)
                     ┌─────────────┴─────────────┐
                     │                           │
                     ▼                           ▼
              Blocked Response         Routing Agent (GPT-4o-mini)
                                                 │
                          ┌──────────────────────┼──────────────────────┐
                          ▼                      ▼                      ▼
                 EngagePro Questions     General Questions     Meta-Conversational
                          │                      │                      │
                          ▼                      ▼                      │
                    ChromaDB (RAG)         Wikipedia API                │
                          │                      │                      │
                          ▼                      ▼                      ▼
                    Prompt Builder        Prompt Builder         Prompt Builder
                          └──────────────────────┼──────────────────────┘
                                                 ▼
                                              GPT-4.1
                                                 │
                                                 ▼
                                        Real-Time Stream UI
```

---

## Project Structure

```
engagepro_chatbot/
│
├── main.py              # Application entry point
├── app.py               # Streamlit user interface & token streaming
├── config.py            # Project configuration & hyperparameter settings
├── graph/               # LangGraph workflow, state, nodes & contextualization
├── guardrails/          # Safety classification
├── llm/                 # LLM factory & model tiering (GPT-4.1 / GPT-4o-mini)
├── prompts/             # Prompt templates (RAG, Wiki, Direct Chat)
├── rag/                 # Retrieval-Augmented Generation, chunking & cached vectorstore
├── routing/             # 3-way intent classification
├── wiki/                # Wikipedia API retrieval
├── scripts/             # Development and testing scripts
├── tests/               # Unit tests
├── docs/                # Documentation & presentation guide
├── data/                # Brochure and vector database
└── requirements.txt
```

---

## Technology Stack

| Component | Technology |
|----------|------------|
| Programming Language | Python 3.11 |
| User Interface | Streamlit (Real-Time Token Streaming) |
| Generation LLM | OpenAI GPT-4.1 |
| Classification LLM | OpenAI GPT-4o-mini |
| Framework | LangChain |
| Workflow Orchestration | LangGraph |
| Vector Database | ChromaDB (In-Memory Cached) |
| Embeddings | text-embedding-3-small (In-Memory Cached) |
| Document Loader | PyPDFLoader |
| Knowledge Source | EngagePro Brochure (PDF) |
| General Knowledge | Wikipedia REST API |
| Version Control | Git & GitHub |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/cheeweeng/engagepro-chatbot.git
cd engagepro-chatbot
```

### 2. Create a virtual environment

```bash
conda create -n EngageProChatbot python=3.11
conda activate EngageProChatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Application

1. Activate the project virtual environment.

2. Install the required packages (if necessary):

```bash
pip install -r requirements.txt
```

3. Launch the chatbot:

```bash
python main.py
```

---

## Example Questions

### EngagePro Questions (RAG)

- What is EngagePro's mission?
- What products does EngagePro provide?
- Where is EngagePro located?
- What are EngagePro's core values?

### General Questions (Wikipedia)

- What is Artificial Intelligence?
- Explain Retrieval-Augmented Generation.
- What is LangChain?
- What is Prompt Engineering?

### Meta-Conversational & History Questions (Direct Chat)

- What was my first question?
- Can you summarize our conversation so far?
- Who are you and how can you help me?

---

## Development Journey

The project was developed incrementally with ChatGPT acting as a technical mentor and learning companion throughout the software development lifecycle. Each iteration focused on a single component, allowing features to be implemented, tested, and integrated systematically.

1. Assignment Analysis
2. System Architecture
3. Environment Setup
4. Streamlit MVP & Token Streaming
5. PDF Loading
6. Document Chunking
7. Knowledge Base Construction & Vectorstore Caching
8. Retrieval-Augmented Generation
9. Model Tiering (`gpt-4o-mini` & `gpt-4.1`)
10. Safety Guardrails & Conditional Workflow Routing
11. Wikipedia Integration
12. Multi-Turn Query Contextualization
13. Direct Meta-Conversational Chat Handling

Each iteration was tested independently before integration into the complete system.

---

## Future Improvements

Potential enhancements include:

- Multi-document knowledge base
- Persistent conversation database across sessions
- Citation of retrieved sources
- Hybrid dense & sparse search (BM25 + ChromaDB)
- User authentication
- Docker deployment

---

## Author

**Ng Chee Wee**

Large Language Model Applications (LLMA)

Ngee Ann Polytechnic
