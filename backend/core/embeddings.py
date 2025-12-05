from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.config import settings

def get_embedding_model():
    """
    Loads the HuggingFace embedding model specified in settings.
    This model is used to convert text into vector representations.
    """
    print(f"Loading embedding model: {settings.EMBEDDING_MODEL_NAME}")
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL_NAME
    )
    return embeddings