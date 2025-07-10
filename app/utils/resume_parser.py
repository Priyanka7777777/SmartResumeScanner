import spacy
from pdfminer.high_level import extract_text
import os

nlp = spacy.load("en_core_web_sm")

# Predefined list of skills
SKILLS = [
    'python', 'java', 'sql', 'flask', 'django', 'aws', 'git', 'docker',
    'html', 'css', 'javascript', 'machine learning', 'data analysis', 'nlp',
    'pandas', 'numpy', 'linux', 'excel', 'communication', 'leadership'
]

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_skills(text):
    doc = nlp(text.lower())
    extracted = set()

    for token in doc:
        if token.text in SKILLS:
            extracted.add(token.text)
    
    return list(extracted)

