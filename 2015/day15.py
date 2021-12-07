import re
from itertools import combinations
from time import time
start = time()

with open("2015/inputs/day_15_input.txt") as f:
    data = f.readlines()

parser = re.compile(r"""(?P<name>\w*): capacity (?P<capac>-?\d*), durability (?P<durab>-?\d*), flavor (?P<flav>-?\d*), texture (?P<text>-?\d*), calories (?P<calor>-?\d*)""")

ingredients = dict()
for line in data:
    info = re.match(parser, line).groupdict()
    ingredients[info['name']] = dict()
    for stat in info.keys():
        if not(stat=='name'):
            ingredients[info['name']][stat] = int(info[stat])

#### PART 1 ####

best_score = 0
for recipe in combinations(range(102), 3):
    amts = dict()
    amts['Sprinkles'] = recipe[0]
    amts['Butterscotch'] = recipe[1] - recipe[0] - 1
    amts['Chocolate'] = recipe[2] - recipe[1] - 1
    amts['Candy'] = 102 - recipe[2]

    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for ingred in ingredients.keys():
        capacity += amts[ingred] * ingredients[ingred]['capac']
        durability += amts[ingred] * ingredients[ingred]['durab']
        flavor += amts[ingred] * ingredients[ingred]['flav']
        texture += amts[ingred] * ingredients[ingred]['text']

    if all([capacity>0, durability>0, flavor>0, texture>0]):
        score = capacity * durability * flavor * texture
        if score > best_score:
            best_score = score

print("\nThe best possible score is {}".format(best_score))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

best_score = 0
for recipe in combinations(range(102), 3):
    amts = dict()
    amts['Sprinkles'] = recipe[0]
    amts['Butterscotch'] = recipe[1] - recipe[0] - 1
    amts['Chocolate'] = recipe[2] - recipe[1] - 1
    amts['Candy'] = 102 - recipe[2]

    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for ingred in ingredients.keys():
        capacity += amts[ingred] * ingredients[ingred]['capac']
        durability += amts[ingred] * ingredients[ingred]['durab']
        flavor += amts[ingred] * ingredients[ingred]['flav']
        texture += amts[ingred] * ingredients[ingred]['text']
        calories += amts[ingred] * ingredients[ingred]['calor']

    if all([capacity>0, durability>0, flavor>0, texture>0, calories==500]):
        score = capacity * durability * flavor * texture
        if score > best_score:
            best_score = score

print("\nThe best possible score with 500 calories is {}".format(best_score))
print("Runtime: {} seconds".format(time()-start))