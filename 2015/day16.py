import re
from time import time
start = time()

parser = re.compile(r"""Sue (?P<num>\d*): (?P<att1>\w*): (?P<val1>\d*), (?P<att2>\w*): (?P<val2>\d*), (?P<att3>\w*): (?P<val3>\d*)""")

with open("2015/inputs/day_16_input.txt") as f:
    data = f.readlines()
data = [re.match(parser, Q).groupdict() for Q in data]

Sues = dict()
for datum in data:
    Sue_num = int(datum['num'])
    Sues[Sue_num] = dict()
    Sues[Sue_num][datum['att1']] = int(datum['val1'])
    Sues[Sue_num][datum['att2']] = int(datum['val2'])
    Sues[Sue_num][datum['att3']] = int(datum['val3'])

gifter_Sue = { 'children': 3,
               'cats': 7,
               'samoyeds': 2,
               'pomeranians': 3,
               'akitas': 0,
               'vizslas': 0,
               'goldfish': 5,
               'trees': 3,
               'cars': 2,
               'perfumes': 1 }

#### PART 1 ####

for Aunt_Sue in range(1, 501):
    possible = True
    for ky in Sues[Aunt_Sue].keys():
        if not(Sues[Aunt_Sue][ky]==gifter_Sue[ky]):
            possible = False
            continue
    if possible:
        break

print("\nThe gift is from Sue #{}".format(Aunt_Sue))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

for Aunt_Sue in range(1, 501):
    possible = True
    for ky in Sues[Aunt_Sue].keys():
        if ky=='cats' or ky=='trees':
            if not(Sues[Aunt_Sue][ky]>gifter_Sue[ky]):
                possible = False
                continue
        elif ky=='pomeranians' or ky=='goldfish':
            if not(Sues[Aunt_Sue][ky]<gifter_Sue[ky]):
                possible = False
                continue
        else:
            if not(Sues[Aunt_Sue][ky]==gifter_Sue[ky]):
                possible = False
                continue
    if possible:
        break

print("\nThe gift is *really* from Sue #{}".format(Aunt_Sue))
print("Runtime: {} seconds".format(time()-start))