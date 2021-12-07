from time import time
start = time()

with open("2019/inputs/day_6_input.txt") as f:
    raw_data = f.readlines()
map_data = [line[:-1].split(')') for line in raw_data]

orbit_map = dict()
for line in map_data:
    parent, child = line
    orbit_map[child] = parent

#### PART 1

orbit_ct = 0

def get_COM_path(body, chart):
    path = []
    while chart[body] in chart.keys():
        body = chart[body]
        path.append(body)
    return path

for body in orbit_map.keys():
    orbit_chain = get_COM_path(body, orbit_map)
    orbit_ct += len(orbit_chain) + 1

print("\nTotal number of orbits is {}".format(orbit_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

Santa_path = set(get_COM_path("SAN", orbit_map))
my_path = set(get_COM_path("YOU", orbit_map))

stops = set.union(Santa_path.difference(my_path), my_path.difference(Santa_path))

print("\n{} orbital transfers are required".format(len(stops)))
print("Runtime: {} seconds".format(time()-start))