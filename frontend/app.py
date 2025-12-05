import streamlit as st
from frontend.components.sidebar import render_sidebar
from frontend.components.chat_box import render_chat

st.set_page_config(
    page_title="PyTeach - ASTU Assistant",
    page_icon="🐍",
    layout="wide"
)

def main():
    st.title("🐍 PyTeach: Python 2.7 Assistant")
    st.markdown("Welcome! I can help you with **Python 2.7**, **cs1robots**, and **cs1media**.")

    # Render Components
    render_sidebar()
    render_chat()

if __name__ == "__main__":
    main()