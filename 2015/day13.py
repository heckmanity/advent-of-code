import re
from itertools import permutations
from time import time
start = time()

parser = re.compile(r"""(?P<seated>\w*) would (?P<sign>\w*) (?P<amt>\d*) happiness units by sitting next to (?P<neighbor>\w*).""")

with open("2015/inputs/day_13_input.txt") as f:
    data = f.readlines()
happy_data = [re.match(parser, Q).groupdict() for Q in data]

happy_dict = dict()
for datum in happy_data:
    if not(datum['seated'] in happy_dict.keys()):
        happy_dict[datum['seated']] = dict()
    delta = int(datum['amt'])
    if datum['sign']=='lose':
        delta *= -1
    happy_dict[datum['seated']][datum['neighbor']] = delta

#### PART 1 ####

happiest = 0
guests = list(happy_dict.keys())
guests.pop(0)

for arr in permutations(guests):
    arr = list(arr)
    arr += ["Alice"]
    current_happy = 0
    for seat in range(len(arr)):
        seat_filler = arr[seat]
        for nbr in [-1, 1]:
            neighbor = arr[(seat + nbr) % len(arr)]
            current_happy += happy_dict[seat_filler][neighbor]
    if current_happy > happiest:
        happiest = current_happy

print("\nThe optimal change in happiness is {}".format(happiest))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

happy_dict['Me'] = dict()
for k in happy_dict.keys():
    happy_dict[k]['Me'] = 0
    happy_dict['Me'][k] = 0

guests.append('Me')

happiest = 0
for arr in permutations(guests):
    arr = list(arr)
    arr += ["Alice"]
    current_happy = 0
    for seat in range(len(arr)):
        seat_filler = arr[seat]
        for nbr in [-1, 1]:
            neighbor = arr[(seat + nbr) % len(arr)]
            current_happy += happy_dict[seat_filler][neighbor]
    if current_happy > happiest:
        happiest = current_happy

print("\nThe optimal change in happiness is *actually* {}".format(happiest))
print("Runtime: {} seconds".format(time()-start))