from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    sentiment: str
    confidence: float
    reply: str = ""
