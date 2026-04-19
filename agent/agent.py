from model.predict import predict_news
from agent.risk_analyzer import analyze_risk
from rag.retriever import retrieve
from agent.llm import generate_report

def run_agent(text):

    ml = predict_news(text)
    risks = analyze_risk(text)
    facts = retrieve(text)

    report = generate_report(text, risks, facts, ml)

    return {
        "ml": ml,
        "risks": risks,
        "facts": facts,
        "report": report
    }