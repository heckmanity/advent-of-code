import re
from copy import deepcopy
from time import time
start = time()

with open("2018/inputs/day_2_input.txt") as f:
    box_ids = f.readlines()
box_ids = [bid[:-1] for bid in box_ids]

#### PART 1

blank_dict = {k:0 for k in 'abcdefghijklmnopqrstuvwxyz'}
twos_ct = threes_ct = 0

for bid in box_ids:
    current_id = deepcopy(blank_dict)
    for char in bid:
        current_id[char] += 1
    if 2 in current_id.values():
        twos_ct += 1
    if 3 in current_id.values():
        threes_ct += 1

checksum = twos_ct * threes_ct

print("\nThe checksum for the list of box IDs is {}".format(checksum))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

common_letters = ""
diff_by_one = re.compile(r"""^(\w*)\w(\w*)\-\1\w\2$""")
search_space = [box_ids[i] + "-" + box_ids[j] for i in range(len(box_ids)-1) \
                                              for j in range(i+1, len(box_ids))]

for test_str in search_space:
    test_results = re.match(diff_by_one, test_str)
    if test_results:
        common_letters = test_results.group(1) + test_results.group(2)
        break

print("\nThe common letters are {}".format(common_letters))
print("Runtime: {} seconds".format(time()-start))