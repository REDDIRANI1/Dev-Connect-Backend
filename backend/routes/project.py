from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.project import ProjectCreate, ProjectOut
from models.project import Project
from dependencies import get_current_user
from models.user import User
from typing import List

router = APIRouter()

@router.post("/projects", response_model=ProjectOut)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_project = Project(**project_data.dict(), user_id=current_user.id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.get("/projects", response_model=List[ProjectOut])
def get_all_projects(db: Session = Depends(get_db)):
    return db.query(Project).order_by(Project.created_at.desc()).all()

@router.get("/projects/{user_id}", response_model=List[ProjectOut])
def get_user_projects(user_id: int, db: Session = Depends(get_db)):
    return db.query(Project).filter(Project.user_id == user_id).all()
