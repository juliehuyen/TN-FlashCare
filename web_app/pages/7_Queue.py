import streamlit as st
import requests

st.set_page_config(page_title="File d’attente patients", layout="centered")

st.title("File d'attente")

QUEUE_URL = "http://localhost:8003/queue"

st.markdown("""
<style>
.patient-card {
    background-color: #f5f9ff;
    border-left: 8px solid #4DAFEB;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.patient-critical {
    border-left-color: #FF4B4B !important;
    background-color: #ffeaea !important;
}

.patient-medium {
    border-left-color: #FFA500 !important;
    background-color: #fff5e6 !important;
}

.patient-low {
    border-left-color: #28a745 !important;
    background-color: #e9f7ef !important;
}

.patient-title {
    font-size: 1.3rem;
    font-weight: bold;
    color: #333;
    margin-bottom: 0.8rem;
}

.patient-score,
.patient-level,
.patient-explanation {
    font-size: 1.05rem;
    color: #444;
    margin-bottom: 0.6rem;
}
</style>
""", unsafe_allow_html=True)



try:
    response = requests.get(QUEUE_URL)
    response.raise_for_status()
    queue = response.json()

    if not queue:
        st.info("La file d'attente est vide.")
    else:
        for i, patient in enumerate(queue, start=1):
            raw_id = patient.get('patient_id', '')
            parts = raw_id.split('_')
            display_name = ' '.join([part.capitalize() for part in parts])

            triage_level = patient.get('triage_level', '').lower()
            triage_class = {
                "high": "patient-critical",
                "moderate": "patient-medium",
                "low": "patient-low"
            }.get(triage_level, "patient-card")  # default fallback

            # Bloc HTML stylisé
            st.markdown(f"""
            <div class="patient-card ">
                <div class="patient-title">{display_name}</div>
                <div class="patient-score">Score: {patient['triage_score']:.2f}</div>
                <div class="patient-level"><strong>Level:</strong> {triage_level.capitalize()}</div>
                <div class="patient-explanation">{patient['explanation']}</div>
            </div>
            """, unsafe_allow_html=True)


except Exception as e:
    st.error(f"Erreur lors de la récupération de la file d'attente : {e}")
