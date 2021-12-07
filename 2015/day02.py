from time import time
start = time()

with open("2015/inputs/day_2_input.txt") as f:
    dimensions = f.readlines()
presents = [sorted([int(S) for S in D[:-1].split('x')]) for D in dimensions]

#### PART 1

paper_reqd = 0
for gift in presents:
    L, W, H = gift
    paper_reqd += 3*L*W + 2*(W*H + L*H)

print("\n{} square feet of wrapping paper is needed".format(paper_reqd))
print("Runtime: {} seconds".format(time()-start))

# #### PART 2

start = time()

ribbon_reqd = 0
for gift in presents:
    L, W, H = gift
    ribbon_reqd += 2*(L+W) + L*W*H

print("\n{} linear feet of ribbon is needed".format(ribbon_reqd))
print("Runtime: {} seconds".format(time()-start))