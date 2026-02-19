# Semantic Candidate–Job Matching Engine

An AI-powered backend service that performs semantic matching between candidate profiles and job descriptions using sentence embeddings and vector similarity search.

This system intelligently matches candidates and jobs even when wording differs by understanding meaning rather than relying on keyword matching.

---

## 🚀 Features

- Create candidate profiles
- Create job descriptions
- Generate sentence embeddings
- Store vectors in FAISS (vector database)
- Semantic similarity matching
- Rank candidates by similarity score and experience
- Explanation endpoint (why candidate matches)
- Minimum experience filtering
- Caching layer for faster results
- SQLite database for persistence
- Dockerized deployment

---

## 🧰 Tech Stack

- Python 3.10+
- FastAPI
- SentenceTransformers (HuggingFace)
- FAISS
- SQLite + SQLAlchemy
- Docker

---

## 📂 Project Architecture

semantic-matcher/
│
├── app/
│ ├── main.py
│ ├── api/
│ │ ├── candidates.py
│ │ └── jobs.py
│ ├── services/
│ │ ├── embedding_service.py
│ │ ├── matching_service.py
│ │ ├── explanation_service.py
│ │ └── cache.py
│ ├── db/
│ │ ├── database.py
│ │ └── tables.py
│ ├── models/
│ │ └── entities.py
│ └── schemas/
│ └── schemas.py
│
├── Dockerfile
├── README.md




---

## ⚙️ System Architecture Explanation

1. Candidate or Job text is received through FastAPI endpoints.
2. Text is converted into numerical vectors using a sentence embedding model.
3. Vectors are stored inside FAISS vector database.
4. When matching is requested:
   - Job vector is compared with all candidate vectors.
   - Cosine similarity is computed.
   - Results are ranked by similarity score and experience.
5. Results are returned to user.

---

## 🧠 Embedding Model Used

Model:  
all-MiniLM-L6-v2


Provided by HuggingFace SentenceTransformers.

Why this model:
- Lightweight and fast
- Produces 384-dimensional embeddings
- Trained for semantic sentence similarity

This model converts text into vectors such that similar meanings produce similar vectors.

---

## 📐 Similarity Metric

Cosine Similarity is used.

Formula:
cosine_similarity(A, B) = (A · B) / (||A|| * ||B||)


Where:
- A and B are embedding vectors
- Higher value means more similar meaning

Similarity range:
- 0.75 – 1.0  → High match  
- 0.40 – 0.75 → Medium match  
- Below 0.40 → Low match  

FAISS inner product index is used with normalized vectors to compute cosine similarity.

---

## 🔌 API Endpoints

### Create Candidate
POST /candidates




  "name": "Rahul",
  "skill_description": "Registered nurse with ICU experience and German A2",
  "experience": 4,
  "location": "India"
}


### Create Job
POST /jobs

{
  "title": "ICU Nurse",
  "country": "Germany",
  "description": "Need ICU nurse with hospital experience and basic German"
}



Match Candidates
GET /jobs/{job_id}/match?min_experience=3

Explanation
GET /jobs/{job_id}/explain/{candidate_id}


▶️ Setup Instructions (Without Docker)

Open terminal

Go to project folder

Activate environment
venv\Scripts\activate

Run server
uvicorn app.main:app --reload

Open browser
http://127.0.0.1:8000/docs

🐳 Setup Instructions (With Docker)

Build image
docker build -t semantic-matcher .

Run container
docker run -p 8000:8000 semantic-matcher

Open browser
http://127.0.0.1:8000/docs



Example Test Cases
| Case | Candidate          | Job               | Expected Result   |
| ---- | ------------------ | ----------------- | ----------------- |
| 1    | ICU Nurse + German | ICU Nurse Germany | High similarity   |
| 2    | General Nurse      | ICU Nurse Germany | Medium similarity |
| 3    | Electrician        | ICU Nurse         | Low similarity    |



Author
Arpana Indrajit
AI Engineer

---

# ✅ WHAT TO DO NOW

1. Open `README.md`
2. Delete everything
3. Paste ALL content above
4. Save

---
