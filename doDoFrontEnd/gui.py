import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[ [label, input_box], [add_button] ])
#layout = [ [row1], [row2] , [rown]... ]  ; donde cada row tiene sus columns
window.read()
window.close()
