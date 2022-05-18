import os 
from add import username
#username=input("username= ")
answer=['admin','user','soc']
print("admin / user /soc ?")
a=input()
while a in answer:
	if a == "admin":
		gid= 1313
	elif a=="user":
		gid=1314
	elif a=="soc":
		gid=1315

	break
print(gid)
uid=input("uid= ")
with open('readme.ldif', 'w') as f: #replace xxx with your openldap config 
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
