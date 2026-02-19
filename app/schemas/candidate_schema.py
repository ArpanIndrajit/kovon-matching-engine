from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    skill_description: str
    experience: int
    location: str
