from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.user import User
from backend.models.project import Project

router = APIRouter()

@router.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.username.ilike(f"%{q}%")).all()
    projects = db.query(Project).filter(Project.title.ilike(f"%{q}%")).all()
    return {"users": users, "projects": projects}
