"""
Factory for creating LLM instances.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from config import LLM_PROVIDER, MODEL_NAME, FAST_MODEL_NAME, TEMPERATURE

# Load environment variables
load_dotenv()


def get_llm(tier: str = "default"):
    """
    Return the configured language model.
    Args:
            tier: "default" for main generation (e.g. gpt-4.1)
                  or "fast" for lightweight classification tasks (e.g. gpt-4o-mini).
    """

    model_name = FAST_MODEL_NAME if tier == "fast" else MODEL_NAME
    
    if LLM_PROVIDER == "openai":
        return ChatOpenAI(
            model=model_name,
            temperature=TEMPERATURE,
        )

    raise ValueError(f"Unsupported provider: {LLM_PROVIDER}")