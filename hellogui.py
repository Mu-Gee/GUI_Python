#hello there

import PySimpleGUI as sg

layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]

#Create the window
window = sg.Window("Demo", layout)

#Create event loop
while True:
    event, values = window.read()
    #End program if user closes window or
    #Presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close() 