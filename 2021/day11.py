from time import time
from copy import deepcopy
from itertools import product, filterfalse
start = time()

with open("2021/inputs/day_11_input.txt") as f:
    octopodes = [ [int(e) for e in ln.strip()] for ln in f.readlines() ]

NUM_ROWS = len(octopodes)
NUM_COLS = len(octopodes[0])

#### PART 1

NUM_STEPS = 100

def take_step(octopodes):
    for rw, energies in enumerate(octopodes):
        octopodes[rw] = [ e + 1 for e in energies ]

    flashed = []
    while True:
        new_flashes = []
        for i, j in product(range(NUM_ROWS), repeat=2):
            if octopodes[i][j] > 9 and not((i, j) in flashed):
                new_flashes.append((i, j))
            
                for i_off, j_off in product(range(-1,2), repeat=2):
                    n_i, n_j = i + i_off, j + j_off
                    if n_i in range(NUM_ROWS) and n_j in range(NUM_COLS):
                        octopodes[n_i][n_j] += 1
        
        if new_flashes:
            flashed = flashed + new_flashes
        else:
            break
    
    for i, j in flashed:
        octopodes[i][j] = 0

    return octopodes, len(flashed)

flash_count = 0
for stp in range(NUM_STEPS):
    octopodes, flashes = take_step(octopodes)
    flash_count += flashes

print(f"\nThere are {flash_count} total flashes after {NUM_STEPS} steps")
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

with open("2021/inputs/day_11_input.txt") as f:
    octopodes = [ [int(e) for e in ln.strip()] for ln in f.readlines() ]

step = 0
while not all([rw.count(0)==NUM_COLS for rw in octopodes]):
    step += 1
    octopodes, _ = take_step(octopodes)

print(f"\nThe first time all octopuses flash is in step {step}")
print("Runtime: {} seconds".format(time()-start))