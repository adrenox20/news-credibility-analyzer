from model.predict import predict_credibility
from agent.llm import analyze_with_llm
from agent.rag import retrieve_facts
from agent.report import generate_report

def run_agent(text):
    state = {}

    # Step 1: ML Prediction
    prediction, confidence = predict_credibility(text)

    # 🧠 SMART OVERRIDE (IMPORTANT)
    trusted_keywords = ["government", "policy", "official", "announced", "minister"]

    if any(word in text.lower() for word in trusted_keywords):
        prediction = "Credible"
        confidence = max(confidence, 70)

    state["prediction"] = prediction
    state["confidence"] = confidence

    # Step 2: RAG
    facts = retrieve_facts(text)
    state["facts"] = facts

    # Step 3: LLM reasoning
    analysis = analyze_with_llm(text, prediction)
    state["analysis"] = analysis

    # Step 4: Final report
    report = generate_report(text, state)

    return report