from time import time
start = time()

with open("2021/inputs/day_1_input.txt") as f:
    data = f.readlines()

depths = []
for ln in data:
    depths.append(int(ln.strip('\n')))

#### PART 1

count = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        count += 1

print("{} measurements are larger than the previous measurement".format(count))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

sums = []
for i in range(2, len(depths)):
    sums.append(sum(depths[i-2:i+1]))

new_count = 0
for j in range(1, len(sums)):
    if sums[j] > sums[j - 1]:
        new_count += 1

print("{} sums are larger than the previous sum".format(new_count))
print("Runtime: {} seconds".format(time()-start))