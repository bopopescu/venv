enemy = {
           'loc_x': 70,
           'loc_y': 50,
           'color': 'green',
           'health': 100,
           'name': 'Vasya',
           'awards': ['Gold', 'Bronze']

}

all_enemis = []



for x in range(0,10):
    all_enemis.append(enemy.copy())
for ele in all_enemis:
    print(ele)

all_enemis[5]['health'] = 30
all_enemis[2]['loc_x']
for ele in all_enemis:
    print(ele)