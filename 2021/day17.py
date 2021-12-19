from time import time
from itertools import product
import re
start = time()

pattern_string = r"""target area: x=(?P<x_min>[-]*\d+)..(?P<x_max>[-]*\d+), y=(?P<y_min>[-]*\d+)..(?P<y_max>[-]*\d+)"""
parser = re.compile(pattern_string)

with open("2021/inputs/day_17_input.txt") as f:
    target_specs = parser.search(f.readline().strip()).groupdict()

sign = lambda x: 0 if x==0 else abs(x) // x

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vec2D(x,y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __repr__(self):
        return f"<{self.x}, {self.y}>"

class Probe:
    def __init__(self, vel):
        self.pos = Vec2D(0, 0)
        self.vel = Vec2D(*vel)
        self.acc = Vec2D(-sign(self.vel.x), -1)

    def update(self):
        self.pos += self.vel
        self.vel += self.acc
        if self.vel.x == 0:
            self.acc.x = 0
    
    def in_area(self, min_r, max_r):
        return all([ self.pos.x <= max_r.x, self.pos.x >= min_r.x, \
                     self.pos.y <= max_r.y, self.pos.y >= min_r.y ])

min_range = Vec2D(int(target_specs['x_min']), int(target_specs['y_min']))
max_range = Vec2D(int(target_specs['x_max']), int(target_specs['y_max']))

#### PART 1

best_y = min_range.y * (min_range.y + 1) // 2

print(f"\nThe highest y position the probe can reach is {best_y}")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

success_count = 0
for vx, vy in product(range(0, max_range.x + 1), range(min_range.y, -min_range.y + 1)):
    probe_sim = Probe((vx, vy))
    while probe_sim.pos.x <= max_range.x and probe_sim.pos.y >= min_range.y:
        probe_sim.update()
        if probe_sim.in_area(min_range, max_range):
            success_count += 1
            break

print(f"\nThere are {success_count} distinct initial velocity values which reach the target area")
print(f"Runtime: {time()-start} seconds")