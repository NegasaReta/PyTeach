from fastapi import FastAPI
from backend.routers import rag, indexer
from backend.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend API for PyTeach RAG System"
)

# Include Routers
app.include_router(rag.router, prefix="/api/rag", tags=["RAG"])
app.include_router(indexer.router, prefix="/api/index", tags=["Indexer"])

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.APP_NAME} API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host=settings.API_HOST, port=settings.API_PORT, reload=True)