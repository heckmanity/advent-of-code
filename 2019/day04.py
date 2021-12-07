import re
from time import time
start = time()

MIN_PW = 246540
MAX_PW = 787419

dbl_test = re.compile(r"""(\d)\1+""")
inc_test = re.compile(r"""^1*2*3*4*5*6*7*8*9*$""")

#### PART 1

def is_increasing(N):
    for i in range(len(N)-1):
        if int(N[i+1]) - int(N[i]) < 0:
            return False
    return True

valid_ct = 0
valid_space = []
for pw in range(MIN_PW, MAX_PW + 1):
    pw_str = str(pw)
    if re.search(dbl_test, pw_str) and is_increasing(pw_str):
        valid_ct += 1
        valid_space.append(pw)

print("\n{} passwords meet the criteria".format(valid_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

new_dbl_test = re.compile(r"""(.)(?!\1)(\d)\2(?!\2)""")

valid_ct = 0
for pw in valid_space:
    pw_str = '-' + str(pw)
    if re.search(new_dbl_test, pw_str):
        valid_ct += 1

print("\n{} passwords meet the new criteria".format(valid_ct))
print("Runtime: {} seconds".format(time()-start))