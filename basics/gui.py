#Graphic User Interface for To-do App
import functions
import time
import FreeSimpleGUI as pSG

now = time.strftime('%b %d, %Y %H:%M:%S')

label = pSG.Text('Type in a to-do')
input_box = pSG.InputText(tooltip='Enter todo', key='todo')
add_button = pSG.Button('Add')

window = pSG.Window('Simple To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font = ('Helvetica', 16))
while True:
    event,values = window.read() #cách dặt biến destructuring giống trong JS
    match event:
        case 'Add':
            todos = functions.get_todos()
            print(todos)
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
        case pSG.WIN_CLOSED:
            break

window.close()