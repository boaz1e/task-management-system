# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

# In-memory database
tasks_db = []

# Pydantic model for Task
class Task(BaseModel):
    title: str
    description: str
    status: str = "todo"

# Endpoint to create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

# Endpoint to get all tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks_db

# Endpoint to get a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = tasks_db[task_id - 1]
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint to update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id > len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id - 1] = task
    return task

# Endpoint to delete a task by ID
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id > len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks_db.pop(task_id - 1)
    return deleted_task
