from itertools import permutations
from time import time
start = time()

with open("2015/inputs/day_9_input.txt") as f:
    distances = f.readlines()
distances = [Q[:-1].split(" ") for Q in distances]

dist_map = dict()
for city_pair in distances:
    city1, city2, dist = city_pair[::2]
    dist = int(dist)
    if city1 not in dist_map.keys():
        dist_map[city1] = dict()
    dist_map[city1][city2] = dist
    if city2 not in dist_map.keys():
        dist_map[city2] = dict()
    dist_map[city2][city1] = dist

#### PART 1 ####

best_route = 1e20
worst_route = 0
for route in permutations(dist_map.keys()):
    rt_dist = 0
    for i in range(len(route)-1):
        rt_dist += dist_map[route[i]][route[i+1]]
    if rt_dist < best_route:
        best_route = rt_dist
    if rt_dist > worst_route:
        worst_route = rt_dist

print("\nThe length of the shortest route is {}".format(best_route))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

print("\nThe length of the longest route is {}".format(worst_route))
print("Runtime: {} seconds".format(time()-start))