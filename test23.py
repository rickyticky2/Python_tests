# Lesson 23 - regular expression

import re

mytext = "Vasya aaaaa 1972, Kolya - 1972: Olesya 1989, aaaaa@intel.com, " \
         "bbbbbbbbbbb@intel.com, Petya gggggg, 1992,cccccc@yahoo.com, " \
         "dddddddddddd@intel.com, Vasya@yandex.net, hello hello, Misha #43 1984" \
         "Vladimir 1977, Irina, 2001, annnnnn@intel.com, eeeee@yandex.com, " \
         "ooooooooooooo@hotmail.gov, gggggggggggg@gov.gov, tutututut@giv.hot"

"""
# https://generatedata.com/

\d  =  Any Digit
\D  =  Any non DIGIT
\w  =  Any Alphabet symbol
\W  =  Any non Alphabet symbol
\s  = breackspace
\S non breavkspace 
[0-9]{4}
[A-Z][a-z]+   =  names
\w+@\w+\.\w+

"""

textlookfor = r"\w+@\w+\.\w+"
allresult = re.findall(textlookfor, mytext)
print(allresult)