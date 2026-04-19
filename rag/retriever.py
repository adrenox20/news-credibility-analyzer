from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

db = None

def get_db():
    global db
    if db is None:
        embedding = HuggingFaceEmbeddings()
        db = Chroma(
            persist_directory="db",
            embedding_function=embedding
        )
    return db


def retrieve(query):
    db_instance = get_db()

    results = db_instance.similarity_search_with_score(query, k=5)

    filtered = []

    for doc, score in results:
        if score < 1.5:
            filtered.append(doc.page_content)

    if not filtered:
        filtered = [doc.page_content for doc, _ in results[:3]]

    return filtered[:3]