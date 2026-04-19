from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings()

db = Chroma(
    persist_directory="db",
    embedding_function=embedding
)

def retrieve(query):
    results = db.similarity_search_with_score(query, k=5)

    filtered = []

    for doc, score in results:
        if score < 1.5:
            filtered.append(doc.page_content)

    # fallback if nothing found
    if not filtered:
        filtered = [doc.page_content for doc, _ in results[:3]]

    return filtered[:3]