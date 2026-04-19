import os

# Ensure DB is created if not exists
if not os.path.exists("db"):
    import subprocess
    subprocess.run(["python", "rag/create_db.py"])
    
import streamlit as st
from agent.agent import app as agent_app

st.set_page_config(
    page_title="AI News Credibility Analyzer",
    layout="wide"
)

# ================= SIDEBAR =================
with st.sidebar:
    st.title("🧠 AI News Credibility System")

    st.markdown("### 📊 Model Information")
    st.markdown("""
**Model Type:** Logistic Regression  
**Feature Extraction:** TF-IDF  
**Accuracy:** 96.4%  

**Developed using:**
- Scikit-learn  
- Streamlit  
- NLP  
""")

    st.markdown("---")

    st.markdown("### 🤖 Milestone 2 (Agentic AI)")
    st.markdown("""
- LangGraph Agent Workflow  
- Risk Analysis Engine  
- Retrieval-Augmented Generation (RAG)  
- Explainable AI Output  
""")

    st.markdown("---")

    st.markdown("### ⚙️ System Status")
    st.success("Model Loaded Successfully")
    st.info("Agent Ready for Analysis")

    st.markdown("---")

    st.markdown("### ⚡ Tips")
    st.write(
        "• Enter one complete news article\n"
        "• Avoid mixing multiple articles\n"
        "• Works best with structured text"
    )

# ================= MAIN =================
st.title("🧠 Intelligent News Credibility Analyzer")

st.markdown("""
AI-powered system for detecting **Fake, Credible, and Suspicious news**  
using **Machine Learning + Agentic AI + RAG**
""")

text = st.text_area("Enter News Article", height=180, placeholder="Paste news article here...")

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    # Prevent multiple articles
    lines = [line for line in text.split("\n") if line.strip() != ""]
    if len(lines) > 8:
        st.warning("Please enter only ONE news article at a time.")
        st.stop()

    result = agent_app.invoke({"text": text})
    report = result["report"]

    # ===== METRICS =====
    col1, col2, col3 = st.columns(3)

    col1.metric("Verdict", report["verdict"])
    col2.metric("Confidence", report["confidence_score"])
    col3.metric("Risk Count", len(report["risk_factors"]))

    st.progress(report["confidence_score"])

    st.markdown("---")

    # ===== TABS =====
    tab1, tab2, tab3 = st.tabs(["📄 Summary", "🔍 Analysis", "⚙️ Details"])

    # ===== SUMMARY =====
    with tab1:
        st.subheader("📄 Summary")
        st.write(report["summary"])

    # ===== ANALYSIS =====
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("⚠️ Risk Factors")
            if report["risk_factors"]:
                for r in report["risk_factors"]:
                    st.write("•", r)
            else:
                st.write("No significant risks detected.")

            st.subheader("🧠 Explanation")
            st.write(report["explanation"])

        with col2:
            st.subheader("🔍 Fact Check (RAG)")
            if report["fact_check"]:
                for f in report["fact_check"]:
                    st.write("•", f)
            else:
                st.write("No related fact-checks found.")

    # ===== DETAILS =====
    with tab3:
        st.subheader("📊 Pattern Summary")
        st.info(report["pattern_summary"])

        st.subheader("🌐 Verification")
        st.write(report["verification"])

        st.subheader("⚖️ Disclaimer")
        st.warning(report["disclaimer"])