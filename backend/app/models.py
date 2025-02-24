from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=True)  
    company = Column(String, nullable=True)  


class PotentialRecruit(Base):
    """
    Database model for potential recruits.
    """
    __tablename__ = "potential_recruits"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    role_description = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    resume_path = Column(String, nullable=True)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, nullable=True)
    department = Column(String, index=True)
    role = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    age = Column(Integer, nullable=True)
    image_url = Column(String, nullable=True)  


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=True)
    organizer = Column(String, nullable=True)

class ApprovedPlace(Base):
    __tablename__ = "approved_places"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    website_url = Column(String, nullable=True)

class FormationEvent(Base):
    __tablename__ = "formation_events"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=True)
    organizer = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String, nullable=False, default="Formation")  # New field for filtering event type
    images = Column(Text, nullable=True)  # Store image URLs as a comma-separated string
