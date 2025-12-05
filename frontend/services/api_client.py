import requests
import os

API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def get_answer(question: str):
    """
    Sends a question to the FastAPI backend and retrieves the answer.
    """
    try:
        response = requests.post(
            f"{API_URL}/api/rag/ask",
            json={"text": question},
            timeout=60 # LLMs can be slow
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"answer": "Error: Unable to get response from server.", "sources": []}
    except requests.exceptions.RequestException as e:
        return {"answer": f"Connection Error: {str(e)}", "sources": []}

def trigger_indexing():
    """
    Triggers the backend to re-index documents.
    """
    try:
        response = requests.post(f"{API_URL}/api/index/refresh")
        return response.status_code == 200
    except:
        return False