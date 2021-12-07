from copy import deepcopy
from time import time
start = time()

with open("2018/inputs/day_1_input.txt") as f:
    values = f.readlines()
values = [int(n[:-1]) for n in values]

#### PART 1

end_freq = sum(values)

print("\nThe resulting frequency is {}".format(end_freq))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

index = 0
total_so_far = 0
seen_totals = set()
modulus = len(values)

while not(total_so_far in seen_totals):
    seen_totals.add(total_so_far)
    total_so_far += values[index % modulus]
    index += 1

print("\nThe first repeated frequency is {}".format(total_so_far))
print("Runtime: {} seconds".format(time()-start))