from app import models, schemas
from sqlalchemy.orm import Session
from app.models import User, PotentialRecruit
from app.schemas import UserCreate, PotentialRecruitCreate, PotentialRecruitUpdate, ApprovedPlaceCreate
from datetime import date
from datetime import datetime
import random
from app.models import Employee
from app.models import Event
from app.schemas import EventCreate
from sqlalchemy import func

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
def get_all_potential_recruits(db: Session):
    """
    Retrieves all potential recruits from the database.
    """
    return db.query(PotentialRecruit).all()

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

def draw_employees(db: Session, department: str, num_employees: int):
    employees = db.query(Employee).filter(Employee.department == department).all()
    if len(employees) < num_employees:
        raise ValueError("Not enough employees in the selected department.")
    return random.sample(employees, num_employees)

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    print("Inserting Event into DB:", db_event)  # Debugging
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_upcoming_events(db: Session):
    today = date.today()
    return db.query(Event).filter(Event.date >= today).order_by(Event.date).all()


    
def search_employees(db: Session, name: str):
    return db.query(Employee).filter(Employee.full_name.ilike(f"%{name}%")).all()

def get_employees_by_department(db: Session):
    employees = db.query(Employee).all()
    return employees


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employees_with_birthdays(db: Session, month: int):
    return db.query(Employee).filter(func.extract('month', Employee.date_of_birth) == month).all()

def update_employee_image(db: Session, employee_id: int, image_url: str):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee:
        employee.image_url = image_url
        db.commit()
        db.refresh(employee)
    return employee


def create_formation_event(db: Session, event: schemas.FormationEventCreate):
    db_event = models.FormationEvent(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_upcoming_formation_events(db: Session):
    today = date.today()
    return db.query(models.FormationEvent).filter(models.FormationEvent.date >= today).order_by(models.FormationEvent.date).all()


def get_past_formation_events(db: Session):
    today = date.today()
    return db.query(models.FormationEvent).filter(models.FormationEvent.date < today).order_by(models.FormationEvent.date.desc()).all()


def create_approved_place(db: Session, place: ApprovedPlaceCreate):
    db_place = models.ApprovedPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def get_approved_places(db: Session):
    return db.query(models.ApprovedPlace).all()
