from app.db.chroma_client import job_collection, candidate_collection
from app.services.embedding_service import generate_embedding

def match_candidates(job_id: str, top_k=5):

    job = job_collection.get(ids=[job_id], include=["embeddings"])

    if not job["embeddings"]:
        return []

    job_embedding = job["embeddings"][0]

    results = candidate_collection.query(
        query_embeddings=[job_embedding],
        n_results=top_k,
        include=["metadatas", "distances", "embeddings", "ids"]
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