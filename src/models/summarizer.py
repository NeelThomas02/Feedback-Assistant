# src/models/summarizer.py
from openai import OpenAI
from config import OPENAI_API_KEY
# instantiate the v1 client
client = OpenAI(api_key=OPENAI_API_KEY)

def summarize(text: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
        max_tokens=150,
    )
    return resp.choices[0].message.content.strip()
