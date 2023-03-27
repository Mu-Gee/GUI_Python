import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Text('CCTV System')],
    [sg.Graph((800, 600), (0, 600), (800, 0), key='-GRAPH-')],
    [sg.Column([
        [sg.Text('Select video file')],
        [sg.Input(key='-FILE-', enable_events=True), sg.FileBrowse()],
        [sg.Text('Select display window')],
        [sg.Radio('Window 1', group_id='display'), sg.Radio('Window 2', group_id='display')],
        [sg.Radio('Window 3', group_id='display'), sg.Radio('Window 4', group_id='display')],
    ], element_justification='c', vertical_alignment='top')],
    [sg.Button('Start'), sg.Button('Stop'), sg.Button('Exit')]
]

# Create the GUI window
window = sg.Window('CCTV System', layout, finalize=True)

# Initialize the graph object
graph = window['-GRAPH-']
graph.DrawRectangle((0, 0), (800, 600), line_color='black')

# Define a function to display the video file in the selected window
def display_video(filename, window_num):
    # You would need to write the code to display the video here
    pass

# The main event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Start':
        filename = values['-FILE-']
        if filename:
            if values['display'] == 0:
                display_video(filename, 1)
            elif values['display'] == 1:
                display_video(filename, 2)
            elif values['display'] == 2:
                display_video(filename, 3)
            else:
                display_video(filename, 4)

    if event == 'Stop':
        # You would need to write the code to stop the video here
        pass

# Close the window
window.close()
