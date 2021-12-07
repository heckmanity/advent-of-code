from functools import reduce
from time import time
start = time()

with open("2020/inputs/day_10_input.txt") as f:
    adapters = f.readlines()
adapters = sorted([int(q[:-1]) for q in adapters])

#### PART 1

adapters = [0] + adapters
adapters.append(max(adapters) + 3)
differences = [adapters[i]-adapters[i-1] for i in range(1, len(adapters))]
product = differences.count(1) * differences.count(3)

print("\nThe product of 1 jolt and 3 jolt differences is {}".format(product))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

split_list = []
sublist = []
for A in differences:
    if A==1:
        sublist.append(A)
    if A==3:
        split_list.append(sublist)
        sublist = []

groupings = [len(g) for g in split_list]
way_cts = { 0: 1, 1: 1, 2: 2, 3: 4, 4: 7 }
ways = [way_cts[g] for g in groupings]

tally = reduce(lambda x,y: x*y, ways)

print("\nThere are {} distinct ways to arrange the adapters".format(tally))
print("Runtime: {} seconds".format(time()-start))