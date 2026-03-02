import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="News Credibility Analyzer",
    page_icon="📰",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# Header
st.title("📰 Intelligent News Credibility Analyzer")
st.markdown("AI-powered system for detecting fake and credible news using Machine Learning")

# Sidebar
st.sidebar.title("Model Information")

st.sidebar.metric("Model Type", "Logistic Regression")
st.sidebar.metric("Feature Extraction", "TF-IDF")
st.sidebar.metric("Model Accuracy", "96.4%")

st.sidebar.markdown("---")
st.sidebar.write("Developed using:")
st.sidebar.write("• Scikit-learn")
st.sidebar.write("• Streamlit")
st.sidebar.write("• NLP")

# Main layout
col1, col2 = st.columns([2,1])

with col1:

    st.subheader("Enter News Article")

    text = st.text_area(
        "",
        height=200,
        placeholder="Paste news article text here..."
    )

    analyze = st.button("Analyze Credibility", use_container_width=True)


with col2:

    st.subheader("System Status")

    st.success("Model Loaded Successfully")

    st.info("Ready for prediction")


# Prediction section
if analyze and text.strip() != "":

    vec = vectorizer.transform([text])

    prediction = model.predict(vec)[0]

    probabilities = model.predict_proba(vec)[0]

    confidence = max(probabilities) * 100

    st.markdown("---")
    st.subheader("Prediction Results")

    col3, col4 = st.columns(2)

    with col3:

        if prediction == 1:
            st.success("Credible News")
        else:
            st.error("Fake News Detected")

        st.metric("Confidence Score", f"{confidence:.2f}%")

    with col4:

        st.write("Prediction Probability")

        labels = ["Fake", "Credible"]
        values = probabilities

        fig, ax = plt.subplots()

        ax.bar(labels, values)

        ax.set_ylabel("Probability")

        st.pyplot(fig)


    # Confidence gauge style bar
    st.subheader("Confidence Meter")

    st.progress(int(confidence))


    # Feature importance (top words)
    st.subheader("Key Feature Importance")

    feature_names = vectorizer.get_feature_names_out()

    coef = model.coef_[0]

    top_indices = np.argsort(coef)[-10:]

    top_features = feature_names[top_indices]

    top_values = coef[top_indices]

    fig2, ax2 = plt.subplots()

    ax2.barh(top_features, top_values)

    ax2.set_xlabel("Importance")

    st.pyplot(fig2)


# Footer
st.markdown("---")
st.markdown("Built with Machine Learning and Natural Language Processing")