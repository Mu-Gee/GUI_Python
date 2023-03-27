import PySimpleGUI as sg

# Define the GUI layout
layout = [
    [sg.Text('Security System', font=('Helvetica', 20))],
    [sg.Text('Enter username'), sg.InputText(key='username')],
    [sg.Text('Enter password'), sg.InputText(key='password', password_char='*')],
    [sg.Button('Login'), sg.Button('Cancel')]
]

# Create the window
window = sg.Window('Security System', layout)

# Event loop to process events and get input values
while True:
    event, values = window.read()

    # If user closes window or clicks cancel, exit the program
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    # If user clicks login
    if event == 'Login':
        # Check if username and password are correct
        if values['username'] == 'admin' and values['password'] == '1234':
            sg.Popup('Login successful!')
        else:
            sg.Popup('Incorrect username or password')

# Close the window
window.close()
