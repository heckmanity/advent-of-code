from time import time
from copy import deepcopy
start = time()

with open("2020/inputs/day_6_input.txt") as f:
    responses = f.readlines()

#### PART 1

current_group = set()
yes_ct_sum = 0
for resp in responses:
    if resp=="\n":
        yes_ct_sum += len(current_group)
        current_group = set()
        continue
    for char in resp[:-1]:
        current_group.add(char)

print("\nThe sum of the 'anyone'-counts is {}".format(yes_ct_sum))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

dict_reset = {letter:0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
current_group = deepcopy(dict_reset)
grp_members = 0
yes_ct_sum = 0
for resp in responses:
    if resp=="\n":
        for val in current_group.values():
            if val==grp_members:
                yes_ct_sum += 1

        grp_members = 0
        current_group = deepcopy(dict_reset)
        continue
    for char in resp[:-1]:
        current_group[char] += 1
    grp_members += 1

print("\nThe sum of the 'everyone'-counts is {}".format(yes_ct_sum))
print("Runtime: {} seconds".format(time()-start))