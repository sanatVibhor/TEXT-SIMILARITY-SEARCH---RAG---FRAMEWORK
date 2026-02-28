import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"

def generate_response(query, context_docs):
    context_text = "\n\n".join(context_docs)

    prompt = f"""
You are an IT incident assistant.

User Query:
{query}

Relevant Incidents:
{context_text}

You MUST answer strictly using only the provided incidents.
If the answer is not present in the incidents, say:
"I do not have enough information in the incident database."
Do not add external knowledge.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]