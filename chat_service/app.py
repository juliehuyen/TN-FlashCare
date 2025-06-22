from fastapi import FastAPI, Request
import random

app = FastAPI(title="Mock Chat Service")

@app.post("/single-prompt")
async def single_prompt(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")

    # 💡 MOCK DÉTERMINISTIQUE SIMPLE
    score = round(random.uniform(0.5, 1.0), 2)
    level = "low" if score < 0.6 else "medium" if score < 0.8 else "high"
    explanation = "Mocked response based on patient symptoms."

    return {
        "score": score,
        "level": level,
        "explanation": explanation
    }
