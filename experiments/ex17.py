import FreeSimpleGUI as sg


def convertir_a_metros(pies, pulgadas):
    # 1 pie = 0.3048 metros
    # 1 pulgada = 0.0254 metros
    metros = pies * 0.3048 + pulgadas * 0.0254
    return metros

sg.theme('Black')

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="green")

exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[ [label1, input1],
                            [label2, input2],
                            [convert_button, exit_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Exit":
            break
        case "Convert":
            try:
                feet = float(values["feet"])
                inches = float(values['inches'])
                m = convertir_a_metros(feet,inches)
                window["output"].update(value=f"{m} m")
            except ValueError:
                sg.popup("Please provide two numbers")
        case None:
            break

window.close()