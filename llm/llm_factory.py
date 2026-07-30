"""
Factory for creating LLM instances.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from config import LLM_PROVIDER, MODEL_NAME, TEMPERATURE

# Load environment variables
load_dotenv()


def get_llm():
    """
    Return the configured language model.
    """

    if LLM_PROVIDER == "openai":
        return ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
        )

    raise ValueError(f"Unsupported provider: {LLM_PROVIDER}")