from time import time
import numpy as np
start = time()

class Scanner:
    def __init__(self, num, recd_data):
        self.designation = num
        self.beacons = recd_data
        self.pos = None
        self.facing = np.array([1,0,0])
        self.heading = 0

    def roll(self, dir):
        pass

        # to rotate CW about pos x:
        # (scanner rotates CW, points rotate CCW)
        # (x,y,z) -> (x,z,-y)
        # A = [[1, 0, 0]
        #      [0, 0, 1]
        #      [0,-1, 0]]
    
    def rotate(self, axis):
        pass

    def overlaps(self, other):
        pass
    
    def __repr__(self):
        return f"Scanner {self.designation}"

scanners = []
with open("2021/inputs/day_19_input.txt") as f:
    current_scanner = None
    incoming_data = []
    for ln in f.readlines():
        if ln[0:3] == '---':
            current_scanner = int(ln.strip()[12:-4])
        elif ln == '\n':
            scanners.append(Scanner(current_scanner, incoming_data))
            current_scanner = None
            incoming_data = []
        else:
            incoming_data.append(np.array([int(c) for c in ln.strip().split(',')]))
    
    if len(scanners) == current_scanner:
        scanners.append(Scanner(current_scanner, incoming_data))
    
    scanners[0].pos = np.array([0,0,0])

print(f"\nData received from {len(scanners)} scanners...")

#### PART 1



num_beacons = 0

print(f"\nIn total, there are {num_beacons} beacons")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()



# print(f"\nThe largest magnitude of any sum from the assignment is {best_mag}")
print(f"Runtime: {time()-start} seconds")