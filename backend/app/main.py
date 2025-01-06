from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from app.routes.register import router as register_router
from app.routes.login import router as login_router
from app.routes import potential_recruits

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# Include routers
app.include_router(login_router, prefix="/auth")
app.include_router(register_router, prefix="/auth")
app.include_router(potential_recruits.router, prefix="/potential_recruits", tags=["Potential Recruits"])
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
