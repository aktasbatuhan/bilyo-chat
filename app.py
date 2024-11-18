import streamlit as st
import requests
import json
from typing import Dict, List
import uuid
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
API_BASE_URL = os.getenv('API_BASE_URL', 'http://94.141.99.80:8080')


def create_new_chat() -> str:
    """Create a new chat session and return the session ID."""
    response = requests.get(f"{API_BASE_URL}/newchat")
    if response.status_code == 200:
        return response.json()['session_id']
    raise Exception("Failed to create new chat session")

def send_message(session_id: str, message: str) -> Dict:
    """Send a message to the chat API and return the response."""
    response = requests.post(
        f"{API_BASE_URL}/chat/{session_id}",
        json={"query": message}
    )
    if response.status_code == 200:
        return response.json()
    raise Exception("Failed to send message")

def get_session_history(session_id: str) -> List[Dict]:
    """Retrieve chat history for a specific session."""
    response = requests.get(f"{API_BASE_URL}/session/{session_id}")
    if response.status_code == 200:
        return response.json()['messages']
    raise Exception("Failed to retrieve session history")

def main():
    st.title("Chat Interface")
    
    # Initialize session state
    if 'session_id' not in st.session_state:
        st.session_state.session_id = create_new_chat()
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        # Load existing messages if any
        try:
            st.session_state.messages = get_session_history(st.session_state.session_id)
        except Exception as e:
            st.error(f"Error loading chat history: {str(e)}")

    # Display chat messages
    for message in st.session_state.messages:
        role = "assistant" if message.get("role") == "assistant" else "user"
        with st.chat_message(role):
            st.write(message.get("content"))

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        try:
            # Get bot response
            response = send_message(st.session_state.session_id, prompt)
            assistant_message = response.get("response", "No response received")
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.write(assistant_message)
        
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Add a button to start a new chat
    if st.sidebar.button("Start New Chat"):
        st.session_state.session_id = create_new_chat()
        st.session_state.messages = []
        st.rerun()

    # Display current session ID in sidebar
    st.sidebar.text(f"Session ID: {st.session_state.session_id}")

if __name__ == "__main__":
    main()