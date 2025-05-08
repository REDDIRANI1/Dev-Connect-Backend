from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str

class CommentOut(BaseModel):
    id: int
    content: str
    user_id: int
    project_id: int
    created_at: datetime

    class Config:
        orm_mode = True
