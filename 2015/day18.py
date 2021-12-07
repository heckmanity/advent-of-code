from alive_progress import alive_bar
from copy import deepcopy
from itertools import product
from time import time
start = time()

with open("2015/inputs/day_18_input.txt") as f:
    data = f.readlines()
initial_state = [Q[:-1] for Q in data]
light_grid = deepcopy(initial_state)
ROWS = len(light_grid)
COLS = len(light_grid[0])

def step(light_grid):
    next_grid = []
    for i in range(ROWS):
        next_row = ''
        for j in range(COLS):
            neighbor_ct = 0
            for m, n in product([-1,0,1], [-1,0,1]):
                if all([not(m==0 and n==0), i+m>=0, j+n>=0, i+m<ROWS, j+n<COLS]):
                    if light_grid[i+m][j+n]=='#':
                        neighbor_ct += 1
            if light_grid[i][j]=='#':
                if neighbor_ct==2 or neighbor_ct==3:
                    next_row += '#'
                else:
                    next_row += '.'
            else:
                if neighbor_ct==3:
                    next_row += '#'
                else:
                    next_row += '.'
        next_grid.append(next_row)
    return next_grid

#### PART 1 ####

generations = 100

print("\n")
with alive_bar(generations) as bar:
    for gen in range(generations):
        light_grid = step(light_grid)
        bar()

light_ct = 0
for row in light_grid:
    light_ct += row.count('#')

print("\nAfter {} steps there are {} lights turned on".format(generations, light_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

light_grid = deepcopy(initial_state)
for row in [0, ROWS-1]:
    light_grid[row] = '#' + light_grid[row][1:-1] + '#'

print("\n")
with alive_bar(generations) as bar:
    for gen in range(generations):
        light_grid = step(light_grid)
        for row in [0, ROWS-1]:
            light_grid[row] = '#' + light_grid[row][1:-1] + '#'
        bar()

light_ct = 0
for row in light_grid:
    light_ct += row.count('#')

print("\nWith broken corners, {} lights are on after {} steps".format(light_ct, generations))
print("Runtime: {} seconds".format(time()-start))