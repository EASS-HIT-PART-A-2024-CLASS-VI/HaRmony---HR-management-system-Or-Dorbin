from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=True)  
    company = Column(String, nullable=True)  


class PotentialRecruit(Base):
    """
    Database model for potential recruits.
    """
    __tablename__ = "potential_recruits"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    role_description = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
