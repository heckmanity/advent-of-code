import numpy as np
from alive_progress import alive_bar
from copy import deepcopy
from time import time
start = time()

with open("2020/inputs/day_23_input.txt") as f:
    raw_data = f.readline()[:-1]

cup_circle = [int(char) for char in raw_data]
cup_circle = np.array(cup_circle, dtype='int64')
cup_reset = deepcopy(cup_circle)

#### PART 1 ####

def play_game(config, num_moves, verbose=False):
    num_cups = len(config)

    for move in range(num_moves):
        current_cup = config[0]
        picked_up = config[1:4]

        destination_cup = current_cup - 1
        if destination_cup < 1:
            destination_cup = num_cups
        while destination_cup in picked_up:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = num_cups
            
        destination_index = np.where(config == destination_cup)[0][0]

        config = np.concatenate( (config[:destination_index+1],  \
                                  picked_up,                     \
                                  config[destination_index+1:],  \
                                  np.array([current_cup])) )[4:]

        if verbose:
            print("debug {}".format(destination_index))
            print("current: {}".format(current_cup))
            print("pick up: {}".format(picked_up))
            print("destination: {}\n".format(destination_cup))
            print(config)

        bar()
    
    return config

move_ct = 100

print("\n")
with alive_bar(move_ct) as bar:
    cup_circle = play_game(cup_circle, move_ct)

labels = ''
index = (np.where(cup_circle == 1)[0][0] + 1) % len(cup_circle)
while not(cup_circle[index]==1):
    labels += str(cup_circle[index])
    index += 1
    index %= len(cup_circle)

print("\nThe labels on the cups after cup 1 are {}".format(labels))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

def play_game_fast(links, start_cup, num_moves, verbose=False):
    num_cups = len(links) - 1
    current_cup = start_cup

    for move in range(num_moves):
        picked_up = [current_cup]
        for i in range(3):
            picked_up.append(links[picked_up[-1]])
        picked_up.pop(0)

        links[current_cup] = links[picked_up[-1]]

        destination_cup = current_cup - 1
        if destination_cup < 1:
            destination_cup = num_cups
        while destination_cup in picked_up:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = num_cups
        
        links[picked_up[-1]] = links[destination_cup]
        links[destination_cup] = picked_up[0]

        if verbose:
            print("current: {}".format(current_cup))
            print("pick up: {}".format(picked_up))
            print("destination: {}\n".format(destination_cup))

        current_cup = links[current_cup]

        bar()
    
    return links

cup_circle = deepcopy(cup_reset)

cup_links = np.arange(1, 1000000+2)
for i in range(len(cup_circle)-1):
    cup_links[cup_circle[i]] = cup_circle[i+1]
cup_links[cup_circle[-1]] = len(cup_circle) + 1
cup_links[1000000] = cup_circle[0]
# print(cup_links)
# print(cup_links[1:])
# cup_links[0] = None

current_cup = cup_circle[i]
move_ct = 10000000

print("\n")
with alive_bar(move_ct) as bar:
    cup_links = play_game_fast(cup_links, cup_circle[0], move_ct)

factor_1 = cup_links[1]
factor_2 = cup_links[factor_1]
product = int(float(factor_1) * float(factor_2))

print("\nThe two cups immediately clockwise of cup 1 multiply to {} x {}".format(factor_1, factor_2))
print("\nThe two cups immediately clockwise of cup 1 multiply to {}".format(product))
print("Runtime: {} seconds".format(time()-start))