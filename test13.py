

# name = input("Please enter You name: ")
# print("Privet " + name)
# 
# num1 = input("Enter X: ")
# num2 = input("Enter Y: ")
# summa = int(num1) + int(num2)
# print(summa)

# message = ""
# while True:
#     message = input("Enter Password ")
#     if message == 'sekret': 
#         break
#     print(message + " Password Not Correct")
# 
# print ("Password was:" + message)


mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)

print(mylist)