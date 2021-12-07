from copy import deepcopy
from time import time
start = time()

with open("2018/inputs/day_5_input.txt") as f:
    polymer = f.readline()[:-1]

#### PART 1

def react(atom):
    pointer_pos = 0
    while pointer_pos < len(atom) - 1:
        if atom[pointer_pos+1] == atom[pointer_pos].swapcase():
            atom = atom[:pointer_pos] + atom[pointer_pos+2:]
            pointer_pos -= 1
            if pointer_pos < 0:
                pointer_pos = 0
        else:
            pointer_pos += 1
    return len(atom)

shortened = react(polymer)

print("\nThe polymer reduces to length {}".format(shortened))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

best_ltr = None
best_length = shortened
alphabet = "abcdefghijklmnopqrstuvwxyz"

for ltr in alphabet:
    new_polymer = deepcopy(polymer)
    pointer_pos = 0
    while pointer_pos < len(new_polymer):
        if new_polymer[pointer_pos]==ltr or new_polymer[pointer_pos]==ltr.swapcase():
            new_polymer = new_polymer[:pointer_pos] + new_polymer[pointer_pos+1:]
        else:
            pointer_pos += 1
    
    new_short_length = react(new_polymer)
    if new_short_length < best_length:
        best_length = new_short_length
        best_ltr = ltr

print("\nRemove all {}/{} units for minimal length {}".format(best_ltr.swapcase(), best_ltr, best_length))
print("Runtime: {} seconds".format(time()-start))