from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embedding(text: str):
    embedding = model.encode(text)
    return embedding.tolist()
