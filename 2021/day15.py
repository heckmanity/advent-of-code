from time import time
from copy import deepcopy
from queue import PriorityQueue
start = time()

class Position:
    def __init__(self, i, j, r):
        self.row = i
        self.col = j
        self.risk = r

        self.f = 1e20
        self.g = 1e20

        self.previous = None
        self.neighbors = []
    
    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Position at ({self.row},{self.col}) with risk value {self.risk}"

with open("2021/inputs/day_15_input.txt") as f:
    grid = [ [ Position(m, n, int(p)) for n, p in enumerate(ln.strip()) ] \
                                            for m, ln in enumerate(f.readlines()) ]

NUM_ROWS = len(grid)
NUM_COLS = len(grid[0])                                            

for m, rw in enumerate(grid):
    for n, cell in enumerate(rw):
        for m_off, n_off in [(1,0), (0,1), (-1,0), (0,-1)]:
            m_new = m + m_off
            n_new = n + n_off
            if all([m_new >= 0, m_new < NUM_ROWS, n_new >= 0, n_new < NUM_COLS ]):
                cell.neighbors.append(grid[m_new][n_new])

def man_dist(a, b, c, d):
    return abs(a-b) + abs(c-d)

def get_path(node):
    path = [node]
    while node.previous:
        node = node.previous
        path.append(node)
    return list(reversed(path))    

def route(start, end, h):
    open_set = PriorityQueue()
    open_set.put((start.f, start))
    start.f, start.g = 0, 0

    while not open_set.empty():
        _, current = open_set.get()
        if current == end:
            return get_path(current)

        for fork in current.neighbors:
            if current.g + fork.risk < fork.g:
                fork.previous = current
                fork.g = current.g + fork.risk
                fork.f = fork.g + h(fork.row, fork.col, NUM_ROWS, NUM_COLS)
                if not(fork in open_set.queue):
                    open_set.put((fork.f, fork))

#### PART 1

best_path = route(grid[0][0], grid[NUM_ROWS-1][NUM_COLS-1], man_dist)
lowest_risk = sum([cell.risk for cell in best_path[1:]])

print(f"\nThe lowest total risk of any path is {lowest_risk}")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

def increase_all(arr, amt):
    new = deepcopy(arr)
    for i in range(len(new)):
        for j in range(len(new[0])):
            new[i][j] += amt
            if new[i][j] > 9:
                new[i][j] -= 9
    return new

def concatenate_tiles(arr1, arr2):
    assert len(arr1)==len(arr2), "Mismatched tile sizes"
    return [ arr1[i] + arr2[i] for i in range(len(arr1)) ]

with open("2021/inputs/day_15_input.txt") as f:
    base_tile = [ [ int(r) for r in ln.strip() ] for ln in f.readlines() ]

strip = base_tile
for inc in range(1,5):
    strip = concatenate_tiles(strip, increase_all(base_tile, inc))
risk_values = strip
for inc in range(1,5):
    risk_values = risk_values + increase_all(strip, inc)

grid = [ [ Position(i, j, r) for j, r in enumerate(ln) ] for i, ln in enumerate(risk_values) ]

NUM_ROWS = len(grid)
NUM_COLS = len(grid[0])                                            

for m, rw in enumerate(grid):
    for n, cell in enumerate(rw):
        for m_off, n_off in [(1,0), (0,1), (-1,0), (0,-1)]:
            m_new = m + m_off
            n_new = n + n_off
            if all([m_new >= 0, m_new < NUM_ROWS, n_new >= 0, n_new < NUM_COLS ]):
                cell.neighbors.append(grid[m_new][n_new])

best_path = route(grid[0][0], grid[NUM_ROWS-1][NUM_COLS-1], man_dist)
lowest_risk = sum([cell.risk for cell in best_path]) - grid[0][0].risk

print(f"\nThe lowest total risk of any path in the full map is {lowest_risk}")
print(f"Runtime: {time()-start} seconds")