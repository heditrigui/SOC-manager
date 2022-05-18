import os 
print('hello')
username=input("give username")
###adding to krb5#####
os.system('ssh -i foo root@xxx.xxx.xxx.xxx kadmin.local addprinc %s'%username) #replace xxx.xxx.xxx.xxx with your krb5 server ip
#####write ldif file######
answer=['admin','user','soc']
print("admin / user /soc ?")
a=input()
gid=0
while a in answer:
	if a=="soc":
		gid=1315

	elif a =="admin":
		gid= 1314
		
	elif a=="user":
		gid=1313

	else: 
		print("wrong choice")
		
	break
print(gid)
uid=input("uid= ")
with open('readme.ldif', 'w') as f: #replace xxx with your ldap config 
    f.write("""dn: cn=%s xxx,ou=people,dc=xxx,dc=com 
uid: %s
loginShell: /bin/bash
homeDirectory: /home/%s
cn: %s
uidNumber: %s
sn: %s
objectClass: posixAccount
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: person
givenName: %s
gidNumber: %d
"""%(username,username,username,username,uid,username,username,gid))
#####adding ldif file to openldap###########""
os.system('sudo ldapadd -h xxx.xxx.xxx.xxx -x -D cn=admin,dc=xxx,dc=com -W -f readme.ldif') #replace xxx.xxx.xxx.xxx with your openldap server ip  and xxx with your ldap config
os.system('rm readme.ldif')


