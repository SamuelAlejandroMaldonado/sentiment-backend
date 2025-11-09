import logging
from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.core.model_loader import sentiment_model

router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.post("/analyze", response_model=ChatResponse)
def analyze_sentiment(request: ChatRequest):
    try:
        sentiment_result = sentiment_model(request.message)[0]
        sentiment_label = sentiment_result["label"]
        confidence = float(sentiment_result["score"])

        logger.info(f"User: {request.message}")
        logger.info(f"Sentiment: {sentiment_label} ({confidence:.2f})")

        return ChatResponse(
            sentiment=sentiment_label,
            confidence=confidence,
            reply=""
        )

    except Exception as e:
        logger.error(f"Error during sentiment analysis: {e}")
        return ChatResponse(
            sentiment="ERROR",
            confidence=0.0,
            reply=""
        )
