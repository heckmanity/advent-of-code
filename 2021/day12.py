from time import time
from copy import deepcopy
start = time()

with open("2021/inputs/day_12_input.txt") as f:
    connections = [ln.strip().split('-') for ln in f.readlines()]

all_caves = set()
for conn in connections:
    all_caves = all_caves.union(set(conn))

cave_map = { k:[] for k in list(all_caves) }
for a, b in connections:
    cave_map[a].append(b)
    cave_map[b].append(a)

#### PART 1

def explore(atlas, origin, goal, journey=[], paths=[], verbose=False):
    journey.append(origin)
    
    if origin == goal:
        paths.append(journey)
        return

    visited_small_caves = list(filter(lambda c: ord(c[0]) in range(97,123), journey))

    if not atlas[origin]:
        return

    for fork in atlas[origin]:
        if not (fork in visited_small_caves or fork==journey[0]):
            explore(atlas, fork, goal, journey=deepcopy(journey), paths=paths,\
                                                                verbose=verbose)
            
    if verbose and origin==journey[0]:
        for p in paths:
            print(','.join(p))
    
    return paths

all_paths = explore(cave_map, 'start', 'end')

print(f"\nThere are {len(all_paths)} paths through the cave system that visit small caves at most once")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

def explore_twice(atlas, origin, goal, journey=[], paths=[], verbose=False):
    journey.append(origin)
    
    if origin == goal:
        paths.append(journey)
        return

    visited_small_caves = list(filter(lambda c: ord(c[0]) in range(97,123), journey))
    
    if all([visited_small_caves.count(c) == 1 for c in visited_small_caves]):
        visited_small_caves = []

    if not atlas[origin]:
        return

    for fork in atlas[origin]:
        if not (fork in visited_small_caves or fork==journey[0]):
            explore_twice(atlas, fork, goal, journey=deepcopy(journey), paths=paths,\
                                                                        verbose=verbose)
            
    if verbose and origin==journey[0]:
        for p in paths:
            print(','.join(p))
    
    return paths

all_paths = explore_twice(cave_map, 'start', 'end')

print(f"\nThere are {len(all_paths)} paths through the cave system that visit a single small cave at most twice")
print(f"Runtime: {time()-start} seconds")