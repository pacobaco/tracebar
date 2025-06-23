import spacy
from datetime import datetime
from faker import Faker
import re
from .ocr_reader import extract_text_from_image

nlp = spacy.load("en_core_web_sm")
fake = Faker()

direct_pii_patterns = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
}
indirect_pii_patterns = {
    "ip": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "location": r"\b(Miami|Florida|New York|Los Angeles)\b",
    "device": r"\b(MacBook|iPhone|Android|Windows)\b",
    "file": r"[\w-]+\.(pdf|docx|xls)",
    "time": r"\b\d{1,2}:\d{2} ?[AP]M\b"
}

def extract_direct_pii(text):
    return {k: list(set(re.findall(v, text))) for k, v in direct_pii_patterns.items()}

def generate_random_mock_direct_pii():
    return {
        "name": [fake.name()],
        "email": [fake.email()],
        "phone": [fake.phone_number()],
        "ssn": [fake.ssn()],
        "location": [fake.city()]
    }

def extract_indirect_pii(text):
    return {k: list(set(re.findall(v, text))) for k, v in indirect_pii_patterns.items()}

def extract_ner(text):
    doc = nlp(text)
    ner = {}
    for ent in doc.ents:
        ner.setdefault(ent.label_, []).append(ent.text)
    return {k: list(set(v)) for k, v in ner.items()}

def resolution_score(direct, indirect):
    return min(len(direct) * 0.4 + len(indirect) * 0.15, 1.0)

def build_identity_profile(text=None, image_path=None, use_mock=False):
    content = ""
    if image_path:
        content = extract_text_from_image(image_path)
    if text:
        content = (content + "\n" + text).strip()
    if not content:
        return {}

    if use_mock:
        direct = generate_random_mock_direct_pii()
        indirect = {"location": direct.pop("location", [])}
        indirect.update(extract_indirect_pii(content))
    else:
        direct = extract_direct_pii(content)
        indirect = extract_indirect_pii(content)

    ner = extract_ner(content)
    confidence = resolution_score(direct, indirect)

    return {
        "id": f"profile_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "direct_pii": direct,
        "indirect_pii": indirect,
        "ner_entities": ner,
        "resolution_confidence": confidence,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }