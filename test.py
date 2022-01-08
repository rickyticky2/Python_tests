# Lesson 8 massive

cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(cities)
print(len(cities))

print(cities[0])
print(cities[-1])
print(cities[2].upper())

cities[2] = 'Tula'
print(cities)

cities.append('Kursk')
cities.append('Yalta')
print(cities)

cities.insert(2, 'Feodosia')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop(-2)
print("Deleted city is: " + deleted_city)
print(cities)

cities.reverse()
print(cities)