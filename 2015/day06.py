import re
from time import time
start = time()

with open("2015/inputs/day_6_input.txt") as f:
    data = f.readlines()
instructions = [s[:-1] for s in data]

#### PART 1 ####

cmd_match = re.compile(r"""^(?P<what>[\w\s]*) (?P<x1>\d*),(?P<y1>\d*) through (?P<x2>\d*),(?P<y2>\d*)""")

lights = [[False] * 1000 for i in range(1000)]

for cmd in instructions:
    cmd = re.match(cmd_match, cmd).groupdict()
    for x in range(int(cmd['x1']), int(cmd['x2'])+1):
        for y in range(int(cmd['y1']), int(cmd['y2'])+1):
            if cmd['what']=='turn on':
                lights[x][y] = True
            if cmd['what']=='turn off':
                lights[x][y] = False
            if cmd['what']=='toggle':
                lights[x][y] = not(lights[x][y])

on_count = 0
for row in lights:
    on_count += row.count(True)

print("\n{} lights are lit".format(on_count))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

cmd_match = re.compile(r"""^(?P<what>[\w\s]*) (?P<x1>\d*),(?P<y1>\d*) through (?P<x2>\d*),(?P<y2>\d*)""")

lights = [[0] * 1000 for i in range(1000)]

for cmd in instructions:
    cmd = re.match(cmd_match, cmd).groupdict()
    for x in range(int(cmd['x1']), int(cmd['x2'])+1):
        for y in range(int(cmd['y1']), int(cmd['y2'])+1):
            if cmd['what']=='turn on':
                lights[x][y] += 1
            if cmd['what']=='turn off':
                if lights[x][y] > 0:
                    lights[x][y] -= 1
            if cmd['what']=='toggle':
                lights[x][y] += 2

brightness = 0
for row in lights:
    brightness += sum(row)

print("\nThe total brightness is {}".format(brightness))
print("Runtime: {} seconds".format(time()-start))