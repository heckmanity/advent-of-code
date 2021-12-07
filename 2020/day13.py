import alive_progress as alive
from math import gcd
from time import time
start = time()

with open("2020/inputs/day_13_input.txt") as f:
    data = f.readlines()
arrival = int(data[0][:-1])
spread = data[1][:-1].split(",")
buses = [int(B) for B in spread if not(B=='x')]

#### PART 1 ####

first_bus = None
wait_time = 1000

for bus in buses:
    wait = bus - (arrival % bus)
    if wait < wait_time:
        wait_time = wait
        first_bus = bus

print("\nThe first bus ID times the wait time is {}".format(first_bus * wait_time))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

spread = [int(B) if not(B=='x') else 'x' for B in spread]

max_bus = max(buses)
max_bus_index = spread.index(max_bus)
offsets = []
for spr in spread:
    if type(spr)==int:
        offsets.append([spr, spread.index(spr)-max_bus_index])

offsets = sorted(offsets, key=lambda Q: Q[0], reverse=True)

timestep = max_bus
timestamp = 0

for bus_ct in range(1, len(buses)):
    found = False
    test_mod, test_off = offsets[bus_ct]
    while not(found):
        timestamp += timestep
        if (timestamp + test_off) % test_mod == 0:
            found = True
    timestep *= test_mod // gcd(timestep, test_mod)

timestamp += min([Q[1] for Q in offsets])

print("\nThe earliest timestamp matching the offsets is {}".format(timestamp))
print("Runtime: {} seconds".format(time()-start))