import random
import smtplib
import os
import time
import PySimpleGUI as sg
a=random.randint(10000,99999)
print (a)
x=str(a)

sg.theme('DarkGrey5')
layout = [[sg.Text('OTP VERIFICATION', font='Default 18')],

[sg.T('Enter your email:'), sg.Input(key='-EMAIL TO-', size=(35,1))],
[sg.Button('Send')],
[sg.T('Enter OTP:'), sg.Input(key='-key-', size=(35,1))],
[sg.Button('Verif')]]

# Create the window
window1= sg.Window('OTP', layout, resizable=True, finalize=True,element_justification='c').Finalize()
window1.Maximize()
while True :
	event, values = window1.read()
	otp =values['-key-']
	usremail = values['-EMAIL TO-']
	if event == 'Send':
		try:
			gmail_user = 'xxx@xxx.xxx' #replace it with your email
			gmail_password = 'xxxxx' #add your password here 

			sent_from = gmail_user
			print("enter your email\n")

			to = values['-EMAIL TO-']
			subject ='OTP VERIF'
			body = x

			email_text = """\
			From: %s
			To: %s
			Subject: %s

			%s
			""" % (sent_from, ", ".join(to), subject, body)	
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(gmail_user, gmail_password)
			server.sendmail(sent_from, to, email_text)
			server.close()
			sg.popup('Sending your message... this will take a moment...', background_color='red' )
			time.sleep(5)
			sg.popup('Check your email', background_color='green',keep_on_top=True )
			print ('Email sent!')
		except:
			sg.popup('email NOT SENT', background_color='red')			
			print ('Something went wrong...')
		
		
	if event == 'Verif' :
		print(otp)
		if values['-key-'] == x : 
			sg.popup('OTP is Correct', background_color='green', keep_on_top=True )
			print("Continue")
			time.sleep(3)
			
			exec(open('/home/user/Desktop/python/gui/ldap.py').read())
			
		else:
			print(otp)
			print("WRONG OTP !!")
			sg.popup('WRONG OTP', background_color='red',keep_on_top=True )
			time.sleep(3)
			print("try again")
			
			
			
		

