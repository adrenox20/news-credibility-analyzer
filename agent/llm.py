def generate_report(article, risks, facts, ml_result):

    label, prob, probs = ml_result

    if len(risks) == 0:
        verdict = "Credible"
    elif "Sensitive claim" in risks:
        verdict = "Fake"
    elif "Conspiracy language" in risks:
        verdict = "Suspicious"
    elif "Unverified news" in risks:
        verdict = "Suspicious"
    elif len(risks) >= 3:
        verdict = "Fake"
    else:
        verdict = "Suspicious"

    return {
        "summary": article[:120],
        "risk_factors": risks,
        "pattern_summary": f"{len(risks)} risks detected",
        "fact_check": facts,
        "verification": f"{len(facts)} references retrieved",
        "verdict": verdict,
        "confidence_score": round(prob, 2),
        "confidence_level": "High" if prob > 0.8 else "Medium",
        "explanation": f"ML predicted {label} with confidence {round(prob,2)}. Risks: {', '.join(risks) if risks else 'None'}",
        "probabilities": probs.tolist(),
        "disclaimer": "Verify with trusted sources"
    }