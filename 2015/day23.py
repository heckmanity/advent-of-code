from time import time
start = time()

with open("2015/inputs/day_23_input.txt") as f:
    raw_data = f.readlines()

program = []
for ln in raw_data:
    parts = ln[:-1].split(' ')
    if len(parts)==3:
        program.append({'cmd': parts[0],
                        'reg': parts[1][:-1], 
                        'amt': int(parts[2])})
    else:
        if parts[1]=='a' or parts[1]=='b':
            program.append({'cmd': parts[0],
                            'reg': parts[1]})
        else:
            program.append({'cmd': parts[0],
                            'amt': int(parts[1])})

def run_computer(prgm, initial):
    registers = initial
    pointer = 0

    while pointer < len(prgm):
        current = prgm[pointer]

        if current['cmd'] == 'inc':
            registers[current['reg']] += 1
        elif current['cmd'] == 'tpl':
            registers[current['reg']] *= 3
        elif current['cmd'] == 'hlf':
            registers[current['reg']] //= 2

        if any([current['cmd']=='jmp',
                current['cmd'] == 'jie' and registers[current['reg']] % 2 == 0,
                current['cmd'] == 'jio' and registers[current['reg']] == 1]):
            pointer += current['amt']
        else: 
            pointer += 1

    return registers

#### PART 1 ####

start_state = {'a': 0, 'b': 0}
end_state = run_computer(program, start_state)

print("\nThe value in register b when the program terminates is {}".format(end_state['b']))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

start_state = {'a': 1, 'b': 0}
end_state = run_computer(program, start_state)

print("\nThe value in register b when the program terminates is {}".format(end_state['b']))
print("Runtime: {} seconds".format(time()-start))