# check ip

import re

ip = input("Enter IP: ")
check = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# Simple regex to check for an IP address: ^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$
results = re.match(check, ip)

while results == None:
    print("IP address " + ip + " is invalid!")
    ip = input("Enter IP: ")
    results = re.match(check, ip)
else:
    print("IP address " + results.group() + " is OK")

