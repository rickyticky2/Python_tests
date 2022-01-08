# lesson 21 - use JSON

import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'playerName' : "Donald Trump",
    'score' : 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'playerName' : "Clinton Hillary",
    'score' : 346,
    'awards': ["WT", "TX", "MI"] 
}


player3 = {
    'playerName' : "Alex Ivanov",
    'score' : 347,
    'awards': ["TO", "MO", "NO"] 
}


myplayers = []
myplayers.append(player1)
myplayers.append(player2)
myplayers.append(player3)


#--------------- SAVE by JSON --------------

json.dump(myplayers, myfile)
myfile.close()

# -----------------LOAD by JSON-----------------
myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)


for user in json_data:
    print("Player name is : " + str(user['playerName']))
    print("Player Score is : " + str(user['score']))
    print("Player Award N1: " + str(user['awards'][0]))
    print("Player Award N2: " + str(user['awards'][1]))    
    print("Player Award N3: " + str(user['awards'][2]))    
    print("----------------------------\n\n")