from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    full_name = Column(String)
    bio = Column(String)
    avatar_url = Column(String, nullable=True)
    website = Column(String, nullable=True)
    github = Column(String, nullable=True)

    user = relationship("User", back_populates="profile")
