# Lesson 19 files

inputfile = 'user_namaes.txt'

myfile = open(inputfile, mode='r', encoding='utf_8')

for num, line  in enumerate(myfile):
      if "Tonya" in line:
          print("Line №: " + str(num) + " : " + line.strip())

myfile.close()

#----------------------------PASS__________________


inputfile = 'list_of_password.txt'
outputfile = 'my_password.txt'

password_tolookfor = "connect"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')


for num, line  in enumerate(myfile1):
      if password_tolookfor in line:
          print("Line №: " + str(num) + " : " + line.strip())
          myfile2.write("Found password: " + line)

myfile1.close()
myfile2.close()          