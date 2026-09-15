from fastapi import FastAPI
import requests

app = FastAPI(
    title="BioGraphRx",
    description="Explainable AI Framework for Personalized Drug Interaction Prediction",
    version="1.0.0"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:4b"


@app.get("/")
def root():
    return {
        "message": "BioGraphRx API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/test-ollama")
def test_ollama():

    payload = {
        "model": MODEL,
        "prompt": "Explain what a drug-drug interaction is in simple terms.",
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    if response.status_code != 200:
        return {
            "error": "Ollama request failed",
            "status_code": response.status_code,
            "details": response.text
        }

    result = response.json()

    return {
        "model": MODEL,
        "response": result["response"]
    }