def generate_report(article, risks, facts, ml_result):

    label, prob, probs = ml_result

    # ================= FINAL DECISION LOGIC =================

    strong_risks = [
        "Sensitive claim (death-related misinformation)",
        "Conspiracy language",
        "Clickbait style",
        "Emotional manipulation"
    ]

    if len(risks) == 0:
        verdict = "Credible"

    elif any(r in risks for r in strong_risks):
        verdict = "Fake"

    elif "Unverified or developing news" in risks:
        verdict = "Suspicious"

    elif len(risks) == 1:
        verdict = "Credible"

    elif len(risks) == 2:
        verdict = "Suspicious"

    else:
        verdict = "Fake"

    confidence_level = "High" if prob > 0.8 else "Medium"

    # ================= EXPLANATION =================

    if len(risks) == 0:
        explanation_text = "The article appears structured, neutral, and does not contain misinformation signals."
    else:
        explanation_text = f"Risk signals detected: {', '.join(risks)}."

    explanation = f"""
{explanation_text}
The ML model predicted '{label}' with confidence {round(prob,2)}.
The final verdict is based on combined reasoning (ML + risk analysis + retrieval).
"""

    # ================= OUTPUT =================

    return {
        "summary": f"This news states: {article[:120]}...",

        "risk_factors": risks,

        "pattern_summary": f"Detected {len(risks)} risk patterns: {', '.join(risks) if risks else 'None'}",

        "fact_check": facts,

        "verification": f"{len(facts)} external references retrieved",

        "verdict": verdict,

        "confidence_score": round(prob, 2),

        "confidence_level": confidence_level,

        "explanation": explanation,

        "probabilities": probs.tolist(),

        "disclaimer": "This AI system provides probabilistic analysis and should be verified with trusted sources."
    }