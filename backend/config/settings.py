import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCUMENTS_DIR = BASE_DIR / "documents"
CHROMA_DB_DIR = BASE_DIR / "data" / "chroma"

# Create dirs if they don't exist
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_DB_DIR.mkdir(parents=True, exist_ok=True)

# Application Settings
APP_NAME = "PyTeach"
VERSION = "1.0.0"
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

# Vector Store Settings
COLLECTION_NAME = "pyteach_knowledge_base"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# LLM Settings
# Options: "ollama", "openai"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama") 

# Ollama Settings
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2") # or mistral

# OpenAI Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-3.5-turbo"

# Retrieval Settings
TOP_K_RETRIEVAL = 5

# System Prompt
SYSTEM_PROMPT = """You are PyTeach, an AI teaching assistant for ASTU freshman students learning Python 2.7 programming.
Your role:
- Explain concepts in simple, clear language.
- Provide accurate Python 2.7 syntax (PRINT is a statement, not a function).
- Help with cs1robots, cs1media, and cs1graphics libraries.
- Be patient and encouraging.
- Use Ethiopian context and examples when helpful.
- Do NOT provide complete assignment solutions.
- If the context doesn't contain the answer, say so and provide general guidance based on Python 2.7 standards.
"""