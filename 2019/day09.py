from intcode.Intcode import Intcode
from time import time
from copy import deepcopy
start = time()

with open("2019/inputs/day_9_input.txt") as f:
    program = f.readline()[:-1]
program = program.split(',')
program = [int(i) for i in program]

#### PART 1

computer = Intcode(program)
computer.reset()
computer.run(1)
keycode = computer.outputs.pop()

print("\nThe BOOST keycode produced is {}".format(keycode))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

computer.reset()
computer.run(2)
coords = computer.outputs.pop()

print("\nThe coordinates of the distress signal are {}".format(coords))
print("Runtime: {} seconds".format(time()-start))