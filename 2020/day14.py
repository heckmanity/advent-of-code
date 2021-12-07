from time import time
start = time()

with open("2020/inputs/day_14_input.txt") as f:
    program = f.readlines()

memory = dict()

#### PART 1 ####

current_mask = None
for instr in program:
    if instr[:3]=='mas':
        current_mask = instr.split(' ')[2][:-1]
    if instr[:3]=='mem':
        address, eq, write_val = instr.split(' ')
        address = int(address[4:-1])
        write_val = int(write_val)

        og_string = format(write_val, '036b')
        new_string = ''
        for i in range(len(current_mask)):
            next_char = og_string[i] if current_mask[i]=='X' else current_mask[i]
            new_string += next_char
        write_val = int(new_string, 2)
        
        memory[address] = write_val

print("\nThe sum of all values in memory is {}".format(sum(memory.values())))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()
memory = dict()

current_mask = None
for instr in program:
    if instr[:3]=='mas':
        current_mask = instr.split(' ')[2][:-1]
    if instr[:3]=='mem':
        address, eq, write_val = instr.split(' ')
        address = int(address[4:-1])
        write_val = int(write_val)

        og_address = format(address, '036b')
        new_string = ''
        for i in range(len(current_mask)):
            if current_mask[i]=='0':
                next_char = og_address[i]
            else:
                next_char = current_mask[i]
            new_string += next_char
        
        for j in range(2**new_string.count('X')):
            newer_string = ''
            replacements = format(j, '00'+str(new_string.count('X'))+'b')
            rpl_ind = 0
            for k in range(len(new_string)):
                if new_string[k]=='X':
                    newer_string += replacements[rpl_ind]
                    rpl_ind += 1
                else:
                    newer_string += new_string[k]
            
            new_address = int(newer_string, 2)        
            memory[new_address] = write_val

print("\nThe sum of all values in memory v2 is {}".format(sum(memory.values())))
print("Runtime: {} seconds".format(time()-start))