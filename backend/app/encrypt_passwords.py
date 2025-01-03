from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from passlib.hash import bcrypt

def encrypt_passwords():
    db: Session = SessionLocal()
    users = db.query(User).all()
    for user in users:
        if not bcrypt.verify(user.password, bcrypt.hash(user.password)):
            user.password = bcrypt.hash(user.password)
    db.commit()
    db.close()

if __name__ == "__main__":
    encrypt_passwords()
