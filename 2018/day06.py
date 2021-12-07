import numpy as np
from copy import deepcopy
from alive_progress import alive_bar
from time import time
start = time()

with open("2018/inputs/day_6_input.txt") as f:
    raw_data = f.readlines()
coords = [np.array([int(c) for c in line[:-1].split(", ")]) for line in raw_data]

def man_dist(displacement):
    m_dist = 0
    for i in displacement:
        m_dist += abs(i)
    return m_dist

#### PART 1 ####

extents = max([max(coords, key=lambda x: x[i])[i] + 1 for i in range(2)])
atlas = []
for rw in range(extents):
    atlas.append([-1] * extents)

for i in range(len(coords)):
    x, y = coords[i]
    atlas[y][x] = i

atlas_reset = deepcopy(atlas)

print("\nFilling in atlas...")
with alive_bar(int(extents**2)) as bar:
    for y in range(len(atlas)):
        for x in range(len(atlas[y])):
            bar()
            pos = np.array([x, y])
            min_dist = extents * extents
            closest_coord = None
            for i in range(len(coords)):
                dis = coords[i] - pos
                dist = man_dist(dis)
                if dist < min_dist:
                    min_dist = dist
                    closest_coord = i
                elif dist == min_dist:
                    closest_coord = '.'
            atlas[y][x] = closest_coord

infinites = set()
for edge in range(0, extents, extents-1):
    for i in range(0, extents):
        infinites.add(atlas[i][edge])
        infinites.add(atlas[edge][i])

max_area = 0

for i in range(len(coords)):
    if not(i in infinites):
        area = 0
        for rw in atlas:
            area += rw.count(i)
        if area > max_area:
            max_area = area

print("\nThe size of the largest finite area is {}".format(max_area))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

atlas = deepcopy(atlas_reset)
safety_margin = 10000

print("\nFilling in atlas...")
with alive_bar(int(extents**2)) as bar:
    for y in range(len(atlas)):
        for x in range(len(atlas[y])):
            bar()
            pos = np.array([x, y])
            total_dist = 0
            for i in range(len(coords)):
                dis = coords[i] - pos
                total_dist += man_dist(dis)
            atlas[y][x] = total_dist < safety_margin

safe_area = 0

for rw in atlas:
    for cl in rw:
        if cl:
            safe_area += 1

print("\nThe size of the largest finite area is {}".format(safe_area))
print("Runtime: {} seconds".format(time()-start))