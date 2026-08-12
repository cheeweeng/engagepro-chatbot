"""
Application configuration settings.
"""

from pathlib import Path

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ------------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).parent

DATA_DIR = PROJECT_ROOT / "data"

BROCHURE_FILE = DATA_DIR / "Company_Brochure.pdf"

VECTORSTORE_ROOT = PROJECT_ROOT / "vectorstore"

CHROMA_DB_DIR = VECTORSTORE_ROOT / "chroma"

# ------------------------------------------------------------------
# LLM
# ------------------------------------------------------------------

LLM_PROVIDER = "openai"

MODEL_NAME = "gpt-4.1" # reasoning model for response generation

TEMPERATURE = 0.2

FAST_MODEL_NAME = "gpt-4o-mini" # for Safety checks and query intent classification

# ------------------------------------------------------------------
# Embeddings
# ------------------------------------------------------------------

EMBEDDING_MODEL = "text-embedding-3-small"

# ------------------------------------------------------------------
# RAG
# ------------------------------------------------------------------

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

COLLECTION_NAME = "engagepro"