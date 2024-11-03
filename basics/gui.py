#Graphic User Interface for To-do App
import functions
import time
import FreeSimpleGUI as pSG

now = time.strftime('%b %d, %Y %H:%M:%S')

label = pSG.Text('Type in a to-do')
input_box = pSG.InputText(tooltip='Enter todo', key='todo') #gán key cho các giá trị trả về

listLabel = pSG.Text('To-do list')
todosItems = pSG.Listbox(values=functions.get_todos(),
                         key='todos',
                         enable_events=True,
                         size=[45, 10])

addBtn = pSG.Button('Add')
editBtn = pSG.Button('Edit')
completeBtn = pSG.Button('Complete')
exitBtn = pSG.Button('Exit')

layout = [
    [label], [input_box, addBtn],
    [listLabel],
    [todosItems, editBtn, completeBtn],
    [exitBtn]
]

window = pSG.Window('Simple To-Do App',
                    layout= layout,
                    font = ('Helvetica', 16))
while True:
    event,values = window.read() #cách dặt biến destructuring giống trong JS
    print(event, values, 'asd')
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            todoEdit = values['todos'][0]
            newTodo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todoEdit)
            todos[index] = newTodo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            curTodoName = values['todos'][0]
            window['todo'].update(value=curTodoName)
        case 'Complete':
            completeItem = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(completeItem)
            functions.write_todos(todos)

            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case pSG.WIN_CLOSED:
            break
print('Bye')
window.close()