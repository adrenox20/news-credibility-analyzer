def analyze_risk(text):

    risks = []
    text_lower = text.lower()

    # Sensational / emotional
    if "!" in text:
        risks.append("Sensational tone")

    if "shocking" in text_lower:
        risks.append("Emotional manipulation")

    # Conspiracy / clickbait
    if "secret" in text_lower:
        risks.append("Conspiracy language")

    if "breaking" in text_lower and len(text.split()) < 15:
        risks.append("Clickbait style")

    # Very short claim
    if len(text.split()) <= 5:
        risks.append("Unverified very short claim")

    # Sensitive topics
    if "dead" in text_lower:
        risks.append("Sensitive claim (death-related misinformation)")

    # Multiple statements
    if text.count(".") > 2:
        risks.append("Multiple news statements detected")

    # 🔥 NEW: Uncertainty detection
    uncertainty_words = [
        "unclear", "not confirmed", "developing",
        "reports suggest", "details awaited"
    ]

    if any(word in text_lower for word in uncertainty_words):
        risks.append("Unverified or developing news")

    return risks