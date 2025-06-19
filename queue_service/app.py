import os
import json
import requests
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI(title="Queue Service")
PATIENTS_DIR = "../patient_service/patients_data"
TRIAGE_URL = "http://localhost:8002/triage/"
queue: List[Dict] = []

@app.post("/trigger-update")
def update_queue():
    global queue
    queue = []

    for file in os.listdir(PATIENTS_DIR):
        if not file.endswith(".json"):
            continue
        with open(os.path.join(PATIENTS_DIR, file), encoding="utf-8") as f:
            patient = json.load(f)
            patient_id = patient.get("id")
            """if not patient_id:
                print("On skip")
                continue"""
            first = patient.get("first_name", "").strip().lower()
            last = patient.get("last_name", "").strip().lower()
            patient_id = f"{first}_{last}"

            try:
                resp = requests.post(f"{TRIAGE_URL}{patient_id}")
                print(f"[queue] triage-service response ({patient_id}): {resp.status_code} {resp.text}")
                if resp.ok:
                    triaged = resp.json()
                    print(f"[queue] triaged patient: {triaged}")
                    queue.append(triaged)
            except Exception as e:
                print(f"Erreur triage patient {patient_id}: {e}")

    queue.sort(key=lambda p: p["triage_score"], reverse=True)
    return {"message": "Queue mise à jour", "size": len(queue)}

@app.get("/queue")
def get_queue():
    return queue