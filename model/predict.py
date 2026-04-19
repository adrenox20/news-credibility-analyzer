import pickle

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def predict_news(text):

    vec = vectorizer.transform([text])

    prediction = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    confidence = max(probabilities)

    if prediction == 1:
        label = "Credible"
    else:
        label = "Fake"

    return label, confidence, probabilities