# app/routers/mood.py
import logging
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.model_loader import generator_model  # solo el generativo

router = APIRouter()
logger = logging.getLogger("uvicorn")

# Request y Response
class MoodRequest(BaseModel):
    sentiment: str

class MoodResponse(BaseModel):
    emoji: str
    message: str

@router.post("/generate-mood", response_model=MoodResponse)
def generate_mood(req: MoodRequest):
    try:
        sentiment = req.sentiment.upper()


        if sentiment == "POSITIVE":
            emoji = "😄"
        elif sentiment == "NEGATIVE":
            emoji = "😔"
        else:
            emoji = "😐"


        prompt = (
            f"Write a short, uplifting, and motivational message (1-2 sentences) "
            f"for someone feeling {sentiment.lower()}. "
            "Start directly with the message, do not include quotes, emojis, or extra characters. "
            "The message should be at least 5 words long and sound natural and encouraging."
        )
        gen = generator_model(
            prompt,
            max_length=60,
            min_length=20,
            do_sample=True,
            temperature=0.8,
            top_p=0.9,
            num_return_sequences=1
        )[0]

        message = gen["generated_text"].strip()

        message = message.split(".")[0].strip() + "."

        # 3️⃣ Logging
        logger.info(f"Sentiment: {sentiment}, Emoji: {emoji}, Message: {message}")

        return MoodResponse(emoji=emoji, message=message)

    except Exception as e:
        logger.error(f"Error generating mood: {e}")
        return MoodResponse(emoji="😐", message="Neutral mood")
