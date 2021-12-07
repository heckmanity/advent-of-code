from time import time
start = time()

with open("2017/inputs/day_05_input.txt") as f:
    instructions = [int(ln.strip()) for ln in f.readlines()]

#### PART 1

step_count = 0
pointer = 0

while pointer < len(instructions):
    instructions[pointer] += 1
    pointer += instructions[pointer] - 1
    step_count += 1

print("\nIt takes {} steps to reach the exit".format(step_count))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

with open("2017/inputs/day_05_input.txt") as f:
    instructions = [int(ln.strip()) for ln in f.readlines()]

step_count = 0
pointer = 0

while pointer < len(instructions):
    jump = instructions[pointer]
    instructions[pointer] += 1 if instructions[pointer] < 3 else -1
    pointer += jump
    step_count += 1

print("\nIt now takes {} steps to reach the exit".format(step_count))
print("Runtime: {} seconds".format(time()-start))