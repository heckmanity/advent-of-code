from itertools import permutations
from time import time
start = time()

with open("2020/inputs/day_9_input.txt") as f:
    XMAS_data = f.readlines()
XMAS_data = [int(q[:-1]) for q in XMAS_data]

#### PART 1

preamble_length = 25

for index in range(25, len(XMAS_data)):
    poss_addends = XMAS_data[index-preamble_length:index]
    target_sum = XMAS_data[index]

    sums = []
    for perm in permutations(poss_addends, 2):
        sums.append(sum(perm))
    
    if not(target_sum in sums):
        first_val = target_sum
        break

print("\nThe first number that is not the sum of two in the previous {} is {}".format(preamble_length, first_val))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

start_index = 0
end_index = 1
range_sum = sum(XMAS_data[start_index:end_index])

while not(range_sum==first_val):
    if range_sum < first_val:
        end_index += 1
    if range_sum > first_val:
        start_index += 1
    range_sum = sum(XMAS_data[start_index:end_index])

contig_range = XMAS_data[start_index:end_index]
weakness = min(contig_range) + max(contig_range)

print("\nThe encryption weakness is {}".format(weakness))
print("Runtime: {} seconds".format(time()-start))