from time import time
start = time()

with open("2021/inputs/day_7_input.txt") as f:
    positions = [int(p) for p in f.readline().strip().split(',')]

#### PART 1

min_fuel_cost = 1000000
for x in range(min(positions), max(positions)+1):
    fuel_cost = 0
    for p in positions:
        fuel_cost += abs(x - p)
    if fuel_cost < min_fuel_cost:
        min_fuel_cost = fuel_cost

print("\nThe crabs must spend a minimum of {} fuel to align".format(min_fuel_cost))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

triangle = lambda N: N * (N+1) // 2

min_fuel_cost = 1000000000
for x in range(min(positions), max(positions)+1):
    fuel_cost = 0
    for p in positions:
        fuel_cost += triangle(abs(x - p))
    if fuel_cost < min_fuel_cost:
        min_fuel_cost = fuel_cost

print("The crabs must actually spend a minimum of {} fuel to align".format(min_fuel_cost))
print("Runtime: {} seconds\n".format(time()-start))