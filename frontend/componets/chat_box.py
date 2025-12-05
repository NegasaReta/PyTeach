import streamlit as st
from frontend.services.api_client import get_answer

def render_chat():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask a Python 2.7 question..."):
        # Display user message
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response_data = get_answer(prompt)
                answer = response_data.get("answer", "Sorry, I encountered an error.")
                sources = response_data.get("sources", [])
                
                st.markdown(answer)
                
                if sources:
                    with st.expander("View Sources"):
                        for source in set(sources):
                            st.caption(f"📄 {source}")

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})