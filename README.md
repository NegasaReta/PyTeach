PyTeach/
│
├── backend/
│   ├── main.py                      # FastAPI root app (API endpoints)
│   ├── routers/
│   │   ├── rag.py                   # /ask, /search, /generate API routes
│   │   └── indexer.py               # /index, /refresh endpoints
│   │
│   ├── core/
│   │   ├── document_loader.py       # PDF reading, splitting, chunking
│   │   ├── chroma_db.py             # ChromaDB init, store, query
│   │   ├── embeddings.py            # Embedding model loading & generation
│   │   ├── rag_pipeline.py          # Retrieval-Augmented Generation logic
│   │   ├── llm.py                   # Ollama / OpenAI wrapper
│   │   └── utils.py                 # Helpers (cleaning, chunking, timing)
│   │
│   └── config/
│       ├── settings.py              # App config, paths, model names
│       └── secrets.env              # API keys, env variables (gitignored)
│
├── frontend/
│   ├── app.py                       # Streamlit UI
│   ├── components/
│   │   ├── sidebar.py               # Navigation UI
│   │   ├── chat_box.py              # Chat window UI
│   │   └── pdf_viewer.py            # PDF preview components
│   └── services/
│       └── api_client.py            # Wrapper to call FastAPI backend
│
├── documents/
│   ├── lecture1.pdf
│   ├── lecture2.pdf
│   ├── ...
│   └── lecture16.pdf                # All learning materials
│
├── data/
│   └── chroma/                      # ChromaDB vector store (auto-created)
│
├── tests/
│   ├── test_rag.py                  # Test retrieval and generation
│   ├── test_embeddings.py           # Test embedding generation
│   └── test_api.py                  # Test FastAPI endpoints
│
├── scripts/
│   ├── init_chroma.py               # Script to create fresh ChromaDB
│   ├── index_all_pdfs.py            # Run once to index the 16 PDF lectures
│   └── backup_vectors.py            # Backup vector DB script
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── .gitignore                       # Ignore cache, vector DB, secrets
└── start.sh                         # Script to run backend + frontend
