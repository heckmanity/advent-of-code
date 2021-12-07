from intcode.Intcode import Intcode
from itertools import permutations
from time import time
start = time()

with open("2019/inputs/day_7_input.txt") as f:
    program = f.readline()[:-1]
program = program.split(',')
program = [int(i) for i in program]

computer = Intcode(program)

#### PART 1

best_signal = 0
for perm in permutations([0,1,2,3,4]):
    signal = 0
    for phase in perm:
        computer.reset()
        computer.run(phase, signal)
        signal = computer.outputs.pop()
    if signal > best_signal:
        best_signal = signal

print("\nThe highest signal that can be sent is {}".format(best_signal))
print("Runtime: {} seconds".format(time()-start))
del computer

#### PART 2

start = time()

amps = [Intcode(program) for i in range(5)]
best_signal = 0
for perm in permutations([5,6,7,8,9]):
    for A in amps:
        A.reset()
    working_amp = 0
    signal = 0
    
    finished = False
    while not(finished):
        amp_index = working_amp % 5
        if working_amp < 5:
            phase = perm[amp_index]
            amps[amp_index].run(phase, signal, outpause=True)
        else:
            amps[amp_index].run(signal, outpause=True)

        finished = any([A.halted for A in amps])
        if not(finished):
            signal = amps[amp_index].outputs.pop()
            working_amp += 1

    if signal > best_signal:
        best_signal = signal

print("\nThe highest signal that can be sent is {}".format(best_signal))
print("Runtime: {} seconds".format(time()-start))