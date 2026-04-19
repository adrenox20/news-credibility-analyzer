from model.predict import predict_news
from agent.risk_analyzer import analyze_risk
from rag.retriever import retrieve_facts
from agent.reasoning import generate_report

def run_agent(text):

    label, prob = predict_news(text)

    risks = analyze_risk(text)

    facts = retrieve_facts(text)

    report = generate_report(text, risks, facts, label, prob)

    return report