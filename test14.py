# Lesson 14 - funktions 1

def napechatat_privetstvie(name):
    """Print Privetstvie"""
    print("COngratuations " + name + " wish you all the beast!")
    print("Heloo Heloo Hello Heloo!!!!")


def summa(x , y):
    s = x + y
    return s  # or x+y



def factorial(x):
    """Calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet


print("-----------------------")
napechatat_privetstvie("Alex")
napechatat_privetstvie("Vasya")


x = summa(33, 22)
print(x)

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

print(factorial(1))
print(factorial(5))

