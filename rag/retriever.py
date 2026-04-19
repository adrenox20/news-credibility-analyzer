import os
from langchain_community.vectorstores import Chroma
from rag.simple_embeddings import SimpleEmbedding

DB_DIR = "db"

def build_db():
    with open("rag/fact_checks.txt", "r") as f:
        texts = [t.strip() for t in f.readlines() if t.strip()]

    embedding = SimpleEmbedding()

    db = Chroma.from_texts(
        texts,
        embedding,
        persist_directory=DB_DIR
    )
    db.persist()
    return db

def load_db():
    embedding = SimpleEmbedding()
    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding
    )

_db = None

def get_db():
    global _db
    if _db is None:
        if not os.path.exists(DB_DIR):
            _db = build_db()
        else:
            _db = load_db()
    return _db

def retrieve(query):
    db = get_db()
    results = db.similarity_search(query, k=3)
    return [doc.page_content for doc in results]