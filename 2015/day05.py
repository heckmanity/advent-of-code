import re
from time import time
start = time()

with open("2015/inputs/day_5_input.txt") as f:
    data = f.readlines()
NNList = [s[:-1] for s in data]

#### PART 1

vowel_test = re.compile(r"""^.*[aeiou].*[aeiou].*[aeiou].*$""")
dbl_ltr_test = re.compile(r"""^.*(\w)(\1).*$""")
naughty_test = re.compile(r"""(ab)|(cd)|(pq)|(xy)""")

nice_ct = 0
for string in NNList:
    if not(re.search(naughty_test, string)):
        if re.match(vowel_test, string) and re.match(dbl_ltr_test, string):
            nice_ct += 1

print("\nThere are {} nice strings".format(nice_ct))
print("Runtime: {} seconds".format(time()-start))

# #### PART 2

start = time()

dbl_duo_test = re.compile(r"""^.*(\w\w).*(\1).*$""")
rondo_test = re.compile(r"""^.*(\w)\w(\1).*$""")

nice_ct = 0
for string in NNList:
    if re.match(dbl_duo_test, string) and re.match(rondo_test, string):
        nice_ct += 1

print("\nThere are {} nice strings under the new ruleset".format(nice_ct))
print("Runtime: {} seconds".format(time()-start))