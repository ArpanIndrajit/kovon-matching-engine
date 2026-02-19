from fastapi import FastAPI

from app.api.candidates import router as candidate_router
from app.api.jobs import router as job_router

app = FastAPI(title="Kovon Matching Engine")

app.include_router(candidate_router)
app.include_router(job_router)

@app.get("/")
def root():
    return {"message": "Kovon Matching Engine Running"}
