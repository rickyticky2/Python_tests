# Lesson 20 - files 2 Перехват ошибок

import sys

filename = "Lessons_List.txt"

while True:
     try:
         print("Inside TRY")
         myfile = open(filename, mode='r', encoding='Latin-1')
     except Exception:
         print("Inside EXCEPT")
         print("Error Found!")
         print(sys.exc_info()[1])
         filename = input("Enter Correct file name! :")
     else:
         print("Inside ELSE")
         print(myfile.read())
         sys.exit()
   

print("==============EOF============")