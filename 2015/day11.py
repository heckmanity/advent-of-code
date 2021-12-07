import re
from time import time
start = time()

day_11_input = "vzbxkghb"
alphabet = "abcdefghjkmnpqrstuvwxyz"

def increment(pw):
    if len(pw)==1:
        return alphabet[(alphabet.index(pw)+1) % len(alphabet)]
    
    ind = -1
    pw = pw[:ind] + increment(pw[ind])
    while pw[ind]=='a':
        ind -= 1
        pw = pw[:ind] + increment(pw[ind]) + pw[ind+1:]
    return pw

def has_3_increasing(pw):
    alpha_part_1 = "abcdefgh"
    alpha_part_2 = "pqrstuvwxyz"
    for AB in [alpha_part_1, alpha_part_2]:
        for i in range(len(AB) - 2):
            if AB[i:i+3] in pw:
                return True
    return False

# iol_test = re.compile(r"""[iol]""")
dbl_test = re.compile(r"""^.*(\w)(\1).*(\w)(\3).*$""")

#### PART 1 ####

start_at = "vzbxxaaa" # only way to make room for requirements
                      # anything before this can't work

pw_found = False
new_pw = start_at # day_11_input
while not(pw_found):
    new_pw = increment(new_pw)
    if has_3_increasing(new_pw) and re.match(dbl_test, new_pw):
        pw_found = True

print("\nSanta's new password should be {}".format(new_pw))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

pw_found = False
while not(pw_found):
    new_pw = increment(new_pw)
    if has_3_increasing(new_pw) and re.match(dbl_test, new_pw):
        pw_found = True

print("\nSanta's next new password should be {}".format(new_pw))
print("Runtime: {} seconds".format(time()-start))