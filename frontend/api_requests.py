# api_requests.py

import requests

BASE_URL = "http://localhost:8000"

def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks/")
    return response.json()

def create_task(task_data):
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data)
    return response.json()

def update_task(task_id, task_data):
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=task_data)
    return response.json()

def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    return response.json()
