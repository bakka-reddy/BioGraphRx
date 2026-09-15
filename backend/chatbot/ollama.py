import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:4b"


def generate_response(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model
    and return the generated response.
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(
            f"Ollama request failed: "
            f"{response.status_code} - {response.text}"
        )

    result = response.json()

    return result["response"]