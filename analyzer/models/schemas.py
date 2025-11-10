from pydantic import BaseModel

class TextRequest(BaseModel):
    context: str

class SentimentResponse(BaseModel):
    sentiment: int

class HealthResponse(BaseModel):
    status: str