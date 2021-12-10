from time import time
from functools import reduce
start = time()

with open("2021/inputs/day_10_input.txt") as f:
    subsystem = [ ln.strip() for ln in f.readlines() ]

#### PART 1

scores = { ')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137 }

error_score = 0
corrupted_lines = []

for ln, line in enumerate(subsystem):
    stack = []
    for sym in line:
        if sym in scores.keys():
            expected = stack.pop()
            if sym==expected:
                continue
            else:
                # print(f"{line} - Expected {expected}, but found {sym} instead")
                error_score += scores[sym]
                corrupted_lines.append(ln)
        else:
            stack.append(chr(ord(sym) + (1 if sym=='(' else 2)))

print("\nThe total syntax error score is {}".format(error_score))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

scores = { ')': 1,
           ']': 2,
           '}': 3,
           '>': 4 }

for ln in corrupted_lines[::-1]:
    subsystem.pop(ln)

complete_scores = []

for line in subsystem:
    stack = []
    for sym in line:
        if sym in scores.keys():
            expected = stack.pop()
        else:
            stack.append(chr(ord(sym) + (1 if sym=='(' else 2)))
    
    # print(f"{line} - Complete by adding {''.join(stack[::-1])}")

    line_score = 0
    while len(stack) > 0:
        missing_sym = stack.pop()
        line_score *= 5
        line_score += scores[missing_sym]

    complete_scores.append(line_score)

print(f"\nThe middle autocomplete score is {sorted(complete_scores)[len(complete_scores)//2]}")
print("Runtime: {} seconds".format(time()-start))