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
    for task in tasks:
        st.write(f"**Task ID:** {task['id']}") 
        st.write(f"**Title:** {task['title']}")
        st.write(f"**Description:** {task['description']}")
        st.write(f"**Status:** {task['status']}")
        st.write("---")

def update_delete_sidebar(tasks):
    st.sidebar.header("Update or Delete Task")
    selected_task_id_text = st.sidebar.text_input("Enter Task ID:")
    try:
        selected_task_id = int(selected_task_id_text)
        selected_task = next((task for task in tasks if task['id'] == selected_task_id), None)

        if selected_task:
            selected_task_index = tasks.index(selected_task)
            return selected_task, selected_task_index

        st.warning(f"Task with ID {selected_task_id} not found.")

    except ValueError:
        st.warning("Please enter a valid Task ID.")

    return None, None
