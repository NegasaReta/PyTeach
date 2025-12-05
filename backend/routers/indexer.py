from fastapi import APIRouter, BackgroundTasks
from backend.core.document_loader import process_and_index

router = APIRouter()

@router.post("/refresh")
async def refresh_index(background_tasks: BackgroundTasks):
    """
    Triggers the document indexing process in the background.
    """
    background_tasks.add_task(process_and_index)
    return {"message": "Indexing started in the background."}