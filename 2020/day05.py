from time import time
start = time()

with open("2020/inputs/day_5_input.txt") as f:
    seats = f.readlines()

#### PART 1

max_seat_id = 0
all_ids = []

for seat in seats:
    row = seat[:-4].replace('F','0').replace('B','1')
    row = int(row, 2)
    col = seat[-4:-1].replace('L','0').replace('R','1')
    col = int(col, 2)

    seat_id = row * 8 + col
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    all_ids.append(seat_id)

print("\nThe highest seat ID is {}".format(max_seat_id))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

all_ids = sorted(all_ids)
diffs = []
for i in range(1, len(all_ids)):
    diffs.append(all_ids[i] - all_ids[i-1])

gap_index = diffs.index(2)
my_seat = gap_index + all_ids[0] + 1

print("\nMy seat has ID number {}".format(my_seat))
print("Runtime: {} seconds".format(time()-start))