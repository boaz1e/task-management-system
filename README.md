# Task Management App

This project is a simple Task Management App with a FastAPI backend and a Streamlit frontend. The application allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks. The backend, built with FastAPI, handles data storage using MongoDB, while the frontend, created with Streamlit, provides an intuitive interface for task management.

## Features

1. **Create Task:** Users can create a new task by providing a title, description, and status (todo or done).

2. **Display Tasks:** Existing tasks are displayed, showing their title, description, and status.

3. **Update Task:** Users can update the title, description, and status of an existing task.

4. **Delete Task:** Users can delete a task.

## Technologies Used

- **FastAPI:** A modern, fast web framework for building APIs with Python.

- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

- **Streamlit:** An open-source Python library for creating web applications with minimal code.

## Setup Instructions

### Using Docker:

```bash
docker build -t task-management-app .
docker run -p 8501:8501 task-management-app
```
