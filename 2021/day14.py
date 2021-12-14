from time import time
from itertools import product
from copy import deepcopy
from alive_progress import alive_bar
start = time()

with open("2021/inputs/day_14_input.txt") as f:
    insertions, divisions = {}, {}
    p_table = set()
    for ln in f.readlines():
        if '-' in ln:
            pair, elem = ln.strip().split(' -> ')
            insertions[pair] = pair[:1] + elem + pair[1:]
            divisions[pair] = [pair[0] + elem, elem + pair[1]]
            p_table = p_table.union(set([pair[0], pair[1], elem]))
        elif ln == '\n':
            continue
        else:
            polymer = ln.strip()
    pairs = insertions.keys()
    p_table = list(p_table)

def quantity_diff(poly, stps):
    print('\n')
    with alive_bar(stps) as bar:
        for stp in range(stps):
            next_step = poly
            insertion_ct = 0

            for i in range(len(poly)-1):
                current_pair = poly[i:i+2]
                if current_pair in pairs:
                    next_step = next_step[:i+insertion_ct] + insertions[current_pair] \
                                                            + next_step[i+insertion_ct+2:]
                    insertion_ct += 1

            poly = next_step
            bar()

    counts = {}
    for c in poly:
        if not c in counts.keys():
            counts[c] = poly.count(c)

    elements_by_freq = sorted(list(counts.keys()), key=lambda e: counts[e], reverse=True)

    return counts[elements_by_freq[0]] - counts[elements_by_freq[-1]]

def fast_quantity_diff(poly, stps):
    bigrams = { ''.join(pr):0 for pr in product(p_table, repeat=2) }
    element_freq = { e:0 for e in p_table }

    for c in poly:
        element_freq[c] += 1
    for i in range(len(poly)-1):
        bigrams[poly[i:i+2]] += 1

    print('\n')
    with alive_bar(stps) as bar:
        for stp in range(stps):
            next_bigrams = deepcopy(bigrams)
            next_elem_freq = deepcopy(element_freq)

            for bg in bigrams.keys():
                if bg in pairs:
                    num_bg = bigrams[bg]
                    next_bigrams[bg] -= num_bg
                    for child in divisions[bg]:
                        next_bigrams[child] += num_bg
                    next_elem_freq[insertions[bg][1]] += num_bg
            
            bigrams = next_bigrams
            element_freq = next_elem_freq
            bar()

    freq_count = sorted(list(element_freq.keys()), key=lambda e: element_freq[e], reverse=True)

    return element_freq[freq_count[0]] - element_freq[freq_count[-1]]

#### PART 1

NUM_STEPS = 10
diff = quantity_diff(polymer, NUM_STEPS)

print(f"\nThe quantity difference between most and least common elements is {diff}")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

NUM_STEPS = 40
diff = fast_quantity_diff(polymer, NUM_STEPS)

print(f"\nThe quantity difference between most and least common elements is {diff}")
print(f"Runtime: {time()-start} seconds")
