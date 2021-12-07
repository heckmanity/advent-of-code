import re
from time import time
start = time()

with open("2015/inputs/day_8_input.txt") as f:
    data = f.readlines()
data = [Q[:-1] for Q in data]

#### PART 1 ####

minus_one_test = re.compile(r"""\\\"|\\\\""")
minus_three_test = re.compile(r"""\\x[a-f0-9][a-f0-9]""")

total_diff = 0

for ln in data:
    total_diff += len(re.findall(minus_one_test, ln))
    total_diff += 3 * len(re.findall(minus_three_test, ln))
    total_diff += 2

print("\nCode and data differ by {} characters".format(total_diff))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()
total_diff = 0

for ln in data:
    total_diff += ln.count('\"')
    total_diff += ln.count('\\')
    total_diff += 2


print("\nData and new code differ by {} characters".format(total_diff))
print("Runtime: {} seconds".format(time()-start))