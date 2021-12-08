from time import time
import re
start = time()

parser = re.compile(r"""(?P<name>[a-z]+) \((?P<weight>[0-9]+)\)( -> )*(?P<supers>.*)""")

with open("2017/inputs/day_07_input.txt") as f:
    programs = [parser.search(p).groupdict() for p in f.readlines()]
for prog in programs:
    prog['weight'] = int(prog['weight'])
    prog['supers'] = None if prog['supers']=='' else prog['supers'].split(', ')

#### PART 1

def get_bottom(nodes):
    all_names, all_supers = set(), set()

    for node in nodes:
        all_names.add(node['name'])
        if node['supers']:
            for spr in node['supers']:
                all_supers.add(spr)

    return list(all_names - all_supers)[0]

bottom = get_bottom(programs)

print("\nThe name of the bottom program is {}".format(bottom))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

program_lookup = { prog['name']: { 'weight': prog['weight'], 'supers': prog['supers'] } \
                        for prog in programs }
    
def get_weight(program):
    if not program_lookup[program]['supers']:
        return program_lookup[program]['weight']
    return program_lookup[program]['weight'] \
            + sum([get_weight(spr) for spr in program_lookup[program]['supers']])

unbalanced_programs = []
for prog in program_lookup.keys():
    if not program_lookup[prog]['supers']:
        continue
    weights = [get_weight(spr) for spr in program_lookup[prog]['supers']]
    if not all([weights.count(weights[i])==len(weights) for i in range(len(weights))]):
        unbalanced_programs.append(prog)

current = bottom
while any([spr in unbalanced_programs for spr in program_lookup[current]['supers']]):
    for spr in program_lookup[current]['supers']:
        if spr in unbalanced_programs:
            current = spr
            break

mismatched = [ get_weight(spr) for spr in program_lookup[current]['supers'] ]
counts = [ mismatched.count(mismatched[i]) for i in range(len(mismatched)) ]
problem_index = counts.index(1)
problem_program = program_lookup[current]['supers'][problem_index]

diff = mismatched[(problem_index + 1) % len(mismatched)] - mismatched[problem_index]
correct_weight = program_lookup[problem_program]['weight'] + diff

print("\nThe weight of {} needs to be {} to balance the tower".format(problem_program, correct_weight))
print("Runtime: {} seconds".format(time()-start))