from copy import deepcopy
from time import time
start = time()

with open("2020/inputs/day_8_input.txt") as f:
    instructions = f.readlines()
instructions = [j[:-1].split(" ") + [False] for j in instructions]

def run_code(inst_set):
    working_copy = deepcopy(inst_set)

    pointer = 0
    accumulator = 0
    working = True

    while working:
        try:
            operation, argument, visited = working_copy[pointer]
        except:
            break

        if visited:
            working = False
            continue
        working_copy[pointer][2] = True
        if operation == "nop":
            pointer += 1
        if operation == "acc":
            accumulator += int(argument)
            pointer += 1
        if operation == "jmp":
            pointer += int(argument)
    
    return (accumulator, working)

#### PART 1
  
pre_loop_val = run_code(instructions)[0]

print("\nBefore looping the value in the accumulator is {}".format(pre_loop_val))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

for index in range(len(instructions)):
    # print(index)
    operation = instructions[index][0]
    if operation == "acc":
        continue
    repaired = deepcopy(instructions)
    if operation == "nop":
        repaired[index][0] = "jmp"
    elif operation == "jmp":
        repaired[index][0] = "nop"

    accumulator, finished = run_code(repaired)
    if finished:
        break

print("\nThe repaired program terminates with accumulator set to {}".format(accumulator))
print("Runtime: {} seconds".format(time()-start))