import streamlit as st
import functions
import time



todos = functions.get_todos()
def add_todo():
    """
    This function is designed for Streamlit specifically:
    It takes the text added in the input box on the webapp and
    stores it in the variable todo: It has the key new_todo.
    Then it appends the new todo to the list of todos and
    the new appended list is again stored/write in the text file
    """
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


now = time.strftime("%b %d, %Y")

st.title("My ToDo App")
st.subheader("This app is designed to increase your productivity")
st.subheader(f"Date: {now}")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new task....",
              on_change=add_todo, key="new_todo")

