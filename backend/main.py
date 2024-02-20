from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base, Task, TaskModel
from database.database import get_db, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tasks/", response_model=Task)
def create_task(task: Task, db: Session = Depends(get_db)):
    try:
        db_task = TaskModel(title=task.title, description=task.description, status=task.status)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    try:
        return db.query(TaskModel).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task:
            return task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):
    try:
        db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            for key, value in task.dict(exclude_unset=True).items():
                setattr(db_task, key, value)
            db.commit()
            db.refresh(db_task)
            return db_task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            db.delete(db_task)
            db.commit()
            return db_task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
