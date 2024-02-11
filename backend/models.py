from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    status: str = "todo"
