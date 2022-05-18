import os
import PySimpleGUI as sg
os.system('clear')
#####################################
# Define the window's contents
sg.theme('DarkGrey5')
layout = [  [sg.Text("WELCOME ADMIN")],     # Part 2 - The Layout
            [sg.Button('web server')] ,
            [sg.Button('mail server dashboard')],
            [sg.Button('admin mail account')],
            [sg.Button('check mail account')],
            [sg.Button('ldap account manager')],
            [sg.Button('FTP client')],
            [sg.Button('add to krb5/ldap')],
            [sg.Button('Quit')]]

# Create the window
window3 = sg.Window('MENU AMDIN', layout, keep_on_top=True ).Finalize()


# Display and interact with the Window using an Event Loop
while True:
	event, values = window3.read()
# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	elif event == 'web server' : 
		os.system(' xdg-open https://www.google.com')
		os.system('clear')
	elif event == 'mail server dashboard' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx/netdata') #replace xxx.xxx.xxx.xxx with your mail server ip 
		os.system('clear')
	elif event == 'FTP client' : 
		os.system('filezilla')
		os.system('clear')
	elif event == 'admin mail account' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx/iredadmin') #replacce  xxx.xxx.xxx.xxx with your mail server ip
		os.system('clear')
	elif event == 'ldap account manager' : 
		os.system(' xdg-open http://xxx.xxx.xxx.xxx/lam ') #replace xxx.xxx.xxx.xxx with your openldap server ip 
		os.system('clear')
	elif event == 'check mail account' : 
		os.system(' xdg-open https://xxx.xxx.xxx.xxx/sogo') #replace xxx.xxx.xxx.xxx with your email server ip 
		os.system('clear')
	elif event == 'add to krb5/ldap' : 
		os.system('gnome-terminal  -e "python3 /home/user/Desktop/python/gui/add.py"')
		os.system('clear')
	elif event == sg.WIN_CLOSED:    # Window close button event
		break

window3.close()



