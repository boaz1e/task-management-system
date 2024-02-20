# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base, Task, TaskModel
from database.database import get_db, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tasks/", response_model=Task)
def create_task(task: Task, db: Session = Depends(get_db)):
    db_task = TaskModel(title=task.title, description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return task


@app.get("/tasks/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
        return db_task  # Return the updated task from the database
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    raise HTTPException(status_code=404, detail="Task not found")
