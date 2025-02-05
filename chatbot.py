import streamlit as st                          # Create interactive web application
from streamlit_chat import message              # Display the chat messages
from dotenv import load_dotenv                  # Load the open API key from the environment variable
import os                                       # Access the environment variable
from langchain.chat_models import ChatOpenAI    # Import the ChatOpenAI model
from langchain.schema import SystemMessage, HumanMessage, AIMessage # Import the message schema


def init():       # Initialize the Streamlit app

    
    load_dotenv() # Load the OpenAI API key from the environment variable

    # Test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("OPENAI_API_KEY is not set. Please set it in your environment variables.")
        st.stop()  # Safely stop the Streamlit app

    # Setup Streamlit page
    st.set_page_config(
        page_title="Chat Bot With OpenAI",
        page_icon="🤖"
    )


def main():    # Main function
    init()     # Initialize the Streamlit app

    # Initialize the ChatOpenAI model
    chat = ChatOpenAI(
        model = 'gpt-3.5-turbo',  # Use the GPT-3.5-turbo model
        temperature=0.5)  # Set the temperature to 0.5 for more diverse responses

    # Initialize message history
    if "messages" not in st.session_state: 
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.Give the answer with simple english") # Initial system message for the message Schema
        ]

    st.header("OpenAI Chatbot 🤖")

    # Sidebar with user input
    with st.sidebar:
        user_input = st.text_input("Enter Your Question:", key="user_input") # User input field

        # Handle user input
        if user_input:
            # Add the user's message to the message history
            st.session_state.messages.append(HumanMessage(content=user_input))

            with st.spinner("Thinking..."):
                # Generate a response from the chat model
                response = chat(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content)) # Add the AI's response to the message history

    # Display message history
    for i, msg in enumerate(st.session_state.messages[1:]):  # Skip the initial system message
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=f"{i}_user")
        elif isinstance(msg, AIMessage):
            message(msg.content, is_user=False, key=f"{i}_ai")


if __name__ == '__main__':   # Run the main function
    main()                   # Call the main function
