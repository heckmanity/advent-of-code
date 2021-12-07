from time import time
start = time()

with open("2018/inputs/day_8_input.txt") as f:
    license_file = [int(Q) for Q in f.readline()[:-1].split(" ")]

#### PART 1 ####

def get_metadata_sum(node, children_ct=1, meta_ct=0):
    if children_ct==0:
        return sum(node[:meta_ct]), node[meta_ct:]

    child_sums = []
    for child in range(children_ct):
        header = node[:2]
        remainder = node[2:]
        this_sum, node = get_metadata_sum(remainder, children_ct=header[0], meta_ct=header[1])
        child_sums.append(this_sum)
    
    parent_sum = sum(node[:meta_ct]) + sum(child_sums)
    return parent_sum, node[meta_ct:]

meta_sum = get_metadata_sum(license_file)[0]

print("\nThe sum of all metadata entries is {}".format(meta_sum))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

def get_root_val(node, children_ct=1, meta_ct=1):
    if children_ct==0:
        return sum(node[:meta_ct]), node[meta_ct:]

    child_sums = []
    for child in range(children_ct):
        header = node[:2]
        remainder = node[2:]
        this_sum, node = get_root_val(remainder, children_ct=header[0], meta_ct=header[1])
        child_sums.append(this_sum)
    
    metavalues = node[:meta_ct]
    parent_sum = 0
    for mv in metavalues:
        if mv <= children_ct:
            parent_sum += child_sums[mv-1]
    
    return parent_sum, node[meta_ct:]

license_file.append(1)
root_node_val = get_root_val(license_file)[0]

print("\nThe value of the root node is {}".format(root_node_val))
print("Runtime: {} seconds".format(time()-start))