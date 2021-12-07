from time import time
start = time()

with open("2015/inputs/day_3_input.txt") as f:
    directions = f.readline()[:-1]

#### PART 1

current_pos = [0, 0]
moves = { '^': [0,  1],
          'v': [0, -1],
          '>': [ 1, 0],
          '<': [-1, 0]  }
visits = [current_pos]

for cmd in directions:
    new_x = current_pos[0] + moves[cmd][0]
    new_y = current_pos[1] + moves[cmd][1]
    current_pos = [new_x, new_y]
    visits.append(current_pos)

house_ct = 1
for i in range(1, len(visits)):
    if visits[i] not in visits[:i]:
        house_ct += 1

print("\n{} houses are visited by Santa".format(house_ct))
print("Runtime: {} seconds".format(time()-start))

# #### PART 2

start = time()

visits = [[0,0]]
for route in [directions[0::2], directions[1::2]]:
    current_pos = [0, 0]

    for cmd in route:
        new_x = current_pos[0] + moves[cmd][0]
        new_y = current_pos[1] + moves[cmd][1]
        current_pos = [new_x, new_y]
        visits.append(current_pos)

house_ct = 1
for i in range(1, len(visits)):
    if visits[i] not in visits[:i]:
        house_ct += 1

print("\n{} houses are visited between Santa and Robo-Santa".format(house_ct))
print("Runtime: {} seconds".format(time()-start))