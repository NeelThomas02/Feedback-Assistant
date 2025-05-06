from data.preprocess import clean_text
from models.summarizer import summarize
from models.classifier import classify

def run_pipeline(raw_text: str) -> dict:
    cleaned = clean_text(raw_text)
    summary = summarize(cleaned)
    category = classify(cleaned)
    return {"summary": summary, "category": category}
