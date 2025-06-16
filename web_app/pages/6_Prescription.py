import streamlit as st

st.set_page_config(page_title="Ordonnance & Chat IA", layout="centered")
st.title("📋 Ordonnance")

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
    med  = pres["medicament"]
    dose = pres["dose"]
    freq = pres["frequence"]
    c1, c2 = st.columns([4, 1])
    with c1:
        st.text(f"- {med} | {dose} | {freq}")
    with c2:
        if st.button("Expliquer", key=f"exp_{idx}"):
            if idx in st.session_state.explanations:
                st.session_state.explanations.pop(idx)
            else:
                # Mock explanation
                explanation = (
                    f"**{med}** sert à soulager la douleur et la fièvre.\n\n"
                    f"- **Dose** : {dose}\n"
                    f"- **Fréquence** : {freq}\n"
                    "- **Effets secondaires** : nausées, maux d'estomac.\n"
                    "- **Conseil** : à prendre après le repas."
                )
                st.session_state.explanations[idx] = explanation
    if idx in st.session_state.explanations:
        st.markdown(st.session_state.explanations[idx])
        st.markdown("---")

# --- 2) Chat mock IA ---
st.subheader("💬 Chat IA sur votre ordonnance")

# Initialisation de l'historique
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Affichage des messages
for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["message"])

# Saisie utilisateur
if prompt := st.chat_input("Posez votre question…"):
    # Ajout du message utilisateur
    st.session_state.chat_history.append({"role": "user", "message": prompt})
    st.chat_message("user").write(prompt)

    # Réponse mock
    bot_response = "ℹ️ Ceci est une réponse simulée de l'IA concernant votre ordonnance."
    st.session_state.chat_history.append({"role": "assistant", "message": bot_response})
    st.chat_message("assistant").write(bot_response)

