from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/create_event/", response_model=schemas.FormationEvent)
def create_formation_event(event: schemas.FormationEventCreate, db: Session = Depends(get_db)):
    return crud.create_formation_event(db, event)



@router.get("/upcoming/", response_model=List[schemas.FormationEvent])
def get_upcoming_formation_events(db: Session = Depends(get_db)):
    return crud.get_upcoming_formation_events(db)

@router.get("/past/", response_model=List[schemas.FormationEvent])
def get_past_formation_events(db: Session = Depends(get_db)):
    return crud.get_past_formation_events(db)

@router.get("/approved_places/", response_model=List[schemas.ApprovedPlace])
def get_approved_places(db: Session = Depends(get_db)):
    return crud.get_approved_places(db)

@router.post("/create_place/", response_model=schemas.ApprovedPlace)
def create_approved_place(place: schemas.ApprovedPlaceCreate, db: Session = Depends(get_db)):
    return crud.create_approved_place(db, place)
