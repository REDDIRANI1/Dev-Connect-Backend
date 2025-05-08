from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile = relationship("Profile", back_populates="user", uselist=False)
    projects = relationship("Project", back_populates="user")  # must match Project.user
    comments = relationship("Comment", back_populates="user", cascade="all, delete")
