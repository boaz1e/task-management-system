# models.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(1024))
    status = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    status: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Task Title",
                "description": "Task Description",
                "status": "Pending"
            }
        }
