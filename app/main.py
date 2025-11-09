from fastapi import FastAPI
from app.api.routes_chat import router as chat_router
from app.api.mood import router as mood_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chatbot API")

#python -m venv venv
#venv\Scripts\activate
#pip install -r requirements.txt


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(mood_router, prefix="/mood", tags=["mood"])
@app.get("/")
def root():
    return {"message": "Chatbot API is running"}
