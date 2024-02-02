# Task Management App

This project is a simple Task Management App with a FastAPI backend and a Streamlit frontend. It allows users to create, read, update, and delete tasks. The backend is responsible for handling data storage (MongoDB) and retrieval, while the frontend provides a user-friendly interface to interact with the tasks.

## Features

- **Create Task:** Users can create a new task by providing a title, description, and status (todo or done).

- **Display Tasks:** Existing tasks are displayed, showing their title, description, and status.

- **Update Task:** Users can update the title, description, and status of an existing task.

- **Delete Task:** Users can delete a task.

## Technologies Used

- **FastAPI:** A modern, fast web framework for building APIs with Python.

- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

- **Streamlit:** An open-source Python library for creating web applications with minimal code.

## Setup Instructions

1. **Backend Setup:**

   - Install the required Python packages: `pip install fastapi[all] sqlalchemy streamlit requests`
   - Run the FastAPI backend using the command: `uvicorn backend:app --reload`

2. **Frontend Setup:**

   - Run the Streamlit frontend using the command: `streamlit run app.py`

3. **Access the App:**
   - Open your web browser and go to `http://localhost:8501` to access the Task Management App.

## API Endpoints

- **Create Task:**

  - Endpoint: `POST /tasks/`
  - Payload: `{ "title": "Task Title", "description": "Task Description", "status": "todo" }`

- **Read Tasks:**

  - Endpoint: `GET /tasks/`

- **Read Task by ID:**

  - Endpoint: `GET /tasks/{task_id}`

- **Update Task by ID:**

  - Endpoint: `PUT /tasks/{task_id}`
  - Payload: `{ "title": "Updated Title", "description": "Updated Description", "status": "done" }`

- **Delete Task by ID:**
  - Endpoint: `DELETE /tasks/{task_id}`
