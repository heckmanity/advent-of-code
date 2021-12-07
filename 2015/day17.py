from alive_progress import alive_bar
from time import time
start = time()

with open("2015/inputs/day_17_input.txt") as f:
    data = f.readlines()
containers = [int(Q[:-1]) for Q in data]
container_ct = len(containers)

eggnog_amt = 150

#### PART 1 ####

combo_ct = 0
combos = []

print("\n")
with alive_bar(2**container_ct) as bar:
    for combo in range(2**container_ct):
        pattern = format(combo, format(container_ct, "03")+"b")
        capacity = 0
        for i in range(container_ct):
            capacity += int(pattern[i]) * containers[i]
        if capacity==eggnog_amt:
            combo_ct += 1
            combos.append(pattern)
        bar()

print("\n{} different container combinations can fit {}L of eggnog".format(combo_ct, eggnog_amt))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

cont_per_pattern = [Q.count('1') for Q in combos]
combo_ct = cont_per_pattern.count(min(cont_per_pattern))

print("\n{} of those combinations fit {}L in the fewest containers".format(combo_ct, eggnog_amt))
print("Runtime: {} seconds".format(time()-start))