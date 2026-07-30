# EngagePro Chatbot

An AI-powered customer support chatbot developed as part of the **Large Language Model Applications (LLMA)** module at **Ngee Ann Polytechnic**.

The chatbot answers **EngagePro-specific questions** using Retrieval-Augmented Generation (RAG) and responds to **general or technical questions** using information retrieved from Wikipedia before generating a natural language response.

---

## Project Overview

The objective of this project is to develop an interactive chatbot capable of engaging in natural language conversations while providing accurate and grounded responses.

The chatbot combines:

- Retrieval-Augmented Generation (RAG) for company knowledge
- Wikipedia retrieval for general and technical knowledge
- LangGraph for workflow orchestration
- Streamlit for the web interface
- OpenAI GPT models for response generation

---

## Features

- Interactive Streamlit chat interface
- EngagePro knowledge base using RAG
- Chroma vector database
- OpenAI embeddings
- LangGraph workflow orchestration
- LLM-based routing agent
- Wikipedia integration for general knowledge
- Conversation history using LangGraph `MessagesState`
- Prompt engineering to minimise hallucinations

---

## System Architecture

```
                    User
                      │
                      ▼
                Streamlit UI
                      │
                      ▼
              LangGraph Workflow
                      │
                      ▼
              Routing Agent (LLM)
               /              \
              /                \
             ▼                  ▼
     EngagePro Questions   General Questions
             │                  │
             ▼                  ▼
        ChromaDB (RAG)     Wikipedia API
             │                  │
             ▼                  ▼
       Prompt Builder     Prompt Builder
             └────────────┬────────────┘
                          ▼
                       GPT-4.1
                          ▼
                    Final Response
```

---

## Project Structure

```
engagepro_chatbot/
│
├── app.py
├── config.py
├── graph/
├── llm/
├── prompts/
├── rag/
├── routing/
├── wiki/
├── scripts/
├── tests/
├── docs/
├── data/
└── requirements.txt
```

---

## Technology Stack

| Component | Technology |
|----------|------------|
| Programming Language | Python 3.11 |
| User Interface | Streamlit |
| LLM | OpenAI GPT-4.1 |
| Framework | LangChain |
| Workflow | LangGraph |
| Vector Database | ChromaDB |
| Embeddings | text-embedding-3-small |
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

Launch the chatbot:

```bash
streamlit run app.py
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

---

## Development Journey

The project was developed incrementally through multiple iterations:

1. Assignment Analysis
2. System Architecture
3. Environment Setup
4. Streamlit MVP
5. PDF Loading
6. Document Chunking
7. Knowledge Base Construction
8. Retrieval-Augmented Generation
9. Routing Agent
10. Conditional Workflow Routing
11. Wikipedia Integration

Each iteration was tested independently before integration into the complete system.

---

## Future Improvements

Potential enhancements include:

- Multi-document knowledge base
- Conversation summarisation
- Citation of retrieved sources
- Support for additional knowledge sources
- User authentication
- Chat history persistence
- Docker deployment

---

## Author

**Ng Chee Wee**

Large Language Model Applications (LLMA)

Ngee Ann Polytechnic