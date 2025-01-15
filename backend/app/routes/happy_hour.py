from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import draw_employees, create_event, get_upcoming_events
from app.schemas import EventCreate
from datetime import date
from app.models import Event

router = APIRouter()

@router.post("/draw/")
def draw_employees_route(department: str, num_employees: int, db: Session = Depends(get_db)):
    try:
        print(f"Received draw request: Department={department}, Number of Employees={num_employees}")  # Debugging
        employees = draw_employees(db, department, num_employees)
        print(f"Selected employees: {[{'full_name': e.full_name, 'email': e.email} for e in employees]}")  # Debugging
        return {"employees": [{"full_name": e.full_name, "email": e.email} for e in employees]}
    except ValueError as e:
        print(f"Error in draw_employees_route: {str(e)}")  # Debugging
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/event/")
def create_event_route(event: EventCreate, db: Session = Depends(get_db)):
    print("Received Event Payload:", event.dict())  # Debugging
    try:
        created_event = create_event(db, event)
        print("Created Event in DB:", created_event)  # Debugging
        return created_event
    except Exception as e:
        print(f"Error in create_event_route: {str(e)}")  # Debugging
        raise HTTPException(status_code=500, detail="Failed to create event.")


@router.get("/events/all/")
def get_all_upcoming_events(db: Session = Depends(get_db)):
    try:
        today = date.today()
        events = db.query(Event).filter(Event.date >= today).order_by(Event.date).all()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch all events.")



