import sys
from dotenv import load_dotenv
import os
import streamlit as st
import requests
# Ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from chat_service.rest.model.chat_request import ChatRequest

from env_config import EnvConfig

BASE_API_URL = EnvConfig.get_api_url()

# Fonction pour gérer les appels API
def api_request(method, url, data=None):
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error during API call: {e}")
        return None

# Fonction pour créer une nouvelle conversation
def create_new_conversation():
    url = f"{BASE_API_URL}/conversation"
    response = api_request("POST", url)
    return response.get("conversation_id") if response else None

# Fonction pour créer une conversation par défaut
def create_default_conversation():
    new_conv_id = create_new_conversation()
    if new_conv_id:
        st.session_state["conv_id"] = new_conv_id
        st.session_state["messages"] = [{"role": "assistant", "message": "How can I help you?"}]
    else:
        st.error("Unable to create a new default conversation.")

# Fonction pour récupérer l'historique de la conversation
def get_conversation_history(conv_id):
    url = f"{BASE_API_URL}/conversation/{conv_id}"
    response = api_request("GET", url)
    if response and "history" in response:
        return response["history"]
    st.error("The API response is not in the expected format.")
    return []

# Fonction pour gérer l'entrée utilisateur
def handle_user_input(prompt):
    st.session_state.messages.append({"role": "user", "message": prompt})
    st.chat_message("user").write(prompt)

    url = f"{BASE_API_URL}/conversation/{st.session_state['conv_id']}"
    request = ChatRequest(prompt=prompt)
    response = api_request("POST", url, data=request.to_dict())

    if response and "history" in response:
        history = response["history"]
        bot_response = next(
            (msg["message"] for msg in reversed(history) if msg["role"] == "assistant"),
            "I didn't understand that."
        )
    else:
        bot_response = "I didn't understand that."

    st.session_state.messages.append({"role": "assistant", "message": bot_response})
    st.chat_message("assistant").write(bot_response)

# Initialisation de la session
if "conv_id" not in st.session_state:
    create_default_conversation()
if "conv_id" not in st.session_state:
    st.session_state["conv_id"] = None
    
# Titre et description de l'application
st.title("💬 Chatbot")
st.caption("🚀 My First Chatbot using Cohere")

# Barre latérale avec description
with st.sidebar:
    st.markdown("""
        This page demonstrates how to create a memory-enabled chatbot using Cohere, showcasing
        the integration of advanced NLP capabilities in a user-friendly interface. Explore the 
        examples and learn how to build your own intelligent applications.     
    """)
    st.header("📚 Learn More")
    st.markdown("""Explore the examples and learn how to build your own intelligent applications.
        [Cohere API](https://docs.cohere.com/reference/chat)""")
    st.markdown("---")
    if st.button("New Conversation"):
        new_conv_id = create_new_conversation()
        if new_conv_id:
            st.session_state["conv_id"] = new_conv_id
            st.session_state["messages"] = [{"role": "assistant", "message": "Welcome! How can I assist you today?"}]

st.markdown("""
    On this demonstration we will be able to send request to Cohere and have a chat with history.
""")

# Initialiser et afficher l'historique de la conversation
if st.session_state["conv_id"]:
    history = get_conversation_history(st.session_state["conv_id"])
    st.session_state["messages"] = history if history else []
else:
    st.session_state["messages"] = []

# Afficher les messages existants
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["message"])

# Gestion de l'entrée utilisateur
if prompt := st.chat_input():
    handle_user_input(prompt)



