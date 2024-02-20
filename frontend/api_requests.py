# api_requests.py
import httpx

BASE_URL = "http://backend:8000"

async def get_tasks():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/tasks/")
        return response.json()

async def create_task(task_data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/tasks/", json=task_data)
        return response.json()

async def update_task(task_id, task_data):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/tasks/{task_id}", json=task_data)
        return response.json()

async def delete_task(task_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/tasks/{task_id}")
        return response.json()
