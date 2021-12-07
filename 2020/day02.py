import re
from time import time
start = time()
tally = 0

rule = re.compile(r"""(?P<min_num>\d+)([-]?)
                      (?P<max_num>\d+)(\s?)
                      (?P<charact>[A-Za-z]?)([:]?\s?)
                      (?P<passstr>[A-Za-z]+)""",
                      re.VERBOSE)

def xor(A, B):
    if (A or B) and not(A and B):
        return True
    return False

with open("2020/inputs/day_2_input.txt") as f:
    all_entries = f.readlines()

checklist = [rule.search(PW).groupdict() for PW in all_entries]

#### PART 1

for item in checklist:
    item['min_num'] = int(item['min_num'])
    item['max_num'] = int(item['max_num'])
    char_ct = item['passstr'].count(item['charact'])
    if char_ct >= item['min_num'] and char_ct <= item['max_num']:
        tally += 1

print("{} passwords are valid".format(tally))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()
tally = 0

for item in checklist:
    pos1 = item['min_num']
    pos2 = item['max_num']
    char = item['charact']
    PW = item['passstr']
    if xor(PW[pos1-1]==char, PW[pos2-1]==char):
        tally += 1

print("{} passwords are valid".format(tally))
print("Runtime: {} seconds".format(time()-start))