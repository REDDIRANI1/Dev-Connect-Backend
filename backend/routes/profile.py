from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.profile import ProfileCreate, ProfileOut, ProfileUpdate
from ..models.profile import Profile
from ..dependencies import get_current_user
from ..models.user import User
from ..database import get_db

router = APIRouter()

@router.post("/profile", response_model=ProfileOut)
def create_or_update_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    existing = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    if existing:
        for key, value in profile_data.dict().items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    new_profile = Profile(**profile_data.dict(), user_id=current_user.id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.get("/profile/{username}", response_model=ProfileOut)
def get_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not user.profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return user.profile
