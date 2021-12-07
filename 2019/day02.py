from intcode.Intcode import Intcode
from time import time
from copy import deepcopy
start = time()

with open("2019/inputs/day_2_input.txt") as f:
    memory = f.readline()[:-1]
memory = memory.split(',')
memory = [int(i) for i in memory]

#### PART 1

memory[1:3] = [12, 2]
computer = Intcode(memory)

computer.run()
pos_0 = computer.memory[0]

print("\nValue at position 0 is {}".format(pos_0))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()
desired_output = 19690720

done = False
for noun in range(1,100):
    for verb in range(1,100):
        computer.reset()
        computer.memory[1:3] = [noun, verb]
        computer.run()
        if computer.memory[0]==desired_output:
            done = True
            break
    if done:
        break

print("\nThe required input is {}".format(100 * noun + verb))
print("Runtime: {} seconds".format(time()-start))

# def op_code_1(tape, regA, regB, output):
#     A = tape[regA]
#     B = tape[regB]
#     tape[output] = A + B
#     return tape

# def op_code_2(tape, regA, regB, output):
#     A = tape[regA]
#     B = tape[regB]
#     tape[output] = A * B
#     return tape

# program_reset = deepcopy(memory)
# def program(inputA, inputB):
#     memory = deepcopy(program_reset)
#     memory[1:3] = [inputA, inputB]

#     pointer = 0
#     current_instruction = memory[pointer]
#     while not(current_instruction==99):
#         if current_instruction==1:
#             memory = op_code_1(memory, *memory[pointer+1:pointer+4])
#         if current_instruction==2:
#             memory = op_code_2(memory, *memory[pointer+1:pointer+4])
#         pointer += 4
#         current_instruction = memory[pointer]
    
#     return memory[0]