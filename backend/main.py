from fastapi import FastAPI, HTTPException
from typing import List, Optional

from models import Task
from database import tasks_db

app = FastAPI()

# Endpoint to create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks_db[len(tasks_db) + 1] = task
    return task

# Endpoint to get all tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return list(tasks_db.values())

# Endpoint to get a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = tasks_db.get(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint to update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task
    return task

# Endpoint to delete a task by ID
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db.pop(task_id)
