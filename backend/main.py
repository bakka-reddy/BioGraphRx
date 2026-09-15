from fastapi import FastAPI
from pydantic import BaseModel

from backend.chatbot.ollama import generate_response
from backend.chatbot.prompts import SYSTEM_PROMPT


app = FastAPI(
    title="BioGraphRx",
    description="Explainable AI Framework for Personalized Drug Interaction Prediction",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


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


@app.post("/chat")
def chat(request: ChatRequest):

    system_prompt = """
...
"""

    prompt = f"""
{system_prompt}

User:
{request.message}

Assistant:
"""

    try:
        answer = generate_response(prompt)

        return {
            "model": "qwen3:4b",
            "message": answer
        }

    except Exception as e:

        return {
            "error": str(e)
        }