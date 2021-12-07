from time import time
start = time()

with open("2019/inputs/day_1_input.txt") as f:
    masses = f.readlines()
masses = [int(n[:-1]) for n in masses]

#### PART 1

total_fuel = 0
for m in masses:
    total_fuel += (m // 3) - 2

print("\nThe sum of the fuel requirements is {}".format(total_fuel))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

def fuel_amt(mass):
    fuel = 0
    while mass > 0:
        mass = (mass // 3) - 2
        if mass > 0:
            fuel += mass
    return fuel

total_fuel = 0
for m in masses:
    total_fuel += fuel_amt(m)

print("\nThe sum of the fuel requirements is {}".format(total_fuel))
print("Runtime: {} seconds".format(time()-start))