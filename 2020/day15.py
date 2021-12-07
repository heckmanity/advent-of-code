from alive_progress import alive_bar
from time import time
start = time()

starting_numbers = [1,2,16,19,18,0]

def play(num_turns):
    spawns = dict()
    prev_num = None
    print("\n")

    with alive_bar(num_turns) as bar:
        for turn in range(num_turns):
            if turn < len(starting_numbers):
                spoken_num = starting_numbers[turn]
            elif not(prev_num in spawns.keys()):
                spoken_num = 0
            else:
                spoken_num = turn - spawns[prev_num]
            
            spawns[prev_num] = turn
            prev_num = spoken_num

            bar()
    
    return spoken_num

#### PART 1 ####

target = 2020
last_said = play(target)

print("\nThe {}th number spoken is {}".format(target, last_said))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

target = 30_000_000
last_said = play(target)

print("\nThe {}th number spoken is {}".format(target, last_said))
print("Runtime: {} seconds".format(time()-start))