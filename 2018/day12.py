import re
from alive_progress import alive_bar
from time import time
start = time()

with open("2018/inputs/day_12_input.txt") as f:
    raw_data = f.readlines()

parse_init_state = re.compile(r"""^initial state: ([#.]*)\n$""")
parse_ruleset = re.compile(r"""^([#.]*) => ([#.])\n$""")

def encode(hashstr):
    num_char = len(hashstr)
    code = 0
    for char_ind in range(num_char):
        num_char -= 1
        if hashstr[char_ind]=='#':
            code += 2**num_char
    return code

ruleset = dict()
for line in raw_data:
    if line=='\n':
        continue
    rule = re.match(parse_ruleset, line)
    if rule:
        ruleset[encode(rule.group(1))] = rule.group(2)
    else:
        gen_zero = re.match(parse_init_state, line).group(1)

for i in range(32):
    if not(i in ruleset.keys()):
        ruleset[i] = '.'

#### PART 1 ####

num_generations = 20
rule_length = 5

padding = '.' * (num_generations + rule_length)
plants = padding + gen_zero + padding

print("\nSpawning generations...")
with alive_bar(num_generations) as bar:
    for gen in range(1, num_generations + 1):
        next_gen = '..'
        for plant_index in range(len(plants)-rule_length+1):
            next_gen += ruleset[encode(plants[plant_index:plant_index+5])]
        next_gen += '..'
        plants = next_gen
        bar()

plant_sum = 0
offset = len(padding)
for i in range(len(plants)):
    plant_num = i - offset
    if plants[i]=='#':
        plant_sum += plant_num

print("\nThe sum of all plant numbers is {}".format(plant_sum))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

# start = time()

# real_time = secs_passed

# print("\nThe elves would've need to wait {} seconds for the message to appear".format(real_time))
# print("Runtime: {} seconds".format(time()-start))