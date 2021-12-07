import re
from copy import deepcopy
from time import time
start = time()

with open("2018/inputs/day_3_input.txt") as f:
    raw_claims = f.readlines()

#### PART 1

parser = re.compile(r"""^\#(?P<ID>\d+) \@ (?P<x>\d+)\,(?P<y>\d+)\: (?P<w>\d+)x(?P<h>\d+).*$""")

whole_cloth = [[None for i in range(1100)] for j in range(1100)]
claims = []

for clm in raw_claims:
    details = re.match(parser, clm).groupdict()
    details = {k:int(v) for (k,v) in details.items()}
    for x in range(details['x'], details['x'] + details['w']):
        for y in range(details['y'], details['y'] + details['h']):
            if whole_cloth[x][y]:
                whole_cloth[x][y] = 'X'
            else:
                whole_cloth[x][y] = details['ID']
    claims.append(details)

area = 0
for row in whole_cloth:
    area += row.count('X')

print("\nThe overlapping area is {} square inches".format(area))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

for clm in claims:
    full_area = clm['w'] * clm['h']
    unique_area = 0
    for row in whole_cloth:
        unique_area += row.count(clm['ID'])
    if unique_area==full_area:
        best_ID = clm['ID']
        break

print("\nThe ID of the non-overlapping claim is {}".format(best_ID))
print("Runtime: {} seconds".format(time()-start))