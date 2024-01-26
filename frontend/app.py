# app.py

import streamlit as st
import requests

# Define the base URL for the FastAPI backend
BASE_URL = "http://localhost:8000"  # Update with the appropriate URL where your FastAPI app is running

# Streamlit UI styling
st.set_page_config(
    page_title="Task Management App",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Function to fetch tasks from the FastAPI backend
def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks/")
    return response.json()

# Function to create a new task
def create_task(task_data):
    response = requests.post(f"{BASE_URL}/tasks/", json=task_data)
    return response.json()

# Function to update a task
def update_task(task_id, task_data):
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=task_data)
    return response.json()

# Function to delete a task
def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    return response.json()

# Streamlit app
def main():
    st.title("Task Management App")

    # Sidebar for task creation
    st.sidebar.header("Create New Task")
    title = st.sidebar.text_input("Title")
    description = st.sidebar.text_area("Description")
    status = st.sidebar.selectbox("Status", ["todo", "done"])
    if st.sidebar.button("Create Task"):
        new_task = {"title": title, "description": description, "status": status}
        created_task = create_task(new_task)
        st.success(f"Task '{created_task['title']}' created successfully!")

    # Display existing tasks
    tasks = get_tasks()
    if tasks:
        st.header("Existing Tasks")
        for index, task in enumerate(tasks):
            st.write(f"**Task ID:** {index + 1}")
            st.write(f"**Title:** {task['title']}")
            st.write(f"**Description:** {task['description']}")
            st.write(f"**Status:** {task['status']}")
            st.write("---")

        # Sidebar for task update and deletion
        st.sidebar.header("Update or Delete Task")
        selected_task_id = st.sidebar.number_input("Enter Task ID:", min_value=1, max_value=len(tasks))
        selected_task_index = selected_task_id - 1  # Adjust to 0-based index
        selected_task = None

        # Find the selected task
        if 0 <= selected_task_index < len(tasks):
            selected_task = tasks[selected_task_index]

        if selected_task:
            st.sidebar.subheader("Update Task")
            updated_title = st.sidebar.text_input("Title", selected_task["title"])
            updated_description = st.sidebar.text_area(
                "Description", selected_task["description"]
            )
            updated_status = st.sidebar.selectbox(
                "Status",
                ["todo", "done"],
                key=f"update_status_{selected_task_index}",  # Unique key
                index=["todo", "done"].index(selected_task["status"])
            )

            if st.sidebar.button("Update Task"):
                updated_task_data = {
                    "title": updated_title,
                    "description": updated_description,
                    "status": updated_status,
                }
                updated_task = update_task(selected_task_index + 1, updated_task_data)
                st.success(f"Task '{updated_task['title']}' updated successfully!")

            st.sidebar.subheader("Delete Task")
            if st.sidebar.button("Delete Task"):
                deleted_task = delete_task(selected_task_index + 1)
                st.warning(f"Task '{deleted_task['title']}' deleted successfully!")

if __name__ == "__main__":
    main()
