from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging
from app.gemini_client import GeminiClient





logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="HR AI Chatbot")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


gemini_client = GeminiClient()

class ChatRequest(BaseModel):
    prompt: str
    context: Optional[str] = None

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "healthy", "service": "HR AI Chatbot"}

@app.post("/chat")
async def chat(request: ChatRequest):

    try:
        response = await gemini_client.get_response(
            prompt=request.prompt,
            context=request.context
        )
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
