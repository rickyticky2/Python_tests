# Lesson 24 - regular ex https://regex101.com/

import re

input_filename = 'dumpfile.txt'
result_filename = 'result.txt'

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()


lookfor = r"[\w.-]+@(?!google\.ca)[A_Za-z-]+\.[\w.]+"

results = re.findall(lookfor, mytext)



for item in results:
    print(item)
    resultfile.write(item + "\n")

    


print("Tolal: " + str(len(results)))