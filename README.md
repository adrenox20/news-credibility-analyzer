# 🧠 Intelligent News Credibility Analyzer  
From ML-Based Classification to Agentic AI Misinformation Monitoring System

A complete end-to-end AI system that analyzes news articles and determines whether they are Credible (Real) or Fake. The project is extended into an Agentic AI system capable of reasoning, fact-checking, and generating structured credibility reports.

---

## 🚀 Live Demo

Streamlit App: https://news-credibility-analyzer-newton-project.streamlit.app/ 
GitHub Repository: https://github.com/adrenox20/news-credibility-analyzer  

---

## 📌 Project Overview

The rapid spread of misinformation across digital platforms has created a need for automated credibility verification systems.

This project is developed in two stages:

Milestone 1  
A Machine Learning system using NLP techniques to classify news articles as Fake or Real.

Milestone 2  
An Agentic AI system that enhances prediction with reasoning, pattern detection, fact-check retrieval, and structured reporting.

---

## 🧠 System Architecture

User Input  
↓  
Streamlit Interface  
↓  
ML Model (TF-IDF + Logistic Regression)  
↓  
Agent Controller (State Management)  
↓  
RAG Module (Fact Retrieval)  
↓  
Analysis Engine  
↓  
Structured Output Report  

---

## 🧾 Dataset

Dataset used: Fake and Real News Dataset (Kaggle)

Total articles: ~44,000  
Fake news: ~23,000  
Real news: ~21,000  

Features:
- Title  
- Article text  
- Subject category  
- Publication date  

Target:
- 0 → Fake News  
- 1 → Real News  

---

## ⚙️ Technology Stack

Programming Language: Python  
Machine Learning: Scikit-learn (Logistic Regression)  
Natural Language Processing: TF-IDF Vectorization  
Data Processing: Pandas, NumPy  
Visualization: Matplotlib  
UI: Streamlit  
Deployment: Streamlit Community Cloud  
Version Control: Git and GitHub  

---

## 📊 Model Details (Milestone 1)

Feature Extraction: TF-IDF Vectorizer (Max Features: 5000)  
Stopword removal enabled  

Classifier: Logistic Regression (max_iter = 1000)  
Train-Test Split: 80 percent training, 20 percent testing  

Performance:
Accuracy: 96–98 percent  
Precision: ~0.97  
Recall: ~0.97  
F1 Score: ~0.97  

---

## 🤖 Milestone 2: Agentic AI System

This phase transforms the system into an intelligent agent that goes beyond prediction.

Key Capabilities:

- Agent workflow with state-based execution  
- Retrieval-Augmented Generation (RAG) for fact-checking  
- Pattern detection of misleading or sensational content  
- Structured credibility report generation  
- Controlled reasoning to reduce hallucinations  

Workflow:
Input → ML Prediction → Retrieval → Analysis → Final Report  

---

## 🧾 Structured Output

The system generates a structured credibility report:

- Summary: Article overview  
- Analysis: Risk factors and misinformation signals  
- Fact Check: Retrieved verification patterns  
- Verdict: Credible or Fake  
- Confidence Score: Percentage  
- Disclaimer: Ethical and verification notice  

---

## 🖥️ Application Features

- Real-time news credibility prediction  
- Confidence score visualization  
- Agent-based reasoning system  
- Fact-check retrieval  
- Structured AI-generated reports  
- Interactive and modern UI  
- Fully deployed web application  

---

## 📁 Project Structure

news-credibility-analyzer/

app.py  
agent/  
workflow.py  
llm.py  
rag.py  
report.py  

model/  
model.pkl  
vectorizer.pkl  
predict.py  

data/  
fact_db.py  

train.py  
requirements.txt  
README.md  

---

## ▶️ How to Run Locally

Step 1: Clone repository  
git clone https://github.com/adrenox20/news-credibility-analyzer.git  
cd news-credibility-analyzer  

Step 2: Create virtual environment  
python3 -m venv venv  
source venv/bin/activate  

Step 3: Install dependencies  
pip install -r requirements.txt  

Step 4: Run application  
streamlit run app.py  

---

## 🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Publicly accessible  
Real-time inference  
No local setup required  

---

## 📈 Future Improvements

- Integration with FAISS or Chroma for real RAG  
- Transformer-based models (BERT, RoBERTa)  
- Explainable AI (SHAP, LIME)  
- Multi-language support  
- Integration with live news APIs  

---

## 👥 Team Members

Ram Bhardwaj  
Mukund Mangla  
Prajjwal Tripathi  

B.Tech Artificial Intelligence & Machine Learning  

---

## 📜 License

This project is developed for academic and educational purposes.

---

## ✅ Conclusion

This project demonstrates how classical NLP and Machine Learning techniques can evolve into an Agentic AI system capable of reasoning, retrieval, and structured analysis.

It highlights a scalable approach to tackling misinformation using predictive models, agent workflows, and interpretable outputs.
