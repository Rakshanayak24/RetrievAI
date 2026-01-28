from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Endee-like vector store abstraction
class EndeeVectorStore:
    def __init__(self):
        self.vectors = []

    def add(self, text, embedding):
        self.vectors.append((text, embedding))

    def search(self, query_embedding, top_k=3):
        scores = []
        for text, emb in self.vectors:
            score = np.dot(query_embedding, emb)
            scores.append((text, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

store = EndeeVectorStore()

@app.post("/ingest")
def ingest(text: str):
    emb = model.encode(text).tolist()
    store.add(text, emb)
    return {"status": "Document ingested into Endee vector store"}

@app.get("/query")
def query(q: str):
    q_emb = model.encode(q).tolist()
    results = store.search(q_emb)
    context = " ".join([r[0] for r in results])
    return {
        "query": q,
        "retrieved_context": context,
        "answer": context
    }