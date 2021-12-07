from time import time
start = time()

with open("2019/inputs/day_8_input.txt") as f:
    image = f.readline()[:-1]
layers = [image[q*150:(q+1)*150] for q in range(len(image)//150)]

#### PART 1

best_index = None
best_zero_ct = 150
for ind in range(len(layers)):
    zero_ct = layers[ind].count('0')
    if zero_ct < best_zero_ct:
        best_zero_ct = zero_ct
        best_index = ind

check_product = layers[best_index].count('1') * layers[best_index].count('2')

print("\nThe product of 1- and 2-counts is {}".format(check_product))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

print("\nThe message produced is:\n")
for row in range(6):
    this_row = ''
    for col in range(25):
        index = row * 25 + col
        for lyr in layers:
            if lyr[index]=='2':
                continue
            else:
                if lyr[index]=='0':
                    this_row += ' ' # '░'
                if lyr[index]=='1':
                    this_row += '█'
                break
    print(this_row)

print("\nRuntime: {} seconds".format(time()-start))