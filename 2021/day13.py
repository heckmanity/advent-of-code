from time import time
start = time()

with open("2021/inputs/day_13_input.txt") as f:
    dots = []
    instructions = []
    for ln in f.readlines():
        if ln == '\n':
            continue
        elif ',' in ln:
            dots.append([int(i) for i in ln.strip().split(',')])
        else:
            eq_loc = ln.index('=')
            instr = [ ln[eq_loc - 1], int(ln.strip()[eq_loc + 1:]) ]
            instructions.append(instr)

def reflect_point(pt, axis, location):
    x, y = pt if axis=='y' else list(reversed(pt))
    if y > location:
        y = 2 * location - y
    return (x, y) if axis=='y' else (y, x)  

#### PART 1

ax, val = instructions[0]
folded = [reflect_point(dt, ax, val) for dt in dots]
folded = list(set(folded))

print(f"\nThere are {len(folded)} dots visible after completing the first fold instruction")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

for instr in instructions[1:]:
    ax, val = instr
    folded = [reflect_point(dt, ax, val) for dt in folded]
    folded = list(set(folded))

x_max, y_max = [max(folded, key=lambda p: p[i])[i] for i in range(2)]
img = [ [' ' for i in range(x_max+1) ] for j in range(y_max+1) ]
for x, y in folded:
    img[y][x] = '█'

print("\nThe activation code is:")
for ln in img:
    print(''.join(ln))
print(f"\nRuntime: {time()-start} seconds")
