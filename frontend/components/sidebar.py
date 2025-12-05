import streamlit as st
from frontend.services.api_client import trigger_indexing

def render_sidebar():
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=50)
        st.title("PyTeach Settings")
        
        st.markdown("---")
        st.subheader("Knowledge Base")
        
        if st.button("Refresh Knowledge Base"):
            with st.spinner("Requesting indexing..."):
                if trigger_indexing():
                    st.success("Indexing started!")
                else:
                    st.error("Failed to connect to backend.")
        
        st.markdown("---")
        st.info(
            """
            About PyTeach
            
            An AI Assistant for ASTU Freshman Students learning Python 2.7.
            
            Ask about:
            - Loops & Conditionals
            - cs1robots
            - cs1media
            """
        )