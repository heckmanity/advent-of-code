from time import time
start = time()

with open("2020/inputs/day_3_input.txt") as f:
    map_slice = f.readlines()
# remove newlines
map_slice = [row[:-1] for row in map_slice]

def count_trees(map_, path):
    count = 0
    width = len(map_[0])
    x = 0
    dx, dy = path
    for row in map_[::dy]:
        if row[x%width]=='#':
            count += 1
        x += dx
    return count

#### PART 1

tree_ct = count_trees(map_slice, (3,1))

print("\n{} trees will be encountered".format(tree_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_prod = 1
for rt in routes:
    tree_prod *= count_trees(map_slice, rt)

print("\n{} is the product of trees encountered".format(tree_prod))
print("Runtime: {} seconds".format(time()-start))