from time import time
start = time()

with open("2015/inputs/day_1_input.txt") as f:
    directions = f.readline()[:-1]

#### PART 1

floor_num = directions.count('(') - directions.count(')')

print("\nSanta should go to floor {}".format(floor_num))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()
index = 0
floor = 0

while floor >= 0:
    if directions[index]=='(':
        floor += 1
    if directions[index]==')':
        floor -= 1
    index += 1

print("\nSanta enters the basement at position {}".format(index))
print("Runtime: {} seconds".format(time()-start))