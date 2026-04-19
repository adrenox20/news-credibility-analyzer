from agent.llm import call_llm

def generate_report(text, risks, facts, label, prob):

    prompt = f"""
    Analyze the following news article:

    Article: {text}

    Risks: {risks}
    Facts: {facts}

    Provide:
    Summary
    Verdict
    Explanation
    """

    llm_output = call_llm(prompt)

    if not llm_output:
        llm_output = "LLM unavailable. Using rule-based reasoning."

    confidence_level = "High" if prob > 0.8 else "Medium"

    return {
        "summary": text[:150] + "...",
        "risk_factors": risks,
        "fact_check": facts,
        "llm_analysis": llm_output,
        "verdict": label,
        "confidence_score": round(prob * 100, 2),
        "confidence_level": confidence_level,
        "analysis": f"ML + rule-based system detected risk indicators: {', '.join(risks)}.",
        "disclaimer": "AI-generated analysis. Verify with trusted sources."
    }