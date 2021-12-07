import re
import numpy as np
from time import time
start = time()

class Point:
    def __init__(self, px, py, vx, vy):
        self.pos = np.array([px, py], dtype='int64')
        self.vel = np.array([vx, vy], dtype='int64')

    def advance(self, stps):
        '''Advances the point stps timesteps into the past/future'''
        self.pos += stps * self.vel

    def __repr__(self):
        return "Point at pos: {} with vel: {}".format(self.pos, self.vel)

with open("2018/inputs/day_10_input.txt") as f:
    raw_data = f.readlines()

parse_str = re.compile(r"""position=<\s*(?P<px>[-]*\d*),\s*
                                     \s*(?P<py>[-]*\d*)>\s*
                           velocity=<\s*(?P<vx>[-]*\d*),\s*
                                     \s*(?P<vy>[-]*\d*)>""", re.VERBOSE)

constellation = []

for datum in raw_data:
    lookup = re.match(parse_str, datum[:-1]).groupdict()
    lookup = { k:int(v) for k,v in lookup.items() }
    constellation.append(Point(**lookup))

#### PART 1 ####

def get_bounding_box(pts):
    '''returns bottom-left & top-right corners'''
    x_coords = [ P.pos[0] for P in pts ]
    y_coords = [ P.pos[1] for P in pts ]
    return [ np.array((min(x_coords), min(y_coords))), \
             np.array((max(x_coords), max(y_coords)))  ]

def get_area(corners):
    dims = abs(corners[1] - corners[0])
    return dims[0] * dims[1]

def advance_all(pts, amt):
    for P in pts:
        P.advance(amt)

def display_msg(message):
    print("\n")
    for line in message:
        print(line)
    print("\n")

prev_area = get_area(get_bounding_box(constellation))
advance_all(constellation, 1)
curr_area = get_area(get_bounding_box(constellation))

secs_passed = 1
while curr_area < prev_area:
    prev_area = curr_area
    advance_all(constellation, 1)
    secs_passed += 1
    curr_area = get_area(get_bounding_box(constellation))

advance_all(constellation, -1)
secs_passed -= 1
msg_box = get_bounding_box(constellation)

view_marg = np.array([0, 0])
view_disp = msg_box[0] - view_marg
view_dims = msg_box[1] - view_disp + view_marg + np.array([1, 1])

msg = [' ' * view_dims[0]] * view_dims[1]
for star in constellation:
    print_loc = star.pos - view_disp
    print_x = print_loc[0]
    print_y = print_loc[1]

    curr_row = msg[print_y]
    msg[print_y] = curr_row[:print_x] + '█' + curr_row[print_x + 1:]

print("\nThe message is:")
display_msg(msg)
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

real_time = secs_passed

print("\nThe elves would've need to wait {} seconds for the message to appear".format(real_time))
print("Runtime: {} seconds".format(time()-start))