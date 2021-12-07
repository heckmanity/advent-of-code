from time import time
start = time()

day_10_input = "1113222113"

#### PART 1 ####

def look_n_say(seq):
    curr_digit = seq[0]
    curr_count = 1

    new_seq = ''
    for dig in seq[1:]:
        if dig==curr_digit:
            curr_count += 1
        else:
            new_seq += str(curr_count) + curr_digit
            curr_digit = dig
            curr_count = 1
    new_seq += str(curr_count) + curr_digit

    return new_seq

iterations = 40

curr_seq = day_10_input
for i in range(iterations):
    curr_seq = look_n_say(curr_seq)

print("\nAfter {} iterations the sequence length is {}".format(iterations, len(curr_seq)))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

iterations = 50

curr_seq = day_10_input
for i in range(iterations):
    curr_seq = look_n_say(curr_seq)

print("\nAfter {} iterations the sequence length is {}".format(iterations, len(curr_seq)))
print("Runtime: {} seconds".format(time()-start))