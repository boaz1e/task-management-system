# FastAPI Task Management System

This is a simple Task Management System API built with FastAPI.

## Features

- CRUD operations on tasks (Create, Read, Update, Delete)
- Task model with title, description, and status fields
- In-memory database
- Docker support

## Requirements

- Docker

## Usage

### Running with Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-IV/task-management-system.git
   ```

2. Navigate to the project directory:

```bash
cd fastapi-task-management-system/backend
```

3. Build the Docker image:

```bash
docker build -t fastapi-task-management-system .
```

4. Run a Docker container based on the image:

```bash
docker run -d -p 8000:8000 fastapi-task-management-system
```

5. Access the API at http://localhost:8000.
