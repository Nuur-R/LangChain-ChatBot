import os
import streamlit as st
from dotenv import load_dotenv
from langchain_chatbot import create_chatbot

# Load environment variables
load_dotenv()

def main():
    # Set up UI
    st.title("LangChain Chatbot with Groq and Streamlit")
    st.write("This is a chatbot powered by LangChain and Groq.")

    # Initialize chatbot
    chatbot = create_chatbot()

    # Conversation history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # User input
    user_input = st.text_input("Ask a question:", "")

    if st.button("Send"):
        if user_input:
            # Get response from chatbot
            response = chatbot(user_input)
            # Append response to chat history
            st.session_state["chat_history"].append((user_input, response))

    # Display chat history
    if st.session_state["chat_history"]:
        for user_input, response in st.session_state["chat_history"]:
            st.write(f"**You**: {user_input}")
            st.write(f"**Chatbot**: {response}")

if __name__ == "__main__":
    main()
