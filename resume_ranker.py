import re
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
nlp = spacy.load("en_core_web_sm")

# Optional: define common tech skills
SKILL_KEYWORDS = ["python","java","c++","tensorflow","keras","pytorch","nlp","sql",
                  "excel","powerbi","react","node","mongodb","flask","docker","aws"]

def extract_skills(text):
    text = text.lower()
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]
    found_skills = [skill for skill in SKILL_KEYWORDS if skill in tokens]
    return list(set(found_skills))

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text

def rank_resumes(resumes, job_description):
    cleaned_resumes = [clean_text(r) for r in resumes]
    jd_cleaned = clean_text(job_description)

    documents = cleaned_resumes + [jd_cleaned]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    resume_vectors = vectors[:-1]
    jd_vector = vectors[-1]

    scores = cosine_similarity(resume_vectors, jd_vector.reshape(1,-1))
    scores = np.array(scores).reshape(-1)

    return scores
