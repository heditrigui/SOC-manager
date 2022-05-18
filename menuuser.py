import os
import PySimpleGUI as sg
os.system('clear')
#####################################
# Define the window's contents
sg.theme('DarkGrey5')
layout = [  [sg.Text("WELCOME USER")],     # Part 2 - The Layout
            [sg.Button('Check Mail')] ,
            [sg.Button('Access FTP client')],
            [sg.Button('Website')],
            [sg.Button('Quit')]]

# Create the window
window2 = sg.Window('MENU USER', layout,keep_on_top=True).Finalize()

# Display and interact with the Window using an Event Loop
while True:
	event, values = window2.read()
# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	elif event == 'Check Mail' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx') #replace xxx.xxx.xxx.xxx with your mail server ip 
		os.system('clear')
	elif event == 'Access FTP client' : 
		os.system('filezilla') 
		os.system('clear')
	elif event == 'Website' : 
		os.system(' xdg-open xxx.xxx.xxx.xxx') #replace xxx.xxx.xxx.xxx with your web server ip 
		os.system('clear')
	elif event == sg.WIN_CLOSED:    # Window close button event
		break
window2.close()
