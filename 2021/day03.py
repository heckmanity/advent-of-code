from time import time
from copy import deepcopy
import numpy as np
start = time()

with open("2021/inputs/day_3_input.txt") as f:
    output = [ln.strip('\n') for ln in f.readlines()]

def get_gamma_eps(vals):
    vals = [list(v) for v in vals]
    vals_T = [ [ row[int(i)] for row in vals ] for i in range(len(vals[0])) ]
    sums = [row.count('1') for row in vals_T]

    gamma = ''
    epsilon = ''
    half_len = len(vals) / 2
    for s in sums:
        gamma += '1' if s >= half_len else '0'
        epsilon += '0' if s >= half_len else '1'

    return gamma, epsilon

#### PART 1

G, E = get_gamma_eps(output)
power = int(G, 2) * int(E, 2)

print("\nThe power consumption of the submarine is {}".format(power))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

bit = 0
searchspace = deepcopy(output)
while len(searchspace) > 1:
    G, E = get_gamma_eps(searchspace)
    searchspace = [i for i in searchspace if i[bit]==G[bit]]
    bit += 1
oxygen = int(searchspace[0], 2)

bit = 0
searchspace = deepcopy(output)
while len(searchspace) > 1:
    G, E = get_gamma_eps(searchspace)
    searchspace = [i for i in searchspace if i[bit]==E[bit]]
    bit += 1
CO2 = int(searchspace[0], 2)

print("The life support rating is {}".format(oxygen*CO2))
print("Runtime: {} seconds".format(time()-start))