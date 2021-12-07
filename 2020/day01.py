from time import time
start = time()
goal_sum = 2020

values = []
with open("2020/inputs/day_1_input.txt") as f:
    values = f.readlines()
values = [int(n[:-1]) for n in values]

#### PART 1

for val in values:
    remain = goal_sum - val
    if remain in values:
        print("{} x {} = {}".format(val, remain, val*remain))
        break

print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()
done = False
for val in values:
    remain = goal_sum - val
    for next_val in values:
        if val==next_val:
            continue
        else:
            third = remain - next_val
            if third in values and not(third==val or third==next_val):
                done = True
                print("{} x {} x {} = {}".format(val, next_val, third, \
                    val*next_val*third))
                break
        if done:
            break

print("Runtime: {} seconds".format(time()-start))