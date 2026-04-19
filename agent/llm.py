def generate_report(article, risks, facts, ml_result):

    label, prob, probs = ml_result

    if len(risks) == 0:
        verdict = "Credible"
    elif "Sensitive claim" in str(risks):
        verdict = "Fake"
    elif len(risks) >= 2:
        verdict = "Fake"
    else:
        verdict = "Suspicious"

    explanation = f"""
Risks: {', '.join(risks) if risks else 'None'}
ML Prediction: {label} ({round(prob,2)})
"""

    return {
        "summary": article[:120],
        "risk_factors": risks,
        "pattern_summary": f"{len(risks)} risks detected",
        "fact_check": facts,
        "verification": f"{len(facts)} references",
        "verdict": verdict,
        "confidence_score": round(prob, 2),
        "confidence_level": "High" if prob > 0.8 else "Medium",
        "explanation": explanation,
        "probabilities": probs.tolist(),
        "disclaimer": "Verify with trusted sources"
    }