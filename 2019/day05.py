from intcode.Intcode import Intcode
from time import time
start = time()

with open("2019/inputs/day_5_input.txt") as f:
    program = f.readline()[:-1]
program = program.split(',')
program = [int(i) for i in program]

#### PART 1

computer = Intcode(program)
computer.run(1)

diag_code_1 = computer.outputs.pop()

print("\nDiagnostic code is {}".format(diag_code_1))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

computer.reset()
computer.run(5)

diag_code_5 = computer.outputs.pop()

print("\nDiagnostic code is {}".format(diag_code_5))
print("Runtime: {} seconds".format(time()-start))