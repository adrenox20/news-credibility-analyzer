import streamlit as st
from agent.workflow import run_agent

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Credibility Agent",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.main {
    background-color: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
}

h1 {
    text-align: center;
    color: #00ffd5;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.verdict-good {
    color: #00ff9f;
    font-weight: bold;
    font-size: 24px;
}

.verdict-bad {
    color: #ff4b4b;
    font-weight: bold;
    font-size: 24px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🧠 AI Agent")
    st.markdown("### 📌 Milestone 2 Project")

    st.markdown("---")

    st.markdown("### 📖 Project Overview")
    st.write(
        "This system analyzes news articles to detect misinformation using "
        "Machine Learning, Agent-based reasoning, and Retrieval techniques."
    )

    st.markdown("---")

    st.markdown("### ⚙️ Features")
    st.write("• ML-based credibility prediction")
    st.write("• Agentic workflow (state-based)")
    st.write("• Fact-check retrieval (RAG)")
    st.write("• Structured AI report generation")

    st.markdown("---")

    st.markdown("### ⚙️ Controls")
    show_details = st.toggle("Show Detailed Analysis", value=True)

    st.markdown("---")

    st.markdown("### 🧩 Tech Stack")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Scikit-learn")

    st.markdown("---")
    st.markdown("🚀 Developed for Intelligent News Analysis")
    st.markdown("👨‍💻 Developed by Your Team")

# ---------------- HEADER ----------------
st.markdown("<h1>🧠 AI News Credibility System</h1>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
text = st.text_area("📰 Paste News Article Here", height=180)

# ---------------- BUTTON ----------------
if st.button("🚀 Analyze"):

    if text.strip() == "":
        st.warning("Enter some text first")
    else:
        report = run_agent(text)

        confidence_val = float(report["Confidence"].replace("%", ""))

        # ---------------- TOP SECTION ----------------
        st.markdown("### 📊 Confidence Level")
        st.progress(int(confidence_val))
        st.markdown(f"### {report['Confidence']} Confidence")

        # ---------------- VERDICT ----------------
        if report["Verdict"] == "Credible":
            st.markdown("<div class='verdict-good'>✅ Credible News</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='verdict-bad'>🚨 Fake News Detected</div>", unsafe_allow_html=True)

        st.markdown("---")

        # ---------------- SUMMARY ----------------
        st.markdown("### 📄 Summary")
        st.markdown(f"<div class='card'>{report['Summary']}</div>", unsafe_allow_html=True)

        # ---------------- DETAILS ----------------
        if show_details:
            st.markdown("### 🧠 AI Analysis")
            st.markdown(f"<div class='card'>{report['Analysis']}</div>", unsafe_allow_html=True)

            st.markdown("### 🔍 Fact Check")
            st.markdown(f"<div class='card'>{report['Fact Check']}</div>", unsafe_allow_html=True)

        # ---------------- DISCLAIMER ----------------
        st.markdown("### ⚠️ Disclaimer")
        st.markdown(f"<div class='card'>{report['Disclaimer']}</div>", unsafe_allow_html=True)