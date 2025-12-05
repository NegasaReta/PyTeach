#!/bin/bash

# Start the Backend in the background
echo "Starting FastAPI Backend..."
python -m backend.main &

# Wait for backend to initialize (simple sleep for demo)
sleep 5

# Start the Frontend
echo "Starting Streamlit Frontend..."
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
