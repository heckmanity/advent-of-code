import re
import numpy as np
from alive_progress import alive_bar
from copy import deepcopy
from time import time
start = time()

with open("2020/inputs/day_24_input.txt") as f:
    raw_data = f.readlines()
instructions = [line[:-1] for line in raw_data]

directions = {  'e': np.array((-1, 0)), 
               'ne': np.array((-1, 1)),
               'nw': np.array(( 0, 1)),
                'w': np.array(( 1, 0)), 
               'sw': np.array((1, -1)),
               'se': np.array((0, -1))  }

get_dir = re.compile(r"""[ns]?[ew]""")

#### PART 1 ####

black_tiles = dict()

for instr in instructions:
    current_tile = np.array((0, 0))
    while len(instr) > 0:
        dir_match = re.match(get_dir, instr)
        begin, end = dir_match.span()

        current_tile += directions[instr[begin:end]]
        instr = instr[end:]
    
    flip_coord = tuple(current_tile)
    if not(flip_coord in black_tiles.keys()):
        black_tiles[flip_coord] = True
    else:
        black_tiles[flip_coord] = not(black_tiles[flip_coord])

black_ct = 0
for v in black_tiles.values():
    if v:
        black_ct += 1

print("\n{} tiles are left black side up".format(black_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

days_passed = 100

print("\n")
with alive_bar(days_passed) as bar:
    for day in range(days_passed):
        tomorrows_tiles = dict()

        to_pop = []
        for k in black_tiles.keys():
            if not(black_tiles[k]):
                to_pop.append(k)
        for k in to_pop:
            black_tiles.pop(k)

        for coord, state in black_tiles.items():
            for tile in [np.array((0,0)), *directions.values()]:
                this_tile_coord = tuple(coord + tile)
                if this_tile_coord in tomorrows_tiles.keys():
                    continue

                neighbor_ct = 0
                for neighbor in directions.values():
                    neighbor_coord = tuple(coord + tile + neighbor)
                    if neighbor_coord in black_tiles.keys():
                        if black_tiles[neighbor_coord]:
                            neighbor_ct += 1

                if not(this_tile_coord in black_tiles.keys()):
                    this_tile_state = False
                else:
                    this_tile_state = black_tiles[this_tile_coord]

                if (this_tile_state and not(neighbor_ct==0 or neighbor_ct > 2)) or \
                                            (not(this_tile_state) and neighbor_ct==2):
                    tomorrows_tiles[this_tile_coord] = True
                else:
                    tomorrows_tiles[this_tile_coord] = False
                
        black_tiles = tomorrows_tiles
        bar()

black_ct = 0
for v in black_tiles.values():
    if v:
        black_ct += 1

print("\nAfter {} days, {} tiles will be black side up".format(days_passed, black_ct))
print("Runtime: {} seconds".format(time()-start))