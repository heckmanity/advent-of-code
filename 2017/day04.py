from time import time
from string import ascii_lowercase
start = time()

with open("2017/inputs/day_04_input.txt") as f:
    phrases = [ln.strip().split(' ') for ln in f.readlines()]

#### PART 1

valid_count = 0

for phrase in phrases:
    valid = True
    for word in phrase:
        if phrase.count(word) > 1:
            valid = False
    if valid:
        valid_count += 1

print("\nThere are {} valid passphrases".format(valid_count))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

valid_count = 0

def anagram_base(wrd):
    encoding = []
    for ltr in ascii_lowercase:
        encoding.append(wrd.count(ltr))
    return encoding

for phrase in phrases:
    valid = True
    phrase_encoded = [anagram_base(w) for w in phrase]
    for word in phrase_encoded:
        if phrase_encoded.count(word) > 1:
            valid = False
    if valid:
        valid_count += 1

print("\nThere are {} valid passphrases under the new policy".format(valid_count))
print("Runtime: {} seconds".format(time()-start))