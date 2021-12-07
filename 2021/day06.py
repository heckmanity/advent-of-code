from time import time
start = time()

with open("2021/inputs/day_6_input.txt") as f:
    starting_school = [int(t) for t in f.readline().strip('\n').split(',')]

timer_counts = [starting_school.count(i) for i in range(9)]

def growth_model(timers, periods):
    for day in range(periods):
        num_births = timers[0]
        timers = timers[1:] + [num_births]
        timers[6] += num_births
    return sum(timers)

#### PART 1

num_days = 80
population = growth_model(timer_counts, num_days)

print("\nThere will be {} lanternfish after {} days".format(population, num_days))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

num_days = 256
population = growth_model(timer_counts, num_days)

print("There will be {} lanternfish after {} days".format(population, num_days))
print("Runtime: {} seconds\n".format(time()-start))