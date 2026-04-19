import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}

def call_llm(prompt):

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=10
        )

        if response.status_code == 200:
            return response.json()[0]["generated_text"]

        return None

    except:
        return None