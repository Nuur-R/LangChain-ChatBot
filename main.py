import os
import streamlit as st
from dotenv import load_dotenv
from langchain_chatbot import create_chatbot

# Load environment variables
load_dotenv()

def main():
    # Set up UI
    st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖")

    st.title("🤖 LangChain Chatbot with Groq and Streamlit")
    st.write("Ask me anything! I'm powered by LangChain and Groq's LLM.")

    # Initialize chatbot
    chatbot = create_chatbot()

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Display chat history using st.chat_message
    for message in st.session_state["chat_history"]:
        with st.chat_message(message["role"]):  # role can be "user" or "assistant"
            st.markdown(message["content"])

    # Chat input area
    user_input = st.chat_input("Ask a question...")

    if user_input:
        # Display user message instantly
        with st.chat_message("user"):
            st.markdown(user_input)

        # Store user message in session state
        st.session_state["chat_history"].append({"role": "user", "content": user_input})

        # Status indicator: Chatbot is "thinking"
        with st.status("Thinking..."):
            # Get chatbot response
            response = chatbot(user_input)

        # Display chatbot response
        with st.chat_message("assistant"):
            st.markdown(response)

        # Store assistant response in session state
        st.session_state["chat_history"].append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
