from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
import shutil
from pathlib import Path
from typing import List

UPLOAD_DIR = Path("uploads/employees_pictures/")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

router = APIRouter()

@router.get("/", response_model=List[schemas.Employee])
def get_all_employees(db: Session = Depends(get_db)):
    employees = crud.get_employees_by_department(db)  
    return employees

@router.get("/search/", response_model=List[schemas.EmployeeBase])
def search_employees(name: str, db: Session = Depends(get_db)):
    return crud.search_employees(db=db, name=name)

@router.get("/birthdays/", response_model=List[schemas.Employee])
def get_birthdays(month: int, db: Session = Depends(get_db)):
    employees_with_birthdays = crud.get_employees_with_birthdays(db, month)
    return employees_with_birthdays



@router.post("/upload-image/")
def upload_employee_image(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"image_url": f"/employees_pictures/{file.filename}"}


@router.put("/{employee_id}/update-image/")
def update_employee_image(employee_id: int, image_url: str, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.update_employee_image(db, employee_id, image_url)
