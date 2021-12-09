from time import time
from functools import reduce
start = time()

with open("2021/inputs/day_9_input.txt") as f:
    heightmap = [ [int(ch) for ch in rw.strip()] for rw in f.readlines() ]

NUM_ROWS = len(heightmap)
NUM_COLS = len(heightmap[0])

#### PART 1

minimums = []
for r in range(NUM_ROWS):
    for c in range(NUM_COLS):
        this_height = heightmap[r][c]
        neighbors = []
        if r > 0:
            neighbors.append(heightmap[r-1][c])
        if r < NUM_ROWS - 1:
            neighbors.append(heightmap[r+1][c])
        if c > 0:
            neighbors.append(heightmap[r][c-1])
        if c < NUM_COLS - 1:
            neighbors.append(heightmap[r][c+1])
        
        if all([this_height < n for n in neighbors]):
            minimums.append({'r': r, 'c': c, 'ht': this_height})

risk_sum = sum([m['ht'] for m in minimums]) + len(minimums)

print("\nThe risk levels of all low points sum to {}".format(risk_sum))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

edgemap = [ ['X' if ht==9 else 0 for ht in rw] for rw in heightmap ]

def flood(grid, seed, num):
    queue = [seed]
    while len(queue) > 0:
        r, c = queue.pop(0)
        if grid[r][c]==0:
            grid[r][c] = num
            if r > 0:
                queue.append((r-1, c))
            if r < NUM_ROWS - 1:
                queue.append((r+1, c))
            if c > 0:
                queue.append((r, c-1))
            if c < NUM_COLS - 1:
                queue.append((r, c+1))
    return grid

for val, low_pt in enumerate(minimums):
    edgemap = flood(edgemap, (low_pt['r'], low_pt['c']), val+1)

areas = [ sum([rw.count(val) for rw in edgemap]) for val in range(1, len(minimums)+1) ]    
area_prod = reduce(lambda x, y: x*y, sorted(areas, reverse=True)[:3])

print("\nThe areas of the three largest basins multiply to {}".format(area_prod))
print("Runtime: {} seconds".format(time()-start))