def generate_report(text, state):

    return {
        "Summary": text[:200],
        "Analysis": state["analysis"],
        "Fact Check": state["facts"],
        "Verdict": state["prediction"],
        "Confidence": f"{state['confidence']:.2f}%",
        "Disclaimer": "AI-generated analysis. Verify from trusted sources."
    }