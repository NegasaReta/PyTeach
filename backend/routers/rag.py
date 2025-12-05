from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.rag_pipeline import process_query

router = APIRouter()

class QueryRequest(BaseModel):
    text: str

class QueryResponse(BaseModel):
    answer: str
    sources: list

@router.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    """
    Endpoint to ask a question to the RAG system.
    """
    if not request.text:
        raise HTTPException(status_code=400, detail="Query text cannot be empty")
    
    try:
        result = process_query(request.text)
        return QueryResponse(answer=result["answer"], sources=result["sources"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))