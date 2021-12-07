from alive_progress import alive_bar
from itertools import product
from time import time
start = time()

cycles = 6

with open("2020/inputs/day_17_input.txt") as f:
    raw_data = f.readlines()

LAYS = 2*cycles + 1
ROWS = 2*cycles + len(raw_data)
COLS = 2*cycles + len(raw_data[0][:-1])
cube_space = [['.'*COLS for j in range(ROWS)] for i in range(LAYS)]

data_ind = 0
for rw in range(cycles, cycles+len(raw_data)):
    cube_space[cycles][rw] = ('.'*cycles) + raw_data[data_ind][:-1] + ('.'*cycles)
    data_ind += 1

offsets = [-1,0,1]

def get_layer_active_3D(lyr):
    active = 0
    for rw in lyr:
        active += rw.count('#')
    return active

def step_3D(time_slice):
    next_slice = []

    lyr_cts = [get_layer_active_3D(L) for L in time_slice]
    # print(lyr_cts)

    for i in range((LAYS // 2) + 1):
        next_layer = []
        sandwich_ct = sum(lyr_cts[max(0, i-1):min(i+2, LAYS)])
        if sandwich_ct == 0:
            next_slice.append(['.'*COLS for r in range(ROWS)])
            continue

        for j in range(ROWS):
            next_row = ''
            for k in range(COLS):
                neighbor_ct = 0
                for m, n, p in product(offsets, offsets, offsets):
                    tests = [not(m==0 and n==0 and p==0), i+m>=0, i+m<LAYS, \
                        j+n>=0, k+p>=0, j+n<ROWS, k+p<COLS] 
                    if all(tests):
                        if time_slice[i+m][j+n][k+p]=='#':
                            neighbor_ct += 1
                if time_slice[i][j][k]=='#':
                    if neighbor_ct==2 or neighbor_ct==3:
                        next_row += '#'
                    else:
                        next_row += '.'
                else:
                    if neighbor_ct==3:
                        next_row += '#'
                    else:
                        next_row += '.'
            next_layer.append(next_row)
        next_slice.append(next_layer)
    
    for lyr_ind in range(len(next_slice)-2, -1, -1):
        next_slice.append(next_slice[lyr_ind])

    return next_slice

def show_layers_3D(cube):
    for lyr in cube:
        print("\n")
        for row in lyr:
            print(row)

#### PART 1 ####

print("\n")
with alive_bar(cycles) as bar:
    for cyc in range(cycles):
        cube_space = step_3D(cube_space)
        bar()

active_ct = 0
for lyr in cube_space:
    active_ct += get_layer_active_3D(lyr)

print("\nThere are {} active cubes after the sixth cycle".format(active_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

HYPS = 2*cycles + 1
hypercube_space = [[['.'*COLS for k in range(ROWS)] for j in range(LAYS)] for i in range(HYPS)]

data_ind = 0
for rw in range(cycles, cycles+len(raw_data)):
    hypercube_space[cycles][cycles][rw] = ('.'*cycles) + raw_data[data_ind][:-1] + ('.'*cycles)
    data_ind += 1

def get_layer_active_4D(hyp):
    active = 0
    for lyr in hyp:
        for rw in lyr:
            active += rw.count('#')
    return active

def step_4D(time_slice):
    next_slice = []

    cube_cts = [get_layer_active_4D(H) for H in time_slice]
    # print(cube_cts)

    for h in range((HYPS // 2) + 1):
        next_cube = []
        sandwich_ct = sum(cube_cts[max(0, h-1):min(h+2, HYPS)])
        if sandwich_ct == 0:
            next_slice.append([['.'*COLS for r in range(ROWS)] for s in range(LAYS)])
            continue
        
        for i in range((LAYS // 2) + 1):
            next_layer = []
            for j in range(ROWS):
                next_row = ''
                for k in range(COLS):
                    neighbor_ct = 0
                    for m, n, p, q in product(offsets, offsets, offsets, offsets):
                        tests = [not(all([m==0, n==0, p==0, q==0])), h+m>=0, h+m<HYPS, \
                            i+n>=0, i+n<LAYS, j+p>=0, j+p<ROWS, k+q>=0, k+q<COLS] 
                        if all(tests):
                            if time_slice[h+m][i+n][j+p][k+q]=='#':
                                neighbor_ct += 1
                    if time_slice[h][i][j][k]=='#':
                        if neighbor_ct==2 or neighbor_ct==3:
                            next_row += '#'
                        else:
                            next_row += '.'
                    else:
                        if neighbor_ct==3:
                            next_row += '#'
                        else:
                            next_row += '.'
                next_layer.append(next_row)
            next_cube.append(next_layer)
        
        for lyr_ind in range(len(next_cube)-2, -1, -1):
            next_cube.append(next_cube[lyr_ind])
        
        next_slice.append(next_cube)

    for cube_ind in range(len(next_slice)-2, -1, -1):
        next_slice.append(next_slice[cube_ind])

    return next_slice

def show_layers_4D(hypercube):
    for cube in hypercube:
        for lyr in cube:
            print("\n")
            for row in lyr:
                print(row)

start = time()

print("\n")
with alive_bar(cycles) as bar:
    for cyc in range(cycles):
        hypercube_space = step_4D(hypercube_space)
        bar()

active_ct = 0
for cube in hypercube_space:
    active_ct += get_layer_active_4D(cube)

print("\nThere are {} active hypercubes after the sixth cycle".format(active_ct))
print("Runtime: {} seconds".format(time()-start))