from pydantic import BaseModel
from typing import Optional

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


    class Config:
         from_attributes = True
