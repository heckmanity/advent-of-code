# import numpy as np
from alive_progress import alive_bar
from math import floor
from time import time
start = time()

serial_number = 9221

#### PART 1 ####

def get_power_level(x_, y_):
    rack_ID = x_ + 10
    pwr = rack_ID * y_
    pwr += serial_number
    pwr *= rack_ID
    pwr = floor(pwr / 100) % 10 - 5
    return pwr

power_grid = [ [get_power_level(x, y) for y in range(1, 301)] for x in range(1, 301) ]

def get_sq_sum(grid, i_, j_, size):
    total = 0
    for i_off in range(size):
        for j_off in range(size):
            total += grid[i_+i_off][j_+j_off]
    return total

max_power = 0
max_power_loc = None

print("\nSearching 3x3 regions...")
with alive_bar(298*298) as bar:
    for i in range(300-2):
        for j in range(300-2):
            total_power = get_sq_sum(power_grid, i, j, 3)
            if total_power > max_power:
                max_power = total_power
                max_power_loc = (i+1, j+1)
            bar()

print("\nThe largest total power is in the 3x3 region with coordinates {}".format(max_power_loc))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

# power_grid = np.array(power_grid)
# def get_sq_sum(grid, i_, j_, size):
#     area_to_sum = grid[np.ix_(np.arange(i_,i_+size), np.arange(j_,j_+size))]
#     return np.sum(area_to_sum)

max_power = 0
max_power_id = None

job_size = sum([i*i for i in range(1, 301)])

print("\nSearching all square regions...")
with alive_bar(job_size) as bar:
    for z in range(1, 301):
        coord_offset = z-1
        for i in range(300-coord_offset):
            for j in range(300-coord_offset):
                total_power = get_sq_sum(power_grid, i, j, z)
                if total_power > max_power:
                    max_power = total_power
                    max_power_id = (i+1, j+1, z)
                bar()

print("\nThe square with largest total power has identifier {}".format(max_power_id))
print("Runtime: {} seconds".format(time()-start))