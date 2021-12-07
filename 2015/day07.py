from copy import deepcopy
from time import time
start = time()

with open("2015/inputs/day_7_input.txt") as f:
    data = f.readlines()
connections = [s[:-1].split(' ') + [False] for s in data]

#### PART 1 ####

wires = {'1': 1}

for cnt in connections:
    wires[cnt[-2]] = None

remaining_connections = deepcopy(connections)

while wires['a'] is None:
    for cnt in remaining_connections:
        if "AND" in cnt:
            w1, w2 = cnt[0:3:2]
            if wires[w1] is not None and wires[w2] is not None:
                wires[cnt[-2]] = wires[w1] & wires[w2]
                cnt[-1] = True
        elif "OR" in cnt:
            w1, w2 = cnt[0:3:2]
            if wires[w1] is not None and wires[w2] is not None:
                wires[cnt[-2]] = wires[w1] | wires[w2]
                cnt[-1] = True
        elif "RSHIFT" in cnt:
            w1 = cnt[0]
            if wires[w1] is not None:
                wires[cnt[-2]] = wires[w1] >> int(cnt[2])
                cnt[-1] = True
        elif "LSHIFT" in cnt:
            w1 = cnt[0]
            if wires[w1] is not None:
                wires[cnt[-2]] = wires[w1] << int(cnt[2])
                cnt[-1] = True
        elif "NOT" in cnt:
            w1 = cnt[1]
            if wires[w1] is not None:
                wires[cnt[-2]] = ~ wires[w1]
                cnt[-1] = True
        else:
            try:
                wires[cnt[-2]] = int(cnt[0])
                cnt[-1] = True
            except:
                w1 = cnt[0]
                if wires[w1] is not None:
                    wires[cnt[-2]] = wires[w1]
                    cnt[-1] = True

    remaining_connections = [Q for Q in remaining_connections if not Q[-1]]

wire_a_signal = wires['a']
            
print("\nSignal {} is provided to wire a".format(wire_a_signal))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

wires = {'1': 1}

for cnt in connections:
    wires[cnt[-2]] = None

wires['b'] = wire_a_signal

remaining_connections = deepcopy(connections)
remaining_connections = [Q for Q in remaining_connections if not(Q[-2]=='b')]

while wires['a'] is None:
    for cnt in remaining_connections:
        if "AND" in cnt:
            w1, w2 = cnt[0:3:2]
            if wires[w1] is not None and wires[w2] is not None:
                wires[cnt[-2]] = wires[w1] & wires[w2]
                cnt[-1] = True
        elif "OR" in cnt:
            w1, w2 = cnt[0:3:2]
            if wires[w1] is not None and wires[w2] is not None:
                wires[cnt[-2]] = wires[w1] | wires[w2]
                cnt[-1] = True
        elif "RSHIFT" in cnt:
            w1 = cnt[0]
            if wires[w1] is not None:
                wires[cnt[-2]] = wires[w1] >> int(cnt[2])
                cnt[-1] = True
        elif "LSHIFT" in cnt:
            w1 = cnt[0]
            if wires[w1] is not None:
                wires[cnt[-2]] = wires[w1] << int(cnt[2])
                cnt[-1] = True
        elif "NOT" in cnt:
            w1 = cnt[1]
            if wires[w1] is not None:
                wires[cnt[-2]] = ~ wires[w1]
                cnt[-1] = True
        else:
            try:
                wires[cnt[-2]] = int(cnt[0])
                cnt[-1] = True
            except:
                w1 = cnt[0]
                if wires[w1] is not None:
                    wires[cnt[-2]] = wires[w1]
                    cnt[-1] = True

    remaining_connections = [Q for Q in remaining_connections if not Q[-1]]

print("\nSignal {} is provided to wire a (with b overridden)".format(wires['a']))
print("Runtime: {} seconds".format(time()-start))