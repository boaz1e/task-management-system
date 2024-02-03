# app.py

import streamlit as st
from api_requests import get_tasks, create_task, update_task, delete_task
from ui_components import create_task_sidebar, display_existing_tasks, update_delete_sidebar

def main():
    st.set_page_config(
        page_title="Task Management App",
        page_icon="✅",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    st.title("Task Management App")

    new_task_data = create_task_sidebar()
    if new_task_data:
        created_task = create_task(new_task_data)
        st.success(f"Task '{created_task['title']}' created successfully!")

    tasks = get_tasks()
    if tasks:
        display_existing_tasks(tasks)

        selected_task, selected_task_index = update_delete_sidebar(tasks)

        if selected_task:
            updated_title = st.sidebar.text_input("Title", selected_task["title"])
            updated_description = st.sidebar.text_area("Description", selected_task["description"])
            updated_status = st.sidebar.selectbox("Status", ["todo", "done"], key=f"update_status_{selected_task['id']}", index=["todo", "done"].index(selected_task["status"]) if selected_task["status"] in ["todo", "done"] else 0)


            if st.sidebar.button("Update Task"):
                updated_task_data = {"title": updated_title, "description": updated_description, "status": updated_status}
                update_task(selected_task['id'], updated_task_data)  
                st.success(f"Task '{updated_title}' updated successfully!")

                st.experimental_rerun()

            if st.sidebar.button("Delete Task"):
                deleted_task = delete_task(selected_task['id']) 
                st.warning(f"Task '{deleted_task['title']}' deleted successfully!")

if __name__ == "__main__":
    main()
