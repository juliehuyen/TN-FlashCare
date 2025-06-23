import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
BASE_API_URL = os.getenv("BASE_API_URL", "http://127.0.0.1:8004")

st.set_page_config(page_title="Ordonnance & Chat IA", layout="centered")
st.title("Ordonnance")

st.markdown("""
<style>
/* Bouton bleu "Expliquer" */
div.stButton > button {
    background-color: #4DAFEB !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.45rem 1rem !important;
    font-weight: 600 !important;
    transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
}

div.stButton > button:hover {
    background-color: #3b99d1 !important;
    color: white !important;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)



# --- Patient Info ---
st.markdown(
    """**Patient :** Jean Dupont  
    **Date de naissance :** 12/03/1975  
    **Date de consultation :** 16/06/2025"""
)
st.markdown("---")


# --- 1) Compte Rendu d'Examen ---
st.subheader("Compte Rendu d'Examen")
st.markdown("""
**Motif de la consultation**  
M. Dupont s’est présenté pour des brûlures mictionnelles, pollakiurie et légère douleur sus-pubienne évoluant depuis 48 heures.

**Diagnostic**  
Cystite aiguë simple sans signe de complication (pyélonéphrite) confirmée par la bandelette.
""")

st.markdown("---")

# --- Prescription Explanation Section ---

# Sample prescription data
if "prescriptions" not in st.session_state:
    st.session_state.prescriptions = [
        {"id": 1, "medicament": "Paracétamol",  "dose": "500 mg", "frequence": "3×/jour"},
        {"id": 2, "medicament": "Ibuprofène",   "dose": "200 mg", "frequence": "2×/jour"},
        {"id": 3, "medicament": "Amoxicilline", "dose": "1 g",    "frequence": "2×/jour"},
    ]
# Explanations toggle state
if "explanations" not in st.session_state:
    st.session_state.explanations = {}

st.subheader("Préscription médicale")

for idx, pres in enumerate(st.session_state.prescriptions):
    med = pres["medicament"]
    dose = pres["dose"]
    freq = pres["frequence"]

    # Deux colonnes : une large pour le texte, une petite pour le bouton
    col_text, col_button = st.columns([4, 1])

    with col_text:
        st.markdown(
            f"<span style='font-size:1.1rem; font-weight:500;'>{med} | {dose} | {freq}</span>",
            unsafe_allow_html=True
        )

    with col_button:
        if st.button("Expliquer", key=f"exp_{idx}"):
            if idx in st.session_state.explanations:
                st.session_state.explanations.pop(idx)
            else:
                explanation = (
                    f"**{med}** sert à soulager la douleur et la fièvre.\n\n"
                    f"- **Dose** : {dose}\n"
                    f"- **Fréquence** : {freq}\n"
                    "- **Effets secondaires** : nausées, maux d'estomac.\n"
                    "- **Conseil** : à prendre après le repas."
                )
                st.session_state.explanations[idx] = explanation

    # Affichage de l'explication en dessous
    if idx in st.session_state.explanations:
        st.markdown(st.session_state.explanations[idx])
    st.markdown("---")



# --- 2) Chat mock IA ---
st.subheader("💬 Une question sur votre ordonnance ? Demandez à notre IA !")
# Initialize conversation
if "conv_id" not in st.session_state:
    # Create new conversation
    resp = requests.post(f"{BASE_API_URL}/conversation")
    if resp.ok:
        st.session_state.conv_id = resp.json().get("conversation_id")
    else:
        st.error("Impossible de créer une conversation.")
        st.stop()

# Load history
def fetch_history(conv_id):
    r = requests.get(f"{BASE_API_URL}/conversation/{conv_id}")
    return r.json().get("history", []) if r.ok else []

history = fetch_history(st.session_state.conv_id)
if "messages" not in st.session_state:
    st.session_state.messages = history

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["message"])

# User input
if prompt := st.chat_input("Posez votre question sur l'ordonnance..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "message": prompt})
    # Send to backend
    r = requests.post(
        f"{BASE_API_URL}/conversation/{st.session_state.conv_id}",
        json={"prompt": prompt}
    )
    if r.ok:
        history = r.json().get("history", [])
        # Find latest assistant message
        bot_msg = next((m["message"] for m in reversed(history) if m["role"] == "assistant"), "")
    else:
        bot_msg = "Désolé, je n'ai pas pu répondre."
    st.chat_message("assistant").write(bot_msg)
    st.session_state.messages.append({"role": "assistant", "message": bot_msg})