import PySimpleGUI as sg
  
sg.theme_previewer() #creates a preview window of themes

theme_name_list = sg.theme_list()
print(theme_name_list) #get a text list of the available choices printed on the console.