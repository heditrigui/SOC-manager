import os
#os.system('clear')
import PySimpleGUI as sg
sg.theme('DarkGrey5')
layout = [
[sg.Text("######## LOGIN #######")], 
[sg.Text("enter you username")],
[sg.Input(key='Username')],
[sg.Text("enter your password")],
[sg.InputText('', key='Password', password_char='*')],
[sg.Text(size=(40,1), key='-OUTPUT-')],
[sg.Button('Ok'),]]

# Create the window
window1= sg.Window('Welcome', layout, resizable=True, finalize=True).Finalize()
window1.Maximize()
while True:
	event, values = window1.read()
	username = values['Username']
	password = values['Password'] 
	
	# See if user wants to quit or window was closed
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		exit()
	elif event == 'Ok' :

		os.system('echo {0} | kinit {1}  2>&1 | tee login.txt'.format(password , username) )
		os.system("cat login.txt |grep 'incorrect' | tee -a verifpass.txt")
		os.system("cat login.txt |grep 'not found' | tee -a verifuser.txt")
		filesizepass = os.path.getsize("verifpass.txt")
		filesizeuser = os.path.getsize("verifuser.txt")
		if (filesizeuser or filesizepass) != 0:
			os.system('clear')
			sg.popup('WRONG PASSWORD / USERNAME !!')
			os.system('rm verifpass.txt verifuser.txt login.txt')
			
		else:

			exec(open('/home/user/Desktop/python/gui/ldap.py').read())

