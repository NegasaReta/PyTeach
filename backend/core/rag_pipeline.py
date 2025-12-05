from langchain_core.prompts import PromptTemplate
from langchain_community.chains import RetrievalQA

from backend.core.llm import get_llm
from backend.core.chroma_db import get_retriever
from backend.config import settings

def get_rag_chain():
    """
    Constructs the RAG pipeline: Retriever -> Prompt -> LLM.
    """
    llm = get_llm()
    retriever = get_retriever()

    # Custom prompt template incorporating the System Prompt
    template = settings.SYSTEM_PROMPT + """
    
    Context from lecture notes and documentation:
    {context}
    
    Student Question: {question}
    
    Answer (in Python 2.7 context):
    """
    
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    
    return qa_chain

def process_query(query: str):
    """
    Executes the RAG chain for a single query.
    """
    chain = get_rag_chain()
    result = chain.invoke({"query": query})
    
    response = {
        "answer": result["result"],
        "sources": [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]
    }
    return response