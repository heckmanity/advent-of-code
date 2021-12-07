from itertools import combinations
from time import time
start = time()

with open("2017/inputs/day_02_input.txt") as f:
    spreadsheet = [ln[:-1].split("\t") for ln in f.readlines()]
spreadsheet = [[int(x) for x in ln] for ln in spreadsheet]

#### PART 1

solution = 0

for row in spreadsheet:
    solution += max(row) - min(row)

print("\nThe spreadsheet's checksum is {}".format(solution))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()
result_sum = 0

for row in spreadsheet:
    for sm, lg in combinations(sorted(row), 2):
        if lg % sm == 0:
            result_sum += lg // sm
            break

print("\nThe sum of each row's result is {}".format(result_sum))
print("Runtime: {} seconds".format(time()-start))