import re
from copy import deepcopy
from time import time
start = time()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("2018/inputs/day_7_input.txt") as f:
    raw_data = f.readlines()

parser = re.compile(r"""Step (?P<prereq>\w) must be finished before step (?P<rule>\w) can begin""")

prereqs = {ltr:[] for ltr in alphabet}
for line in raw_data:
    details = re.match(parser, line).groupdict()
    prereqs[details['rule']].append(details['prereq'])

prereqs_reset = deepcopy(prereqs)

#### PART 1 ####

order = ''

while len(prereqs) > 0:
    ready = []
    for ltr in prereqs.keys():
        if len(prereqs[ltr])==0:
            ready.append(ltr)

    ready = sorted(ready)
    next_step = ready.pop(0)
    order += next_step
    prereqs.pop(next_step)

    for ltr in prereqs.keys():
        if next_step in prereqs[ltr]:
            prereqs[ltr].pop(prereqs[ltr].index(next_step))

print("\nThe steps should be completed in this order: {}".format(order))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

num_workers = 5
prereqs = deepcopy(prereqs_reset)
times = {alphabet[i]: i+61 for i in range(len(alphabet))}
done = ''

tick = -1
workers = [{'step': None, 'timeout': None} for w in range(num_workers)]
steps_avail = []

while not(len(done)==len(order)):
    tick += 1

    for wkr in workers:
        if wkr['timeout']:
            wkr['timeout'] -= 1
            if wkr['timeout']==0:
                done += wkr['step']

                for ltr in prereqs.keys():
                    if wkr['step'] in prereqs[ltr]:
                        prereqs[ltr].pop(prereqs[ltr].index(wkr['step']))

                wkr['step'] = None
                wkr['timeout'] = None

    for ltr in prereqs.keys():
        if len(prereqs[ltr])==0:
            steps_avail.append(ltr)

    steps_avail = sorted(steps_avail)
    for ltr in steps_avail:
        if ltr in prereqs.keys():
            prereqs.pop(ltr)

    for wkr in workers:
        if not(wkr['timeout']) and len(steps_avail) > 0:
            wkr['step'] = steps_avail.pop(0)
            wkr['timeout'] = times[wkr['step']]
    
    # print(tick, workers[0], workers[1])

print("\nWith {} workers the project will take {} seconds in the order {}".format(num_workers, tick, done))
print("Runtime: {} seconds".format(time()-start))