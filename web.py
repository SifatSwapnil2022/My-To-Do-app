import streamlit as st
import fuctions
todos = fuctions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fuctions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity."
         "This allows you to organize and complete the most crucial tasks first. ")

for index, todo in enumerate(todos):

    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fuctions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo,key='new_todo')
print("hello")


