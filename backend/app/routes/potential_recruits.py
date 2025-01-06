from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.PotentialRecruit)
def create_recruit(recruit: schemas.PotentialRecruitCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new potential recruit.
    """
    return crud.create_potential_recruit(db=db, recruit=recruit)

@router.get("/", response_model=list[schemas.PotentialRecruit])
def get_all_recruits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all potential recruits.
    """
    return crud.get_all_potential_recruits(db, skip=skip, limit=limit)

@router.get("/search/", response_model=list[schemas.PotentialRecruit])
def search_recruits(keyword: str, db: Session = Depends(get_db)):
    """
    Endpoint to search recruits by keyword.
    """
    return crud.search_potential_recruits(db, keyword)

@router.delete("/{recruit_id}", response_model=schemas.PotentialRecruit)
def delete_recruit(recruit_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a recruit by ID.
    """
    recruit = crud.delete_potential_recruit(db, recruit_id)
    if not recruit:
        raise HTTPException(status_code=404, detail="Recruit not found")
    return recruit
