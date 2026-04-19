def retrieve(query):
    q = query.lower()

    if "vaccine" in q:
        return ["Vaccines are safe – WHO"]

    if "conspiracy" in q or "secret" in q:
        return ["No evidence supports conspiracy claims"]

    return ["Verify from trusted sources"]