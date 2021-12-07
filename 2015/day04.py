from hashlib import md5
from time import time
start = time()

secret_key = "ckczppom"

#### PART 1

pos_num = 1
found = False
while not(found):
    hash_input = (secret_key + str(pos_num)).encode()
    hash_result = md5(hash_input)
    if hash_result.hexdigest()[:5] == "00000":
        found = True
    else:
        pos_num += 1

print("\nThe lowest number to hash to 5 zeroes is {}".format(pos_num))
print("Runtime: {} seconds".format(time()-start))

# #### PART 2

start = time()

pos_num = 1
found = False
while not(found):
    hash_input = (secret_key + str(pos_num)).encode()
    hash_result = md5(hash_input)
    if hash_result.hexdigest()[:6] == "000000":
        found = True
    else:
        pos_num += 1

print("\nThe lowest number to hash to 6 zeroes is {}".format(pos_num))
print("Runtime: {} seconds".format(time()-start))