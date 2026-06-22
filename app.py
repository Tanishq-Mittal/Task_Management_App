import streamlit as st

st.title("📝 Task Manager")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)
        st.success("Task Added!")

st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4,1])

    with col1:
        st.write(f"{i+1}. {t}")

    with col2:
        if st.button("Delete", key=i):
            st.session_state.tasks.pop(i)
            st.rerun()
