import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    input_val = st.session_state['todoInput']
    todos.append(input_val +  '\n')
    functions.write_todos(todos)
    st.session_state['todoInput'] = ''

st.title('My Todo App1')
st.subheader('This is first webapp')
st.write('This app is to increase ur productivity')

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f'todo_{index}')

st.text_input(label='Enter todo:', placeholder='Type in your todo', on_change=add_todo, key='todoInput')