import streamlit as st
from agent.agent import run_agent

st.set_page_config(page_title="AI News Credibility Analyzer", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🧠 AI News Credibility System")
    st.write("ML + Agent + Chroma RAG")
    st.success("System Ready")

# Main UI
st.title("🧠 Intelligent News Credibility Analyzer")

text = st.text_area("Enter News Article", height=180)

if st.button("Analyze"):

    if not text.strip():
        st.warning("Enter text")
        st.stop()

    result = run_agent(text)
    report = result["report"]

    col1, col2, col3 = st.columns(3)
    col1.metric("Verdict", report["verdict"])
    col2.metric("Confidence", report["confidence_score"])
    col3.metric("Risk Count", len(report["risk_factors"]))

    st.progress(report["confidence_score"])

    tab1, tab2, tab3 = st.tabs(["Summary", "Analysis", "Details"])

    with tab1:
        st.write(report["summary"])

    with tab2:
        st.subheader("Risks")
        for r in report["risk_factors"]:
            st.write("•", r)

        st.subheader("Explanation")
        st.write(report["explanation"])

    with tab3:
        st.write(report["pattern_summary"])
        st.write(report["verification"])
        st.write(report["disclaimer"])