
import os 
import PySimpleGUI as sg
from admin import username

layout = [  [sg.Text("What do you want to do")]]
os.system('ldapsearch -x -b "dc=xxx,dc=com" -H ldap://xxx.xxx.xxx.xxx "cn=%s*" 2>&1 | tee ldap.txt'%username) #replace xxx.xxx.xxx.xxx with your openldap server ip and xxx with your openldap config
#os.system('ldapsearch -x -b "dc=sw-masterguard,dc=com" -H ldap://169.254.30.148  "cn=%s*" 2>&1 | tee ldap.txt'%username)
#os.system ('cat ldap.txt |grep 2000 2>&1 | tee ldapusr.txt')
#os.system ('cat ldap.txt |grep 2001 2>&1 | tee ldapadmin.txt')
os.system ('cat ldap.txt |grep 1313 2>&1 | tee ldapusr.txt')
os.system ('cat ldap.txt |grep 1315 2>&1 | tee ldapsoc.txt')
os.system ('cat ldap.txt |grep 1314 2>&1 | tee ldapadmin.txt')
filesizeusr = os.path.getsize("ldapusr.txt")
filesizesoc = os.path.getsize("ldapsoc.txt")
filesizeadmin = os.path.getsize("ldapadmin.txt")
if filesizeadmin != 0:
	os.system('clear')
	exec(open('/home/user/Desktop/python/gui/menuadmin.py').read())
	#os.system('xdg-open /home/ossec/Desktop/web/sw/index.html')
	os.system('rm ldapres.txt ldap.txt')
elif filesizeusr !=0 :
	os.system('clear')
	exec(open('/home/user/Desktop/python/gui/menuuser.py').read())
	#os.system('xdg-open /home/ossec/Desktop/web/sw/index.html')
	os.system('rm ldapres.txt ldap.txt')
elif filesizesoc !=0 :
	os.system('clear')
	exec(open('/home/user/Desktop/python/gui/menusoc.py').read())
	#os.system('xdg-open /home/ossec/Desktop/web/sw/index.html')
	os.system('rm ldapres.txt ldap.txt')
else :
	sg.popup('WRONG PASSWORD / USERNAME')

