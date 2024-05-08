import streamlit as st
import functions

todos = functions.get_file()
def add_todo():
    new = st.session_state['action']+"\n"
    if new not in todos :
        todos.append(new)
        functions.write_list(todos)



st.title("hello from the web app")
st.subheader("this app is this app")
st.write('this app is also waht this app is ')

for index, item in enumerate(todos) :
    checkbox=st.checkbox(item , key = item)
    if checkbox :
        todos.pop(index)
        functions.write_list(todos)
        del st.session_state[item]
        st.rerun()



st.text_input(label= "enter a todo" , placeholder='type an action', on_change=add_todo , key='action')


#st.session_state