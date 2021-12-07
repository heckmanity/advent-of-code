import numpy as np
from time import time
start = time()

with open("2020/inputs/day_12_input.txt") as f:
    data = f.readlines()
instructions = [[Q[0], int(Q[1:-1])] for Q in data]

#### PART 1 ####

class Ship:
    def __init__(self):
        self.reset()
        self.NSEW = { 'N': np.array([0,  1]),
                      'S': np.array([0, -1]),
                      'E': np.array([ 1, 0]),
                      'W': np.array([-1, 0]) }
    
    def forward(self, amt):
        self.pos += amt * self.dir
    
    def fwd_WP(self, mult):
        self.pos += mult * self.waypoint
    
    def rotate(self, deg):
        rads = np.radians(deg)
        rot_mat = np.array([[int(np.cos(rads)), -int(np.sin(rads))], \
                            [int(np.sin(rads)),  int(np.cos(rads))]] )
        self.dir = np.matmul(rot_mat, self.dir)
    
    def rot_WP(self, deg):
        rads = np.radians(deg)
        rot_mat = np.array([[int(np.cos(rads)), -int(np.sin(rads))], \
                            [int(np.sin(rads)),  int(np.cos(rads))]] )
        self.waypoint = np.matmul(rot_mat, self.waypoint)

    def translate(self, card_dir, amt):
        self.pos += amt * self.NSEW[card_dir]
    
    def trans_WP(self, card_dir, amt):
        self.waypoint += amt * self.NSEW[card_dir]

    def get_dist(self):
        return sum(abs(self.pos))
    
    def reset(self):
        self.pos = np.array([0, 0])
        self.dir = np.array([1, 0])
        self.waypoint = np.array([10,1])
    
boat = Ship()
for cmd in instructions:
    if cmd[0] in 'NSEW':
        boat.translate(*cmd)
    if cmd[0]=='F':
        boat.forward(cmd[1])
    if cmd[0] in 'LR':
        arg = (1 - 2*(cmd[0]=='R')) * cmd[1]
        boat.rotate(arg)

dist = boat.get_dist()

print("\nThe ferry's Manhattan distance from the start point is {}".format(dist))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()
boat.reset()

for cmd in instructions:
    if cmd[0] in 'NSEW':
        boat.trans_WP(*cmd)
    if cmd[0]=='F':
        boat.fwd_WP(cmd[1])
    if cmd[0] in 'LR':
        arg = (1 - 2*(cmd[0]=='R')) * cmd[1]
        boat.rot_WP(arg)

dist = boat.get_dist()

print("\nThe ferry's Manhattan distance from the start point is *actually* {}".format(dist))
print("Runtime: {} seconds".format(time()-start))