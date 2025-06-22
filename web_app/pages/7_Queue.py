import streamlit as st
import requests

st.set_page_config(page_title="📝 File d’attente patients", layout="centered")

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
            # Transform patient_id "prenom_nom" into "Prénom NOM"
            raw_id = patient.get('patient_id', '')
            parts = raw_id.split('_')
            display_name = ' '.join([part.capitalize() for part in parts])

            st.subheader(f"{i}. {display_name}")
            st.markdown(f"**Score:** {patient['triage_score']:.2f}")
            st.markdown(f"**Niveau:** {patient['triage_level'].capitalize()}")
            st.markdown(f"**Explication:** {patient['explanation']}")
            st.markdown("---")

except Exception as e:
    st.error(f"Erreur lors de la récupération de la file d'attente : {e}")
