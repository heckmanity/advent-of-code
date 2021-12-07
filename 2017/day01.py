from time import time
start = time()

with open("2017/inputs/day_01_input.txt") as f:
    sequence = f.readline()

#### PART 1

solution = 0
seq_len = len(sequence)

for i in range(seq_len):
    if sequence[i] == sequence[(i+1)%seq_len]:
        solution += int(sequence[i])

print("\nThe captcha solution is {}".format(solution))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

new_solution = 0
half_len = seq_len // 2

for i in range(seq_len):
    if sequence[i] == sequence[(i+half_len)%seq_len]:
        new_solution += int(sequence[i])

print("\nThe new captcha solution is {}".format(new_solution))
print("Runtime: {} seconds".format(time()-start))