import os
import PySimpleGUI as sg
os.system('clear')
#####################################
# Define the window's contents
sg.theme('DarkGrey5')
layout = [  [sg.Text("WELCOME TO SOC")],     # Part 2 - The Layout
            [sg.Button('THE HIVE')] ,
            [sg.Button('CORTEX')],
            [sg.Button('MISP')],
            [sg.Button('CUCKOO')],
            [sg.Button('PATROWL')],
            [sg.Button('ELK')],
            [sg.Button('FIREWALL')],
            [sg.Button('Quit')]]

# Create the window
window3 = sg.Window('SOC MENU', layout, keep_on_top=True ).Finalize()


# Display and interact with the Window using an Event Loop
while True:
	event, values = window3.read()
# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	elif event == 'THE HIVE' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx') #replace xxx.xxx.xxx.xxx with THEHIVE server ip
		os.system('clear')
	elif event == 'CORTEX' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx') #replace xxx.xxx.xxx.xxx with CORTEX server ip 
		os.system('clear')
	elif event == 'MISP' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx') #MISP SERVER IP 
		os.system('clear')
	elif event == 'CUCKOO' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx') #CUCKOO server ip
		os.system('clear')
	elif event == 'PATROWL' : 
		os.system(' xdg-open http://xxx.xxx.xxx.xxx ') #PATROWL server ip
		os.system('clear')
	elif event == 'ELK' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx') #ELK SERVER IP
		os.system('clear')
	elif event == 'FIREWALL' : 
		os.system(' xdg-open xxx.xxx.xxx.xxx') #FIREWALL server ip 
		os.system('clear')
	
	
	elif event == sg.WIN_CLOSED:    # Window close button event
		break

window3.close()



