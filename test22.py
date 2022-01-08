# Lesson 22 - arguments

import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help argument")
        print("Usage of this program is python3 myfile/py argv1 argv2 ")

    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Argument NOT PROVIDED ")


os.system("ls -la > 1.txt ")
sys.exit(2)