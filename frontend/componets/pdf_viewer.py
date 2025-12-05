import streamlit as st
import os
import base64
from pathlib import Path

# Config
DOCUMENTS_DIR = Path("documents")

def display_pdf(file_path):
    """
    Embeds a PDF in the Streamlit app using an HTML iframe.
    """
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # PDF embedding via HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def render_pdf_viewer():
    """
    Renders the PDF viewer section in the frontend.
    """
    st.header("📚 Course Materials")
    
    # Ensure directory exists
    if not DOCUMENTS_DIR.exists():
        st.warning(f"Documents directory not found at {DOCUMENTS_DIR}")
        return

    # List PDF files
    pdf_files = [f for f in os.listdir(DOCUMENTS_DIR) if f.endswith('.pdf')]
    
    if not pdf_files:
        st.info("No lecture PDFs found in the documents folder.")
        return

    # Selection Dropdown
    selected_pdf = st.selectbox("Select a Lecture to View", pdf_files)

    if selected_pdf:
        file_path = DOCUMENTS_DIR / selected_pdf
        st.markdown(f"Viewing: {selected_pdf}")
        display_pdf(file_path)