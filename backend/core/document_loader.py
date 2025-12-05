import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from backend.config import settings

def load_documents() -> List[Document]:
    """
    Loads all PDF documents from the documents directory.
    """
    print(f"Loading documents from {settings.DOCUMENTS_DIR}")
    
    # Check if directory is empty
    if not os.listdir(settings.DOCUMENTS_DIR):
        print("No documents found to index.")
        return []

    loader = DirectoryLoader(
        str(settings.DOCUMENTS_DIR),
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")
    return documents

def split_documents(documents: List[Document]) -> List[Document]:
    """
    Splits documents into smaller chunks for embedding.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")
    return chunks

def process_and_index():
    """
    Orchestrates the loading, splitting, and indexing process.
    """
    docs = load_documents()
    if not docs:
        return {"status": "empty", "message": "No documents found"}
        
    chunks = split_documents(docs)
    
    from backend.core.chroma_db import get_vector_store
    vector_store = get_vector_store()
    
    # Add to vector store
    vector_store.add_documents(chunks)
    vector_store.persist()
    
    return {"status": "success", "chunks_indexed": len(chunks)}