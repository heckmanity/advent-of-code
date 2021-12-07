import re
from itertools import combinations
from copy import deepcopy
from time import time
start = time()

with open("2015/inputs/day_21_input.txt") as f:
    raw_data = f.readlines()

player_reset = {'HP': 100, 'Armor': 0, 'Damage': 0}
boss_reset = deepcopy(player_reset)

parser = re.compile(r"""(?P<Item>\w*(?:\s\+\d)*)\s*(?P<Cost>\d*)\s*(?P<Damage>\d*)\s*(?P<Armor>\d*)""")

store = dict()
reading_store = False
current_category = None
for line in raw_data:
    if reading_store:
        if ':' in line:
            category = line[:line.index(':')]
            store[category] = []
            current_category = category
        elif not(line=='\n'):
            data = re.match(parser, line[:-1]).groupdict()
            for k in data.keys():
                if not(k=='Item'):
                    data[k] = int(data[k])
            store[current_category].append(data)
    else:
        if line=="\n":
            reading_store = True
        else:
            data = line[:-1].split(": ")
            boss_reset[data[0]] = int(data[1])

#### PART 1 ####

def game(player, enemy):
    parties = [player, enemy]
    turns = [0, 1]
    while all([p['HP']>0 for p in parties]):
        attack, defend = turns
        damage_dealt = parties[attack]['Damage'] - parties[defend]['Armor']
        if damage_dealt < 1:
            damage_dealt = 1
        parties[defend]['HP'] -= damage_dealt
        turns = turns[::-1]
    
    if player['HP'] > 0:
        return True
    return False

least_gold = 500

for wpn in store['Weapons']:
    for num_armor in range(2):
        for amr in combinations(store['Armor'], num_armor):
            for num_rings in range(3):
                for rng in combinations(store['Rings'], num_rings):
                    bag_of_holding = [wpn, *amr, *rng]
                    hero = deepcopy(player_reset)
                    boss = deepcopy(boss_reset)

                    for stat in ['Damage', 'Armor']:
                        for itm in bag_of_holding:
                            hero[stat] += itm[stat]
                    
                    if game(hero, boss):
                        game_cost = sum([itm['Cost'] for itm in bag_of_holding])
                        if game_cost < least_gold:
                            least_gold = game_cost


print("\nYou must spend at least {} gold to win the fight".format(least_gold))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

most_gold = 0

for wpn in store['Weapons']:
    for num_armor in range(2):
        for amr in combinations(store['Armor'], num_armor):
            for num_rings in range(3):
                for rng in combinations(store['Rings'], num_rings):
                    bag_of_holding = [wpn, *amr, *rng]
                    hero = deepcopy(player_reset)
                    boss = deepcopy(boss_reset)

                    for stat in ['Damage', 'Armor']:
                        for itm in bag_of_holding:
                            hero[stat] += itm[stat]
                    
                    if not(game(hero, boss)):
                        game_cost = sum([itm['Cost'] for itm in bag_of_holding])
                        if game_cost > most_gold:
                            most_gold = game_cost

print("\nYou can spend at most {} gold and lose the fight".format(most_gold))
print("Runtime: {} seconds".format(time()-start))