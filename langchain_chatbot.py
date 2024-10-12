import os
from groq import Groq
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

def create_chatbot():
    """
    Creates the LangChain chatbot with Groq as the LLM backend.
    """
    # Get Groq API key
    groq_api_key = os.getenv("GROQ_API_KEY")
    model = 'llama3-8b-8192'

    # Initialize Groq Langchain chat object
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)

    # Define system prompt and memory
    system_prompt = 'You are a friendly conversational chatbot'
    conversational_memory_length = 5

    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    # Define chat prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )

    # Create conversation chain
    conversation = LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )

    # Define chatbot function
    def chatbot(user_input):
        return conversation.predict(human_input=user_input)
    
    return chatbot
