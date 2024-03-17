from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.main import app, get_db
from backend.models import Task

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Task 1", "description": "Description 1", "status": "pending"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task 1"
    assert data["description"] == "Description 1"
    assert data["status"] == "pending"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_read_task():
    response = client.post("/tasks/", json={"title": "Task 2", "description": "Description 2", "status": "completed"})
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task 2"
    assert data["description"] == "Description 2"
    assert data["status"] == "completed"

def test_update_task():
    response = client.post("/tasks/", json={"title": "Task 3", "description": "Description 3", "status": "pending"})
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={"title": "Task 3 Updated", "description": "Description 3 Updated", "status": "completed"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task 3 Updated"
    assert data["description"] == "Description 3 Updated"
    assert data["status"] == "completed"

def test_delete_task():
    response = client.post("/tasks/", json={"title": "Task 4", "description": "Description 4", "status": "pending"})
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task 4"
    assert data["description"] == "Description 4"
    assert data["status"] == "pending"
