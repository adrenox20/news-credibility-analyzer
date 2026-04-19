from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

docs = open("rag/fact_checks.txt").read().split("\n")

embedding = HuggingFaceEmbeddings()

db = Chroma.from_texts(docs, embedding, persist_directory="db")

db.persist()

print("Vector DB created")