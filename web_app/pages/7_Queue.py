import streamlit as st
import requests

st.set_page_config(page_title="📝 File d’attente patients")

st.title("📝 File d'attente actuelle")

QUEUE_URL = "http://localhost:8003/queue"

try:
    response = requests.get(QUEUE_URL)
    response.raise_for_status()
    queue = response.json()

    if not queue:
        st.info("La file d'attente est vide.")
    else:
        for i, patient in enumerate(queue, start=1):
            st.subheader(f"{i}. {patient['patient_id']}")
            st.markdown(f"**Score:** {patient['triage_score']:.2f}")
            st.markdown(f"**Niveau:** {patient['triage_level'].capitalize()}")
            st.markdown(f"**Explication:** {patient['explanation']}")
            st.markdown("---")

except Exception as e:
    st.error(f"Erreur lors de la récupération de la file d'attente : {e}")
