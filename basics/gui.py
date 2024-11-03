#Graphic User Interface for To-do App
import functions
import time
import FreeSimpleGUI as pSG

now = time.strftime('%b %d, %Y %H:%M:%S')

label = pSG.Text('Type in a to-do')
input_box = pSG.InputText(tooltip='Enter todo')
add_button = pSG.Button('Add')

window = pSG.Window('Simple To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()