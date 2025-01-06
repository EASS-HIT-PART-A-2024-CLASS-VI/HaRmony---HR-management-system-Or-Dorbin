from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import draw_employees, create_event, get_upcoming_events
from app.schemas import EventCreate

router = APIRouter()

@router.post("/draw/")
def draw_employees_route(department: str, num_employees: int, db: Session = Depends(get_db)):
    try:
        employees = draw_employees(db, department, num_employees)
        return {"employees": [{"full_name": e.full_name, "email": e.email} for e in employees]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/event/")
def create_event_route(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)

@router.get("/events/")
def get_upcoming_events_route(db: Session = Depends(get_db)):
    return get_upcoming_events(db)
