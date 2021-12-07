from math import sqrt, floor
from time import time
start = time()

mem_loc = 347991

#### PART 1

nearest_sq = floor(sqrt(mem_loc))
if nearest_sq % 2 == 0:
    nearest_sq -= 1

coord = {'x': nearest_sq//2, 'y': nearest_sq//2}
remaining = mem_loc - nearest_sq**2
side_length = nearest_sq + 1

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

man_dist = abs(coord['x']) + abs(coord['y'])

print("\nThe number of steps required is {}".format(man_dist))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

# start = time()

# print("\nThe sum of each row's result is {}".format(result_sum))
# print("Runtime: {} seconds".format(time()-start))