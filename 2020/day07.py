import re
from time import time
start = time()

with open("2020/inputs/day_7_input.txt") as f:
    rules = f.readlines()

color_parser = re.compile(r"""(?P<color>\w+\s\w+) bags contain""")
contents_parser = re.compile(r"""(?P<num>\d+) (?P<in_color>\w+\s\w+) bags*[,.]""")

ruleset = dict()
for rl in rules:
    ruleset[re.match(color_parser, rl).group(1)] = re.findall(contents_parser, rl)

my_bag_color = "shiny gold"

#### PART 1

hold_gold_cache = dict()

def hold_gold(color):
    if color in hold_gold_cache.keys():
        return hold_gold_cache[color]

    subcolors = [q[1] for q in ruleset[color]]
    if my_bag_color in subcolors:
        hold_gold_cache[color] = True
        return True
    
    sub_holds = [hold_gold(clr) for clr in subcolors]
    if True in sub_holds:
        hold_gold_cache[color] = True
        return True
    hold_gold_cache[color] = False
    return False

container_ct = 0
for bag_color in ruleset.keys():
    if hold_gold(bag_color):
        container_ct += 1

print("\n{} bag colors can eventually contain a shiny gold bag".format(container_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()
bag_ct_cache = dict()

def count_bags(color):
    if color in bag_ct_cache.keys():
        return bag_ct_cache[color]

    this_bag = sum([int(q[0]) for q in ruleset[color]])

    for clr in ruleset[color]:
        this_bag += int(clr[0]) * count_bags(clr[1])
    
    bag_ct_cache[color] = this_bag
    return this_bag

bag_ct = count_bags(my_bag_color)

print("\n{} individual bags are required inside a single {} bag".format(bag_ct, my_bag_color))
print("Runtime: {} seconds".format(time()-start))