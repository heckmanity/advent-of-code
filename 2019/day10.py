import numpy as np
from math import gcd
from copy import deepcopy
from time import time
start = time()

with open("2019/inputs/day_10_input.txt") as f:
    raw_data = f.readlines()
map_grid = [line[:-1] for line in raw_data]
map_reset = deepcopy(map_grid)
grid_size = (len(map_grid), len(map_grid[0]))

#### PART 1

def spiral_path():
    x, y, d, m = 0, 0, 1, 1
    
    while True:
        while 2 * x * d < m:
            yield np.array((x,y))
            x += d
        while 2 * y * d < m:
            yield np.array((x,y))
            y += d
        d *= -1
        m += 1

def count_asteroids(grid):
    tally = 0
    for rw in grid:
        tally += rw.count('#')
    return tally

visible = []
map_grid = deepcopy(map_reset)
for rw in range(len(map_grid)):
    for cl in range(len(map_grid[rw])):
        cell = map_grid[rw][cl]
        if not(cell=='#'):
            continue
        
        viewpoint = np.array((rw, cl))
        
asteroid_ct = 0

print("\nThe most asteroids that can be detected is {}".format(asteroid_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

# start = time()

# print("\n{} orbital transfers are required".format(len(stops)))
# print("Runtime: {} seconds".format(time()-start))