from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import models, schemas, crud
from fastapi.staticfiles import StaticFiles
from app.database import SessionLocal, engine
from app.routes.register import router as register_router
from app.routes.login import router as login_router
from app.routes import potential_recruits
from app.routes import happy_hour
from app.routes import employees
from app.routes import formation_events
import os
import httpx

models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()
GEMINI_URL = "http://gemini_service:8002"
assets_path = "/app/frontend/assets"
# Include routers
app.include_router(login_router, prefix="/auth", tags=["authentication"])
app.include_router(register_router, prefix="/auth", tags=["authentication"])
app.include_router(potential_recruits.router, prefix="/potential_recruits", tags=["Potential Recruits"])
app.include_router(happy_hour.router, prefix="/happy_hour", tags=["Happy Hour"])
app.include_router(employees.router, prefix="/Employees", tags=["Employees"])
app.mount("/employees_pictures", StaticFiles(directory="uploads/employees_pictures"), name="employees_pictures")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(formation_events.router, prefix="/formation_events", tags=["Formation Events"])
if os.path.exists(assets_path):
    app.mount("/assets", StaticFiles(directory=assets_path), name="assets")
else:
    raise RuntimeError(f"Assets directory not found at {assets_path}")



# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{GEMINI_URL}/chat", json={"prompt": request.prompt})
        return response.json()
