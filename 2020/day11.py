from copy import deepcopy
from time import time
start = time()

with open("2020/inputs/day_11_input.txt") as f:
    rows = f.readlines()
layout = [[P for P in Q[:-1]] for Q in rows]

def show(LO):
    for rw in LO:
        row_str = ''
        for cl in rw:
            row_str += cl
        print(row_str)
    print("\n")

#### PART 1 ####

def advance(LO):
    next_frame = []
    for rw in range(len(LO)):
        next_row = []
        for cl in range(len(LO[0])):
            if LO[rw][cl]=='.':
                next_row.append('.')
                continue
            occ_ct = 0
            all_ct = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if i==0 and j==0:
                        continue
                    if all([rw+i>=0, rw+i<len(LO), cl+j>=0, cl+j<len(LO[0])]): 
                        state = LO[rw+i][cl+j]
                        if state=='#':
                            occ_ct += 1
            if LO[rw][cl]=='L' and occ_ct==0:
                next_row.append('#')
            elif LO[rw][cl]=='#' and occ_ct>=4:
                next_row.append('L')
            else:
                next_row.append(LO[rw][cl])
        next_frame.append(next_row)
    return(next_frame)

last_frame = deepcopy(layout)
this_frame = advance(last_frame)
while not(this_frame==last_frame):
    # show(this_frame)
    last_frame = this_frame
    this_frame = advance(last_frame)

occ_ct = 0
for rw in this_frame:
    occ_ct += rw.count('#')

print("\nUpon stabilizing, {} seats are occupied".format(occ_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

def readvance(LO):
    next_frame = []
    for rw in range(len(LO)):
        next_row = []
        for cl in range(len(LO[0])):
            if LO[rw][cl]=='.':
                next_row.append('.')
                continue
            occ_ct = 0
            all_ct = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if i==0 and j==0:
                        continue
                    mult = 1
                    move_on = False
                    while not(move_on):
                        if all([rw+mult*i>=0, rw+mult*i<len(LO), cl+mult*j>=0, cl+mult*j<len(LO[0])]): 
                            state = LO[rw+mult*i][cl+mult*j]
                            if state=='#':
                                occ_ct += 1
                            if state=='#' or state=='L':
                                move_on = True
                            if state=='.':
                                mult += 1
                        else:
                            move_on = True
            if LO[rw][cl]=='L' and occ_ct==0:
                next_row.append('#')
            elif LO[rw][cl]=='#' and occ_ct>=5:
                next_row.append('L')
            else:
                next_row.append(LO[rw][cl])
        next_frame.append(next_row)
    return(next_frame)

start = time()

last_frame = deepcopy(layout)
this_frame = readvance(last_frame)
while not(this_frame==last_frame):
    # show(this_frame)
    last_frame = this_frame
    this_frame = readvance(last_frame)

occ_ct = 0
for rw in this_frame:
    occ_ct += rw.count('#')

print("\nUpon stability with new rules, {} seats are occupied".format(occ_ct))
print("Runtime: {} seconds".format(time()-start))