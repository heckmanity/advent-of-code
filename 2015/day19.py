import re
from alive_progress import alive_bar
from time import time
start = time()

with open("2015/inputs/day_19_input.txt") as f:
    raw_data = f.readlines()

parser = re.compile(r"""(?P<atom>\w*) => (?P<new>\w*)""")

replacements = dict()
rev_replace = dict()

read_molecule = False
for dataline in raw_data:
    if read_molecule:
        molecule = dataline[:-1]
        break
    else:
        line_read = re.match(parser, dataline)
        if line_read:
            info = line_read.groupdict()
            if not(info['atom'] in replacements.keys()):
                replacements[info['atom']] = []
            replacements[info['atom']].append(info['new'])
            rev_replace[info['new']] = [info['atom']]
        else:
            read_molecule = True

#### PART 1 ####

def get_products(reactant, rules):
    atom_list = rules.keys()
    synthesized = set()
    min_atom_len = min([len(Q) for Q in atom_list])
    max_atom_len = max([len(Q) for Q in atom_list])
    react_len = len(reactant)

    for i in range(react_len):
        for atom_len in range(min_atom_len, max_atom_len+1):
            if i + atom_len <= react_len:
                atom = reactant[i:i+atom_len]
                if atom in atom_list:
                    for rpl in rules[atom]:
                        new = reactant[:i] + rpl + reactant[i+atom_len:]
                        if not('e' in new and len(new)>1):
                            synthesized.add(reactant[:i] + rpl + reactant[i+atom_len:])
    
    return synthesized

molecule_ct = len(get_products(molecule, replacements))

print("\n{} distinct molecules can be created with one replacement".format(molecule_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

get_priors = get_products

def search_next_tier(prev_tier, desired, lvl=0):
    if not(type(prev_tier)==list):
        prev_tier = [prev_tier]
    # print("Level = {}; Checking {} reactants".format(lvl, len(prev_tier)))    

    if len(prev_tier)==0:
        return None
    
    next_tier = []
    for reactant in prev_tier:
        next_tier = next_tier + list(get_priors(reactant, rev_replace))
        if desired in next_tier:
            return lvl+1
    
    next_tier = list(set(next_tier))
    # edge_len = len(desired)
    # outputs = [Q for Q in list(next_tier) if len(Q)>edge_len]

    # this is the greedy solution; not guaranteed (except by possible structure in ruleset?)
    output_ind = min([i for i in range(len(next_tier))], key=lambda i: len(next_tier[i]))
    return search_next_tier(next_tier[output_ind], desired, lvl=lvl+1)

min_steps = search_next_tier(molecule, "e")

print("\nThe molecule can be fabricated in a minimum of {} steps".format(min_steps))
print("Runtime: {} seconds".format(time()-start))

# min_steps_lookup = dict()
# min_atom_len = min([len(Q) for Q in rev_replace.keys()])
# max_atom_len = max([len(Q) for Q in rev_replace.keys()])

# job_size = 0
# for i in range(len(molecule)):
#     for atom_len in range(min_atom_len, max_atom_len+1):
#         if i + atom_len <= len(molecule):
#             atom = molecule[i:i+atom_len]
#             if atom in rev_replace.keys():
#                 job_size += 1

# def synthesize(reactant, step=0):
#     # print(len(reactant), step)
#     if step==1:
#         bar()
    
#     if reactant in min_steps_lookup.keys():
#         return min_steps_lookup[reactant]
#     if reactant=='e':
#         return step
    
#     product_steps = []
#     for i in range(len(reactant)):
#         for atom_len in range(1, max_atom_len+1):
#             if i + atom_len <= len(reactant):
#                 atom = reactant[i:i+atom_len]
#                 if atom in rev_replace.keys():
#                     rpl = rev_replace[atom]
#                     next_reactant = reactant[:i] + rpl + reactant[i+atom_len:]
#                     product_steps.append(synthesize(next_reactant, step=step+1))
        
#     product_steps = [Q for Q in product_steps if Q is not None]
#     min_steps_lookup[reactant] = min(product_steps) if len(product_steps)>0 else None
#     return min_steps_lookup[reactant]