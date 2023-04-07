import PySimpleGUI as sg

sg.theme('Dark Amber 5')
# Define the layout of the GUI
layout = [[sg.Text('CCTV System', font=('Helvetica', 20))],
          [sg.Canvas(size=(800, 600), background_color='gray', key='-CANVAS-')],
          [sg.Button('Exit')]]

# Create the GUI window
window = sg.Window('CCTV System', layout, background_color='#191d2b')

# Run the GUI event loop
while True:
    event, values = window.read()
    
    # Exit the program if the 'Exit' button is clicked or the window is closed
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
# Close the GUI window
window.close()
