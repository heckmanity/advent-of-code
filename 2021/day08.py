from time import time
start = time()

with open("2021/inputs/day_8_input.txt") as f:
    log = [ln.strip().split(' | ') for ln in f.readlines()]
log = [ [ [''.join(sorted(s)) for s in entry.split(' ')]   \
                                for entry in note ]        \
                                for note in log ]

for entry in log:
    entry[0] = sorted( entry[0], key=lambda l: len(l) )

#### PART 1

tally = 0

for signal, output in log:
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            tally += 1

print("\nThe digits 1, 4, 7, or 8 appear {} times in the output values".format(tally))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

running_sum = 0

for signal, output in log:
    defns = { k:None for k in range(10) }
    for digit in [1, 7, 4, 8]:
        defns[digit] = signal.pop(-1) if digit==8 else signal.pop(0)

    for segment in defns[1]:
        if all([d.count(segment)==1 for d in signal[3:]]):
            bottom_right = segment
        else:
            top_right = segment
    
    for pattern in signal:
        if not(top_right in pattern):
            defns[len(pattern)] = pattern # taking advantage of a weird coincidence here
        elif not(bottom_right in pattern):
            defns[2] = pattern
        elif len(pattern)==5 and top_right in pattern and bottom_right in pattern:
            defns[3] = pattern
        else:
            # weird math but it's just len of 2 maps to index 9, and 3 to 0
            defns[(len(set(pattern) - set(defns[4])) + 7) % 10] = pattern 
    
    encodings = { v:str(k) for k,v in defns.items() }
    value = ''
    for digit_pattern in output:
        value += encodings[digit_pattern]

    running_sum += int(value)        

print("The sum of all output values is {}".format(running_sum))
print("Runtime: {} seconds\n".format(time()-start))