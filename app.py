# app.py

import streamlit as st
import pickle


@st.cache_resource
def load_model():

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    return model, vectorizer


model, vectorizer = load_model()


st.title("Intelligent News Credibility Analyzer")

st.write("Analyze news articles and detect credibility using Machine Learning")


text = st.text_area("Enter News Article Text", height=200)


if st.button("Analyze Credibility"):

    if text.strip() == "":

        st.warning("Please enter news article text")

    else:

        vec = vectorizer.transform([text])

        prediction = model.predict(vec)[0]

        probabilities = model.predict_proba(vec)[0]

        confidence = max(probabilities) * 100


        if prediction == 1:

            st.success("Credible News")

            st.write(f"Confidence: {confidence:.2f}%")

        else:

            st.error("Fake News Detected")

            st.write(f"Confidence: {confidence:.2f}%")


st.write("---")

st.write("Model: Logistic Regression")
st.write("Features: TF-IDF Vectorization")
st.write("Framework: Streamlit")