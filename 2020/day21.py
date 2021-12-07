from functools import reduce
from time import time
start = time()

with open("2020/inputs/day_21_input.txt") as f:
    raw_data = f.readlines()

recipes = []
for line in raw_data:
    ingredient_string, allergen_string = line[:-1].split(" (contains ")
    this_recipe = dict()
    this_recipe['ingredients'] = ingredient_string.split(" ")
    this_recipe['allergens'] = allergen_string[:-1].split(", ")
    recipes.append(this_recipe)

ingredients = set()
allergens = set()
for rcp in recipes:
    for ing in rcp['ingredients']:
        ingredients.add(ing)
    for alg in rcp['allergens']:
        allergens.add(alg)

#### PART 1 ####

set_union = lambda x, y: x.union(y)
set_intersect = lambda x, y: x.intersection(y)

poss_sources_of = dict()
for alg in allergens:
    poss_sources_of[alg] = []
    for rcp in recipes:
        if alg in rcp['allergens']:
            poss_sources_of[alg].append(set(rcp['ingredients']))

for alg in poss_sources_of.keys():
    poss_sources_of[alg] = reduce(set_intersect, poss_sources_of[alg])
        
unsafe_ingred = reduce(set_union, poss_sources_of.values())
safe_ingred = ingredients.difference(unsafe_ingred)

safe_ct = 0
for sfi in safe_ingred:
    for rcp in recipes:
        safe_ct += rcp['ingredients'].count(sfi)

print("\nThe ingredients which are definitely allergen-free appear {} times".format(safe_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

identified_allergens = dict()
while len(identified_allergens) < len(allergens):
    for confirmed_ingred in identified_allergens.values():
        for alg in poss_sources_of.keys():
            if confirmed_ingred in poss_sources_of[alg]:
                poss_sources_of[alg].remove(confirmed_ingred)

    to_remove = []
    for alg in poss_sources_of.keys():
        if len(poss_sources_of[alg])==1:
            identified_allergens[alg] = list(poss_sources_of[alg])[0]
            to_remove.append(alg)
    
    for alg in to_remove:
        poss_sources_of.pop(alg)

bad_list = ''

for alg in sorted(list(allergens)):
    bad_list += identified_allergens[alg] + ","
bad_list = bad_list[:-1]

print("\nThe canonical dangerous ingredient list is {}".format(bad_list))
print("Runtime: {} seconds".format(time()-start))