from fastapi import APIRouter
import uuid

from app.schemas.job_schema import JobCreate
from app.services.embedding_service import generate_embedding
from app.db.chroma_client import job_collection, candidate_collection

router = APIRouter()

@router.post("/jobs")
def create_job(job: JobCreate):

    job_id = str(uuid.uuid4())

    embedding = generate_embedding(job.description)

    job_collection.add(
        ids=[job_id],
        embeddings=[embedding],
        metadatas=[{
            "title": job.title,
            "country": job.country,
            "description": job.description
        }]
    )

    return {
        "job_id": job_id,
        "message": "Job created successfully"
    }


@router.get("/jobs/{job_id}/match")
def match_candidates(job_id: str):

    job = job_collection.get(ids=[job_id], include=["embeddings"])

    job_embedding = job["embeddings"][0]

    results = candidate_collection.query(
        query_embeddings=[job_embedding],
        n_results=5,
        include=["metadatas", "distances", "documents"]
    )

    matches = []

    for i in range(len(results["ids"][0])):

        similarity_score = 1 - results["distances"][0][i]

        metadata = results["metadatas"][0][i]

        matches.append({
            "candidateId": results["ids"][0][i],
            "similarityScore": similarity_score,
            "experience": metadata["experience"]
        })

    matches.sort(
        key=lambda x: (x["similarityScore"], x["experience"]),
        reverse=True
    )

    return matches
