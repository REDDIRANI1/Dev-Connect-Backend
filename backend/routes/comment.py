from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.comment import Comment
from models.project import Project
from schemas.comment import CommentCreate, CommentOut
from dependencies import get_current_user
from models.user import User

router = APIRouter()

@router.post("/projects/{project_id}/comments", response_model=CommentOut)
def create_comment(
    project_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    new_comment = Comment(
        content=comment.content,
        user_id=current_user.id,
        project_id=project_id,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/projects/{project_id}/comments", response_model=List[CommentOut])
def get_comments(project_id: int, db: Session = Depends(get_db)):
    return db.query(Comment).filter(Comment.project_id == project_id).order_by(Comment.created_at.desc()).all()
