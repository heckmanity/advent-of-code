from alive_progress import alive_bar
from time import time
start = time()

day_20_input = 34000000
street_length = 1000000

#### PART 1 ####

presents = [0 for i in range(1, street_length+1)]

print("\nDistributing gifts...")
with alive_bar(street_length) as bar:
    for elf in range(1, street_length+1):
        bar()
        for i in range(1, street_length//elf + 1):
            presents[i*elf-1] += elf

presents = [10*p for p in presents]

print("\nCounting gifts...")
with alive_bar(street_length) as bar:
    for house_num in range(1, street_length+1):
        bar()
        if presents[house_num-1] > day_20_input:
            break

print("\nThe lowest house number to get at least {} presents is {}".format(day_20_input, house_num))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

presents = [0 for i in range(1, street_length+1)]

print("\nDistributing gifts...")
with alive_bar(street_length) as bar:
    for elf in range(1, street_length+1):
        bar()
        for i in range(1, 51):
            if i*elf >= len(presents):
                break
            presents[i*elf-1] += elf

presents = [11*p for p in presents]

print("\nCounting gifts...")
with alive_bar(street_length) as bar:
    for house_num in range(1, street_length+1):
        bar()
        if presents[house_num-1] > day_20_input:
            break

print("\nThe lowest house number to get at least {} presents is {}".format(day_20_input, house_num))
print("Runtime: {} seconds".format(time()-start))