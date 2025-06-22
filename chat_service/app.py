from fastapi import FastAPI, Request, HTTPException
import json
import cohere
import re

cohere_api_key = "5Z1ylzHGp7J1SGNxPXbJXgI6ioDguFlVTrjYeMCP"  # Remplacez par votre clé API
client = cohere.Client(cohere_api_key)

app = FastAPI()

@app.post("/single-prompt")
async def single_prompt(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        raise HTTPException(status_code=400, detail="Missing prompt")
    try:
        response = client.chat(
            model="command-nightly",
            message=prompt,
            max_tokens=150,
        )
        raw = response.text.strip()
        print("LLM raw response:", raw)  # Pour debug

        # Extraction robuste du JSON
        match = re.search(r"```json\s*({.*?})\s*```", raw, re.DOTALL)
        if match:
            json_str = match.group(1)
        else:
            # fallback: extraire le premier bloc JSON trouvé
            match = re.search(r"({.*})", raw, re.DOTALL)
            if match:
                json_str = match.group(1)
            else:
                raise HTTPException(status_code=500, detail=f"LLM did not return JSON: {raw}")

        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")