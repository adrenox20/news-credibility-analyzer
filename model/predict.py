import pickle
import os

# Get correct path (VERY IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model + vectorizer
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))


def predict_credibility(text):
    vec = vectorizer.transform([text])

    probabilities = model.predict_proba(vec)[0]

    credible_prob = probabilities[1]
    confidence = max(probabilities) * 100

    if credible_prob > 0.6:
        label = "Credible"
    else:
        label = "Fake"

    return label, confidence