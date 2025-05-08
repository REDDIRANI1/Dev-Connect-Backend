from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    full_name: str
    bio: str
    avatar_url: Optional[str] = None
    website: Optional[str] = None
    github: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileOut(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
