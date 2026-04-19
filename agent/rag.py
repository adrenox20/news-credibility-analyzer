from data.fact_db import fact_db

def retrieve_facts(text):
    results = []

    for fact in fact_db:
        if fact["claim"] in text.lower():
            results.append(fact)

    return results if results else "No matches found"