from time import time
start = time()

with open("2019/inputs/day_3_input.txt") as f:
    raw_data = f.readlines()
wire_instructions = [w[:-1].split(',') for w in raw_data]

def man_dist(p1, p2):
    return int(abs(p1.x-p2.x) + abs(p1.y-p2.y))

class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Point(sum_x, sum_y)

    def __mul__(self, scalar):
        return Point(scalar * self.x, scalar * self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x==other.x) and (self.y==other.y)

    def __hash__(self):
        return hash((self.x, self.y))

class Segment:
    def __init__(self, bgn_, end_):
        self.bgn = bgn_
        self.end = end_
        self.horiz = True if bgn_.y==end_.y else False
        self.length = man_dist(bgn_, end_) 

    def crosses(self, other):
        '''See https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line'''

        if (self.horiz and other.horiz) or (not(self.horiz) and not(other.horiz)):
            return None

        t_num = (self.bgn.x - other.bgn.x) * (other.bgn.y - other.end.y) \
                - (self.bgn.y - other.bgn.y) * (other.bgn.x - other.end.x)
        u_num = (self.bgn.x - self.end.x) * (self.bgn.y - other.bgn.y) \
                - (self.bgn.y - self.end.y) * (self.bgn.x - other.bgn.x)
        denom = (self.bgn.x - self.end.x) * (other.bgn.y - other.end.y) \
                - (self.bgn.y - self.end.y) * (other.bgn.x - other.end.x)

        t = t_num / denom
        u = -1 * u_num / denom

        if all([t >= 0, t <= 1, u >= 0, u <= 1]):
            return Point(int(self.bgn.x + t*(self.end.x - self.bgn.x)), \
                            int(self.bgn.y + t*(self.end.y - self.bgn.y)) )
        return None

#### PART 1

def lay_wire(instructions):
    wire_build = []
    from_node = Point(0, 0)
    dirs = {'U': Point(0, 1), 'D': Point(0, -1), 'R': Point(1, 0), 'L': Point(-1, 0)}
    for instr in instructions:
        direction = instr[0]
        distance = int(instr[1:])

        to_node = from_node + dirs[direction] * distance
        wire_build.append(Segment(from_node, to_node))

        from_node = to_node
    
    return wire_build

wires = [lay_wire(w) for w in wire_instructions]

crossings = []
for seg_1 in wires[0]:
    for seg_2 in wires[1]:
        potential = seg_1.crosses(seg_2)
        if potential:
            crossings.append(potential)

zero_pt = Point(0, 0)
nearest = min([man_dist(P, zero_pt) for P in crossings if not(P==zero_pt)])

print("\nNearest crossing is at Manhattan distance {}".format(nearest))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

w1_crossings = dict()
delay = 0
for seg_1 in wires[0]:
    for seg_2 in wires[1]:
        xing = seg_1.crosses(seg_2)
        if xing:
            break
    
    if xing:
        partial_dist = delay + man_dist(seg_1.bgn, xing)
        w1_crossings[xing] = partial_dist
    
    delay += seg_1.length

w2_crossings = dict()
delay = 0
for seg_2 in wires[1]:
    for seg_1 in wires[0]:
        xing = seg_2.crosses(seg_1)
        if xing:
            break
    
    if xing:
        partial_dist = delay + man_dist(seg_2.bgn, xing)
        w2_crossings[xing] = partial_dist
    
    delay += seg_2.length

total_delays = []
for xing in w1_crossings.keys():
    if xing in w2_crossings.keys() and not(xing==zero_pt):
        total_delays.append(w1_crossings[xing] + w2_crossings[xing])

fewest = min(total_delays)

print("\nFewest steps to reach an intersection is {}".format(fewest))
print("Runtime: {} seconds".format(time()-start))