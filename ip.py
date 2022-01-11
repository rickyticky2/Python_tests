# check ip

import re
ip = 0
msg = ""

msg = input("Enter IP: ")
ip = str(msg)

check = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
results = re.match(check, ip)

if results != None:
    print("IP address " + results.group() + " is OK")
else:
    print("IP address " + msg + " is invalid")


