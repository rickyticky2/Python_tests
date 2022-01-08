#Lesson 10 el if else

x = 26
if x == 25:
    print("YES you Right")
else:
    print("NO you are wrong")   

age = 20

if (age <= 4):
    print("You are baby!")
elif (age > 4 ) and (age < 12):
    print("You are kid")
elif (age >=12) and (age < 19):
    print("You are teen")
else:
    print("you are old!")        


print("-----END-----")

all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
geman_cars = ['bmw', 'vw', 'audi']


if 'lada' in all_cars:
    print("Yes LADA is in the list")
else:
    print("LADA Not in the list")  



for xxxx in all_cars:
    if xxxx in geman_cars:
        print(xxxx + " is German Car")
    #else:
    #    print(xxxx + " is not German car")    
