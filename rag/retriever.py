def retrieve_facts(text):

    facts = []

    if "covid" in text.lower():
        facts.append("COVID vaccine does not cause infertility – WHO")

    if "moon" in text.lower():
        facts.append("Moon landing was real – NASA")

    if "5g" in text.lower():
        facts.append("5G does not spread viruses – scientific consensus")

    if "climate" in text.lower():
        facts.append("Climate change is real – IPCC")

    if not facts:
        facts = [
            "No direct fact match found",
            "Cross-check with trusted sources"
        ]

    return facts