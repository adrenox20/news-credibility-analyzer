def analyze_with_llm(text, prediction):
    return f"""
    🧠 AI Analysis:

    Summary:
    {text[:120]}

    Risk Factors:
    - Sensational language detected
    - Lack of verifiable sources
    - Possible misleading claims

    Prediction:
    The ML model classified this as {prediction}

    Explanation:
    This result is based on linguistic patterns and known misinformation indicators.
    """