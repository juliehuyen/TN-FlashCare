import os
import json
import requests
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Patient Service")

class PatientForm(BaseModel):
    id: str = None  # optionnel pour qu'on le génère si absent
    first_name: str
    last_name: str
    birth_date: str
    medical_history: List[str]
    other_conditions: str
    symptoms: str
    emergency: str
    uploaded_files: List[str] = []

def save_form_data(data, directory="patient_service/patients_data"):
    os.makedirs(directory, exist_ok=True)
    prenom = data.get("first_name", "unknown").strip().capitalize().replace(" ", "_")
    nom = data.get("last_name", "unknown").strip().upper().replace(" ", "_")
    data["id"] = prenom.strip().lower() + "_" + nom.strip().lower()
    filename = f"{prenom}_{nom}.json"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    try:
        resp = requests.post("http://localhost:8003/trigger-update")
        if resp.ok:
            return {"message": "Formulaire soumis et queue mise à jour"}
        else:
            return {"warning": "Formulaire soumis mais échec de mise à jour de la queue"}
    except Exception as e:
        return {"error": f"Erreur lors de l'appel au queue-service: {e}"}
