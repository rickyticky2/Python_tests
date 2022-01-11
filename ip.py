# check ip

import re

ip = input("Enter IP: ")
check = r"((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))"
# Simple regex to check for an IP address: ^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$
results = re.match(check, ip)

while results == None:
    print("IP address " + ip + " is invalid!")
    ip = input("Enter IP: ")
    results = re.match(check, ip)
else:
    print("IP address " + results.group() + " is OK")

exit()