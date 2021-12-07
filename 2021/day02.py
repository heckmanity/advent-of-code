from time import time
start = time()

with open("2021/inputs/day_2_input.txt") as f:
    instructions = [ln.strip('\n').split(' ') for ln in f.readlines()]

#### PART 1

pos = 0
dep = 0

for dir, val in instructions:
    if dir=="forward":
        pos += int(val)
    elif dir=="down":
        dep += int(val)
    else: 
        dep -= int(val)

print("{} is the product of the final position and depth".format(pos*dep))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

pos = 0
dep = 0
aim = 0

for dir, val in instructions:
    if dir=="forward":
        X = int(val)
        pos += X
        dep += aim * X
    elif dir=="down":
        aim += int(val)
    else: 
        aim -= int(val)

print("{} is the product of the final position and depth".format(pos*dep))
print("Runtime: {} seconds".format(time()-start))