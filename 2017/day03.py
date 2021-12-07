from math import sqrt, floor
from time import time
start = time()

mem_loc = 347991

#### PART 1

def spiral_to_coord(N):
    nearest_sq = floor(sqrt(N))
    if nearest_sq % 2 == 0:
        nearest_sq -= 1

    coord = {'x': nearest_sq//2, 'y': nearest_sq//2}
    remaining = N - nearest_sq**2

    if not(remaining==0):
        coord['x'] += 1
        coord['y'] += 1

    spiral_order = [ ('y', -1), ('x', -1), ('y', 1), ('x', 1) ]
    for axis, dir in spiral_order:
        if remaining==0:
            break
        num_stps = min(nearest_sq + 1, remaining)
        coord[axis] += dir * num_stps
        remaining -= num_stps
    
    return coord['x'], -coord['y']

position = spiral_to_coord(mem_loc)
man_dist = abs(position[0]) + abs(position[1])

print("\nThe number of steps required is {}".format(man_dist))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

sign = lambda x: -1 if x < 0 else 1

def coord_to_spiral(x, y):
    if abs(x) > abs(y):
        gnomon = 2 * abs(x)
        gnomon += 1 if x < 0 else 0
        abs_mult = 1 if x < 0 else -1
        stps = - abs_mult * (y + abs_mult * abs(x))
    elif abs(x) < abs(y):
        gnomon = 2 * abs(y)
        gnomon += 1 if y < 0 else 0
        abs_mult = 1 if y < 0 else -1
        stps = abs_mult * (x + abs_mult * abs(y))
    else:
        gnomon = 2 * abs(x)
        if any([x<0, y<0]):
            gnomon += 1
        stps = 0 if sign(x)==sign(y) else sign(x) * (gnomon - 1)
        
    return gnomon*gnomon - gnomon + 1 + stps
    
values = [0, 1]
current_loc = 2

while values[-1] < mem_loc:
    coord = spiral_to_coord(current_loc)
    next_val = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0:
                continue
            spiral_index = coord_to_spiral(coord[0]+i, coord[1]+j)
            if spiral_index < len(values):
                next_val += values[spiral_index]
    values.append(next_val)
    current_loc += 1

val = values[-1]

print("\nThe first written value larger than {} is {}".format(mem_loc, val))
print("Runtime: {} seconds".format(time()-start))