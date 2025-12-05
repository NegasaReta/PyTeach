PyTeach – AI-Powered Python Learning Assistant

PyTeach is an interactive Retrieval-Augmented Generation (RAG) learning assistant designed to help students understand Python programming concepts using real lecture materials. The system combines FastAPI, Streamlit, ChromaDB, and LLMs (Ollama/OpenAI) to deliver accurate, context-aware explanations from your uploaded course notes.

🚀 Features

📘 Uses 16+ Python lecture PDFs as the knowledge source.

🔍 Fast and accurate retrieval with ChromaDB vector database.

🤖 AI-powered explanations, summaries, quizzes, and examples.

💬 Clean chat-based interface built with Streamlit.

⚡ Backend powered by FastAPI for modularity and scalability.

🧩 Structured RAG pipeline: chunking → embeddings → retrieval → LLM answer.

🔄 Easy to update: add/remove PDFs anytime.

🏗️ Tech Stack

Frontend: Streamlit

Backend: FastAPI

Vector Store: ChromaDB

Embeddings: Sentence Transformers

LLM: Ollama or OpenAI API

Processing: PyPDF

📁 Project Structure
PyTeach/
│── backend/        # FastAPI backend
│── frontend/       # Streamlit UI
│── core/           # RAG pipeline and helpers
│── documents/      # Lecture PDFs
│── data/chroma/    # Vector database
└── README.md

▶️ Getting Started

Install dependencies:

pip install -r requirements.txt


Start the backend:

uvicorn backend.main:app --reload


Launch the Streamlit app:

streamlit run frontend/app.py

🎯 Purpose

PyTeach is designed to make Python learning intuitive, interactive, and personalized by grounding all explanations in your actual lecture notes.

Perfect for students, tutors, and classrooms.