import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [tok.lemma_ for tok in doc if not tok.is_stop and tok.is_alpha]
    return " ".join(tokens)
