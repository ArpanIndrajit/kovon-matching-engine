import chromadb
from app.config import CHROMA_DB_PATH, CANDIDATE_COLLECTION, JOB_COLLECTION

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

candidate_collection = client.get_or_create_collection(
    name=CANDIDATE_COLLECTION
)

job_collection = client.get_or_create_collection(
    name=JOB_COLLECTION
)
