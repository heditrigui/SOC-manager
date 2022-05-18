# SOC-manager
a gui made with python to manage krb5 and ldap for a soc 
first of all you'll need to pass the OTP verification,<br>
![image](https://user-images.githubusercontent.com/73761526/169046346-6963ca8c-f665-480c-95a2-c8e30bc6c75b.png)
![image](https://user-images.githubusercontent.com/73761526/169046428-8ab7c04f-da44-431a-9f74-95db463dabe3.png)
![image](https://user-images.githubusercontent.com/73761526/169046492-7fd422ec-8a5c-4fab-98a8-a269d8de1585.png)
![image](https://user-images.githubusercontent.com/73761526/169046565-7dd977f4-cf59-41d5-98a1-1d8534ee9f47.png)

after that you'll need to login with a user already exists in the ldap/krb5 database<br>
![image](https://user-images.githubusercontent.com/73761526/169046683-7c614c3e-3760-4d6c-be0c-cd997a7a8f0b.png)

-if the user is in the "regular user group" a menu will popup with options for a regular user 
![image](https://user-images.githubusercontent.com/73761526/169047528-ffa396ad-75fa-4b75-aaec-ce7dff4e8b29.png)

-if the user is in the "admins" group a menu will popup with administration options
![image](https://user-images.githubusercontent.com/73761526/169047599-dfaefc07-0466-4284-9e10-9e79d49cf594.png)

-if the user is in the "soc team group" a dedicated menu will popup with all the dashboards that he can chose from
![image](https://user-images.githubusercontent.com/73761526/169047662-32ff4016-6d24-4aaa-b818-2f5f62c89d85.png)


in my project i used : 
OpenLDAP 
KRB5
iREDMAIL 
FileZilla
TheHive
Cortex
MISP 
CUCKOO 
ELK
PATROWL
PFSENSE Firewall
------
requirements :
openssh 
pysimplegui 
smtplib


------
how it works : 
in your terminal just type "python3 otp.py"

------
