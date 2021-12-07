from time import time
from copy import deepcopy
start = time()

with open("2017/inputs/day_06_input.txt") as f:
    banks = [int(num) for num in f.readline().strip().split('\t')]

MEMORY_SIZE = len(banks)

#### PART 1

cycle = 0
prev_states = []

while not(banks in prev_states):
    prev_states.append(deepcopy(banks))
    index = max(range(MEMORY_SIZE), key=lambda i: banks[i])
    pot = banks[index]
    banks[index] = 0

    index += 1
    while pot > 0:
        banks[index % MEMORY_SIZE] += 1
        pot -= 1
        index += 1

    cycle += 1

print("\nThe configuration repeats after {} redistribution cycles".format(cycle))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

first_occurrence = prev_states.index(banks)
loop_size = len(prev_states) - first_occurrence

print("\nThere are {} cycles in the infinite loop".format(loop_size))
print("Runtime: {} seconds".format(time()-start))