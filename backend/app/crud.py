from sqlalchemy.orm import Session
from app.models import User, PotentialRecruit
from app.schemas import UserCreate, PotentialRecruitCreate, PotentialRecruitUpdate
from datetime import datetime

# Function to create a new user
def create_user(db: Session, user: UserCreate):
    """
    Creates a new user in the database.
    """
    db_user = User(
        username=user.username,
        password=user.password,
        role=user.role,
        company=user.company
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Function to create a new potential recruit
def create_potential_recruit(db: Session, recruit: PotentialRecruitCreate):
    """
    Creates a new potential recruit in the database.
    """
   
    db_recruit = PotentialRecruit(**recruit.dict())
    db.add(db_recruit)
    db.commit()
    db.refresh(db_recruit)
    return db_recruit

# Function to get all potential recruits
def get_all_potential_recruits(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieves all potential recruits from the database.
    """
    return db.query(PotentialRecruit).offset(skip).limit(limit).all()

# Function to search potential recruits by keyword
def search_potential_recruits(db: Session, keyword: str):
    """
    Searches for recruits whose name, email, or description contains the keyword.
    """
    return db.query(PotentialRecruit).filter(
        (PotentialRecruit.first_name.ilike(f"%{keyword}%")) |
        (PotentialRecruit.last_name.ilike(f"%{keyword}%")) |
        (PotentialRecruit.description.ilike(f"%{keyword}%"))
    ).all()

# Function to delete a potential recruit
def delete_potential_recruit(db: Session, recruit_id: int):
    """
    Deletes a potential recruit by ID.
    """
    recruit = db.query(PotentialRecruit).filter(PotentialRecruit.id == recruit_id).first()
    if recruit:
        db.delete(recruit)
        db.commit()
    return recruit

