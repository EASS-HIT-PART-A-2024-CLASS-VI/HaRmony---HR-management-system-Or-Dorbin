from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    username: str
    role: str
    company: str

class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[str]
    company: Optional[str]


class User(UserBase):
    id: int

class UserLogin(BaseModel):
    username: str
    password: str


class EmployeeBase(BaseModel):
    full_name: str
    email: str
    phone_number: Optional[str] = None
    department: str
    role: str | None = None
    date_of_birth: date | None = None
    age: int | None = None
    image_url: Optional[str]

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True

class EventBase(BaseModel):
    name: str
    date: date
    location: str | None = None
    organizer: str | None = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int


    class Config:
         from_attributes = True


class PotentialRecruitBase(BaseModel):
    """
    Shared properties for potential recruits.
    """
    first_name: str
    last_name: str
    phone_number: str
    email: str
    date_of_birth: date
    age: int
    role_description: Optional[str] = None
    description: Optional[str] = None

class PotentialRecruitCreate(PotentialRecruitBase):
    """
    Properties required to create a new recruit.
    """
    pass

class PotentialRecruitUpdate(PotentialRecruitBase):
    """
    Properties required to update an existing recruit.
    """
    pass

class PotentialRecruit(PotentialRecruitBase):
    """
    Properties shared across all recruit actions.
    """
    id: int


class ApprovedPlaceBase(BaseModel):
    name: str
    location: str
    description: Optional[str] = None
    website_url: Optional[str] = None

class ApprovedPlaceCreate(ApprovedPlaceBase):
    pass

class ApprovedPlace(ApprovedPlaceBase):
    id: int

class FormationEventBase(BaseModel):
    name: str
    date: date
    location: Optional[str] = None
    organizer: Optional[str] = None
    description: Optional[str] = None
    type: str = "Formation"
    images: Optional[str] = None

class FormationEventCreate(FormationEventBase):
    pass

class FormationEvent(FormationEventBase):
    id: int
