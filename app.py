import streamlit as st
from agent.workflow import run_agent

st.set_page_config(page_title="Agentic News Analyzer", layout="wide")

st.title("🧠 Intelligent News Credibility & Misinformation Analyzer")

text = st.text_area("Enter News Article")

if st.button("Analyze"):

    report = run_agent(text)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Summary")
        st.write(report["summary"])

        st.subheader("⚠️ Risk Factors")
        for r in report["risk_factors"]:
            st.write("•", r)

        st.subheader("🧠 Analysis")
        st.write(report["analysis"])

    with col2:
        st.subheader("🔍 Fact Check")
        for f in report["fact_check"]:
            st.write("•", f)

        st.subheader("📊 Verdict")
        st.metric("Verdict", report["verdict"])
        st.metric("Confidence (%)", report["confidence_score"])

        st.progress(report["confidence_score"] / 100)

    st.subheader("🤖 LLM Analysis")
    st.write(report["llm_analysis"])

    st.subheader("⚖️ Disclaimer")
    st.warning(report["disclaimer"])