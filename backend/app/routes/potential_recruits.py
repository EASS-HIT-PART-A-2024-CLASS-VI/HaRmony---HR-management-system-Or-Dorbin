from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.models import PotentialRecruit
import shutil
import os

router = APIRouter()


UPLOAD_DIR = "uploads/resumes/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=schemas.PotentialRecruit)
def create_recruit(recruit: schemas.PotentialRecruitCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new potential recruit.
    """
    return crud.create_potential_recruit(db=db, recruit=recruit)

@router.get("/", response_model=list[schemas.PotentialRecruit])
def get_all_recruits(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all potential recruits.
    """
    return crud.get_all_potential_recruits(db)

@router.get("/search/", response_model=list[schemas.PotentialRecruit])
def search_recruits(keyword: str, db: Session = Depends(get_db)):
    """
    Endpoint to search recruits by keyword.
    """
    if not keyword:
        raise HTTPException(status_code=400, detail="Keyword is required.")
    return crud.search_potential_recruits(db, keyword)

@router.delete("/{recruit_id}", response_model=schemas.PotentialRecruit)
def delete_recruit(recruit_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a recruit by ID.
    """
    recruit = crud.delete_potential_recruit(db, recruit_id)
    if not recruit:
        raise HTTPException(status_code=404, detail="Recruit not found")
    return recruit


@router.post("/{recruit_id}/upload_resume/")
async def upload_resume(recruit_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Endpoint to upload a resume for a specific recruit.
    """
    file_path = os.path.join(UPLOAD_DIR, f"{recruit_id}.pdf")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    recruit = db.query(PotentialRecruit).filter(PotentialRecruit.id == recruit_id).first()
    if not recruit:
        raise HTTPException(status_code=404, detail="Recruit not found")

    recruit.resume_path = f"/{file_path}"  
    db.commit()

    return {"message": "Resume uploaded successfully", "url": recruit.resume_path}

@router.get("/{recruit_id}/download_resume/")
def download_resume(recruit_id: int):
    """
    Endpoint to download a resume for a specific recruit.
    """
    file_path = os.path.join(UPLOAD_DIR, f"{recruit_id}.pdf")
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Resume not found")

    headers = {
        "Content-Disposition": f"attachment; filename=resume_{recruit_id}.pdf",
        "Content-Type": "application/pdf"
    }
    
    return FileResponse(file_path, headers=headers)


