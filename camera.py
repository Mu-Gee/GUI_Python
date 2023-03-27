import cv2
import PySimpleGUI as sg

# Create a capture object
cap = cv2.VideoCapture(0)

# Define the GUI layout
layout = [
    [sg.Image(filename='', key='-IMAGE-')],
    [sg.Button('Exit')]
]

# Create the window
window = sg.Window('CCTV System', layout)

# Event loop to process events and display video
while True:
    event, values = window.read(timeout=20)

    # If user closes window or clicks exit, exit the program
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    # Read the next frame from the capture object
    ret, frame = cap.read()

    # Convert the frame from BGR to RGB for PySimpleGUI
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Update the image element with the new frame
    window['-IMAGE-'].update(data=cv2.imencode('.png', img)[1].tobytes())

# Release the capture object and close the window
cap.release()
window.close()
