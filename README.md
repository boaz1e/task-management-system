# Task Management App

This project is a simple Task Management App with a FastAPI backend and a Streamlit frontend. The application allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks. The backend, built with FastAPI, handles data storage using MySQL, while the frontend, created with Streamlit, provides an intuitive interface for task management.

![image](https://github.com/boaz1e/task-management-system/assets/108184198/0f84cb4e-efc6-485b-bc6d-970977a1dba9)

## Features

1. **Create Task:** Users can create a new task by providing a title, description, and status (todo or done).

2. **Display Tasks:** Existing tasks are displayed, showing their title, description, and status.

3. **Update Task:** Users can update the title, description, and status of an existing task.

4. **Delete Task:** Users can delete a task.

## Technologies Used

- **FastAPI:** A modern, fast web framework for building APIs with Python.
- **MySQL:** A relational database management system used for storing task data.
- **Streamlit:** An open-source Python library for creating web applications with minimal code.

## Requirements

- Docker

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/boaz1e/task-management-system.git
   ```
2. Navigate to the project directory:

```
cd task-management-system
```

3. Build and run the Docker containers:

```
docker-compose up
```

Access the Streamlit frontend at ```localhost:8501``` to manage tasks.

To test the backend API, navigate to ```localhost:8000/docs``` for the interactive API documentation provided by FastAPI.


[![Video](https://img.youtube.com/vi/QLGogzCX0m4/0.jpg)](https://www.youtube.com/watch?v=QLGogzCX0m4)

