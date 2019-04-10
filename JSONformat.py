import json
filename = "user_setting.txt"
myfile = open(filename, mode='a', encoding='Latin-1')

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OREGON", "NEVADA", "NEW YORK"]
}

player2 = {
    'PlayerName': "Hilary Clinton",
    'Score': 346,
    'awards': ["COLUMBIA", "TEXAS", "NEW ORLEAN", "MISSURI", "ALASKA"]
}

MyPlayers = []
MyPlayers.append(player1)
MyPlayers.append(player2)

#------------------------SAVE-TO-JSON-------------------

json.dump(MyPlayers, myfile)
myfile.close()

#------------------------LOAD-TO-JSON--------------------
myfile = open(filename, mode='r', encoding='Latin1')
player_data = json.load(myfile)
for user in player_data:
    print("Name: " +str(user['PlayerName']))
    print("Score: " +str(user['Score']))

    for num in user['awards']:
        awN= user['awards'].index(num)+1
        print("AWARDS "+ str(awN) + " " +num )
    print("--------------------------------------------------------")
