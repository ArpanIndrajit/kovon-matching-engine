from fastapi import APIRouter
import uuid

from app.schemas.candidate_schema import CandidateCreate
from app.services.embedding_service import generate_embedding
from app.db.chroma_client import candidate_collection

router = APIRouter()

@router.post("/candidates")
def create_candidate(candidate: CandidateCreate):

    candidate_id = str(uuid.uuid4())

    embedding = generate_embedding(candidate.skill_description)

    candidate_collection.add(
    ids=[candidate_id],
    embeddings=[embedding],
    documents=[candidate.skill_description],   # ← add this
    metadatas=[{
        "name": candidate.name,
        "experience": candidate.experience,
        "location": candidate.location,
        "skill_description": candidate.skill_description
    }]
)

    return {
        "candidate_id": candidate_id,
        "message": "Candidate created successfully"
    }
