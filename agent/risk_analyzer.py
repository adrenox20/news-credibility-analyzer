def analyze_risk(text):
    risks = []
    t = text.lower()

    if "secret" in t:
        risks.append("Conspiracy language")

    if "breaking" in t:
        risks.append("Clickbait style")

    if len(text.split()) <= 5:
        risks.append("Very short claim")

    if "dead" in t:
        risks.append("Sensitive claim")

    if "unclear" in t or "not confirmed" in t:
        risks.append("Unverified news")

    return risks