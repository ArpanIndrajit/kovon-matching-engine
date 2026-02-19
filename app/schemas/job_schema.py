from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    country: str
    description: str
