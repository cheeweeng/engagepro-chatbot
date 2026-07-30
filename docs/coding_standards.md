# EngagePro Chatbot
## Coding Standards

This document defines the coding standards followed throughout the EngagePro Chatbot project.

---

# 1. General Principles

- Keep the design simple and maintainable.
- Implement features in small, testable increments.
- Follow the Single Responsibility Principle whenever practical.
- Prefer readability over clever code.

---

# 2. Python Style

- Follow PEP 8.
- Use descriptive variable and function names.
- Avoid hard-coded values.
- Use constants defined in `config.py`.

Example:

```python
MAX_RESULTS = 5
```

instead of

```python
results = search(query, 5)
```

---

# 3. Type Hints

Use type hints for all public functions.

Example:

```python
def get_llm() -> BaseChatModel:
```

---

# 4. Docstrings

Every public module, class and function should include a concise docstring.

Example:

```python
def get_llm() -> BaseChatModel:
    """
    Create and return the configured language model.
    """
```

---

# 5. Project Structure

- UI code belongs in `app.py`
- Workflow belongs in `graph/`
- LLM configuration belongs in `llm/`
- Retrieval logic belongs in `rag/`
- Utility functions belong in `utils/`

Avoid mixing responsibilities.

---

# 6. Configuration

Store configuration in `config.py`.

Secrets must never be hard-coded.

Store API keys in `.env`.

---

# 7. Paths

Use `pathlib.Path`.

Do not hard-code Windows file paths.

Example:

```python
DATA_DIR = PROJECT_ROOT / "data"
```

---

# 8. LangGraph

Use `MessagesState` for conversation state.

Avoid custom state unless additional fields are required.

---

# 9. Testing

Every new feature should be tested immediately after implementation.

Develop using:

Design → Code → Test → Verify

---

# 10. Error Handling

Raise meaningful exceptions.

Avoid silent failures.

Provide informative error messages.

---

# 11. Version Control

Commit after completing each successful iteration.

Use meaningful commit messages.

Example:

```
feat: integrate LangGraph with Streamlit chat interface
```

---

# 12. Documentation

Document significant architectural decisions.

Update the project notebook after each completed iteration.

# 13. AI Development Principles

- Minimise hallucinations by grounding answers with RAG whenever appropriate.
- Prefer deterministic behaviour over unnecessary creativity.
- Add AI features only when they provide clear value.
- Keep prompts concise and maintainable.
- Explainable design is preferred over complex workflows.