import chromadb
from langchain import Chroma
from backend.config import settings
from backend.core.embeddings import get_embedding_model

def get_vector_store():
    """
    Initializes and returns the ChromaDB vector store.
    """
    embedding_function = get_embedding_model()
    
    vector_store = Chroma(
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embedding_function,
        persist_directory=str(settings.CHROMA_DB_DIR)
    )
    
    return vector_store

def get_retriever():
    """
    Returns the vector store as a retriever object.
    """
    vector_store = get_vector_store()
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": settings.TOP_K_RETRIEVAL}
    )