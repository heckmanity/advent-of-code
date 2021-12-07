from time import time
start = time()

with open("2020/inputs/day_25_input.txt") as f:
    card_public = int(f.readline()[:-1])
    door_public = int(f.readline()[:-1])

def transform(subject, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject
        value %= 20201227
    return value

#### PART 1 ####

card_transform = 1
door_transform = 1
initial_subject = 7
loop_ct = 0

while not(card_public==card_transform or door_public==door_transform):
    loop_ct += 1
    card_transform = (card_transform * initial_subject) % 20201227
    door_transform = (door_transform * initial_subject) % 20201227

if card_public==card_transform:
    encryption_key = transform(door_public, loop_ct)
if door_public==door_transform:
    encryption_key = transform(card_public, loop_ct)

print("\nThe handshake is trying to establish encryption key {}".format(encryption_key))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

# No Part 2