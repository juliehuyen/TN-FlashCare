import os
import json
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Triage Service")
PATIENTS_DIR = "../patient_service/patients_data"
CHAT_SERVICE_URL = "http://localhost:8004"  # exemple

class TriageResult(BaseModel):
    patient_id: str
    triage_score: float
    triage_level: str
    explanation: str

def find_patient(patient_id: str) -> Optional[dict]:
    for filename in os.listdir(PATIENTS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(PATIENTS_DIR, filename), encoding="utf-8") as f:
                patient = json.load(f)
                # on normalise l'ID comme dans patient_service
                expected_id = f"{patient['first_name'].strip().lower()}_{patient['last_name'].strip().lower()}"
                if expected_id == patient_id:
                    return patient
    return None

@app.post("/triage/{patient_id}", response_model=TriageResult)
def triage_patient(patient_id: str):
    patient = find_patient(patient_id)
    if not patient:
        raise HTTPException(404, f"Patient {patient_id} not found.")

    prompt = (
        "You are a medical triage assistant.\n"
        "Given this patient record in JSON:\n"
        f"{json.dumps(patient, ensure_ascii=False, indent=2)}\n\n"
        "Please:\n"
        "  • Compute a triage score between 0.0 (low) and 1.0 (critical).\n"
        "  • Assign a level: 'low', 'medium', or 'high'.\n"
        "  • Provide a brief explanation of your reasoning.\n\n"
        "Return a JSON with keys: score, level, explanation."
    )

    resp = requests.post(f"{CHAT_SERVICE_URL}/single-prompt", json={"prompt": prompt})
    if not resp.ok:
        raise HTTPException(resp.status_code, f"ChatService error: {resp.text}")

    body = resp.json()
    try:
        return TriageResult(
            patient_id=patient_id,
            triage_score=float(body["score"]),
            triage_level=str(body["level"]),
            explanation=str(body["explanation"])
        )
    except KeyError as e:
        raise HTTPException(500, f"Malformed response from ChatService, missing {e}")