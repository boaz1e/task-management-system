# ui_components.py

import streamlit as st

def create_task_sidebar():
    st.sidebar.header("Create New Task")
    title = st.sidebar.text_input("Title")
    description = st.sidebar.text_area("Description")
    status = st.sidebar.selectbox("Status", ["todo", "done"])
    if st.sidebar.button("Create Task"):
        return {"title": title, "description": description, "status": status}

def display_existing_tasks(tasks):
    st.header("Existing Tasks")
    for index, task in enumerate(tasks):
        st.write(f"**Task ID:** {index + 1}")
        st.write(f"**Title:** {task['title']}")
        st.write(f"**Description:** {task['description']}")
        st.write(f"**Status:** {task['status']}")
        st.write("---")

def update_delete_sidebar(tasks):
    st.sidebar.header("Update or Delete Task")
    selected_task_id = st.sidebar.number_input("Enter Task ID:", min_value=1, max_value=len(tasks))
    selected_task_index = selected_task_id - 1  # Adjust to 0-based index
    selected_task = None

    if 0 <= selected_task_index < len(tasks):
        selected_task = tasks[selected_task_index]

    return selected_task, selected_task_index
