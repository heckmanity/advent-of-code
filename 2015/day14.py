import re
from time import time
start = time()

parser = re.compile(r"""^(?P<name>\w*) can fly (?P<speed>\d*) km/s for (?P<move_time>\d*) seconds, but then must rest for (?P<rest_time>\d*)""")

with open("2015/inputs/day_14_input.txt") as f:
    data = f.readlines()
reindeer = [re.match(parser, Q).groupdict() for Q in data]
for rd in reindeer:
    rd['speed'] = int(rd['speed'])
    rd['move_time'] = int(rd['move_time'])
    rd['rest_time'] = int(rd['rest_time'])

race_length = 2503 # seconds

#### PART 1 ####

best_dist = 0
for rd in reindeer:
    period = rd['move_time'] + rd['rest_time']
    rd['period'] = period
    dist_per_period = rd['move_time'] * rd['speed']

    full_periods = race_length // period
    leftover_time = race_length % period

    dist_covered = full_periods * dist_per_period
    if leftover_time >= rd['move_time']:
        dist_covered += dist_per_period
    else:
        dist_covered += rd['speed'] * leftover_time

    if dist_covered > best_dist:
        best_dist = dist_covered

print("\nThe winning reindeer has travelled {} km".format(best_dist))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

locations = dict()
points = dict()
for rd in reindeer:
    locations[rd['name']] = 0
    points[rd['name']] = 0

for tick in range(race_length):
    for rd in reindeer:
        if tick % rd['period'] < rd['move_time']:
            locations[rd['name']] += rd['speed']
    
    lead_position = max(locations.values())
    for lc in locations.keys():
        if locations[lc]==lead_position:
            points[lc] += 1

max_pts = max(points.values())

print("\nThe winning reindeer will have {} points".format(max_pts))
print("Runtime: {} seconds".format(time()-start))