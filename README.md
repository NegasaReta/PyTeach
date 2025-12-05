# 🐍 PyTeach – AI-Powered Python Learning Assistant

> *Learn Python the smart way, guided by your course materials and real AI insights.*

---

```
PyTeach is your personal RAG-powered Python mentor.
It helps you master Python concepts,
using your lecture notes as the source.
```

---

## 🚀 Core Features

- `📘` **16+ Python Lecture PDFs:** Your own syllabus becomes the knowledge base.
- `🔍` **Smart & Blazing-Fast Retrieval:** Powered by ChromaDB vector search.
- `🤖` **AI Explanations, Summaries, Quizzes & Examples:** Ask anything!
- `💬` **Chat UI:** Beautiful, intuitive Streamlit-driven conversations.
- `⚡` **Modern API Backend:** Modular & scalable with FastAPI.
- `🧩` **Structured RAG Pipeline:**
  - Chunking → Embeddings → Retrieval → LLM Answers
- `🔄` **Easy Content Upgrades:** Add or remove PDFs anytime.

---

## 🏗️ Tech Stack

```plaintext
Frontend      : Streamlit
Backend       : FastAPI
Vector Store  : ChromaDB
Embeddings    : Sentence Transformers
LLM Engine    : Ollama / OpenAI API
PDF Parsing   : PyPDF
```

---

## 📦 Project Structure

```plaintext
PyTeach/
├── backend/        # FastAPI backend
├── frontend/       # Streamlit UI
├── core/           # RAG pipeline & helpers
├── documents/      # Lecture PDFs
├── data/chroma/    # Vector database
└── README.md
```

---

## ▶️ Quickstart

1. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
2. **Start the backend**
    ```bash
    uvicorn backend.main:app --reload
    ```
3. **Launch the Streamlit app**
    ```bash
    streamlit run frontend/app.py
    ```

---

## 🎯 Why PyTeach?

- *Stop searching random content online.*  
  PyTeach trains exclusively on your lecture notes for **personalized, relevant answers**.
- *Instant code examples and interactive quizzes.*
- *Perfect for:* Students, Tutors, Classrooms.

---

### ⭐ Explore. Learn. Master Python with PyTeach!

```
Learning Python should be intuitive and grounded,
with answers that match your course.
PyTeach makes Python learning interactive, accurate and fun!
```
