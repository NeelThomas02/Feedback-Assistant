# src/models/classifier.py
from openai import OpenAI
from config import OPENAI_API_KEY
# instantiate the v1 client
client = OpenAI(api_key=OPENAI_API_KEY)

def classify(text: str) -> str:
    prompt = (
      "Classify this feedback into: bug report, feature request, praise, "
      "complaint, or urgent.\n\n" + text
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_tokens=50,
    )
    return resp.choices[0].message.content.strip()
