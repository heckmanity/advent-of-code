import re
from collections import deque
from alive_progress import alive_bar
from time import time
start = time()

with open("2018/inputs/day_9_input.txt") as f:
    input_data = f.readline()[:-1]

parse_str = re.compile(r"""(?P<player_ct>\d*) players; last marble is worth (?P<final_pts>\d*)""")
vals = re.match(parse_str, input_data).groupdict()

num_players = int(vals['player_ct'])
last_marble = int(vals['final_pts'])

#### PART 1 ####

def game(players, endpoint):
    scorecard = [0] * (players + 1)
    circle = deque([0])
    current_marble = 0
    turn_number = 1

    print("\nPlaying game...")
    with alive_bar(endpoint) as bar:
        while turn_number <= endpoint:
            if turn_number % 23 == 0:
                pyr = turn_number % players
                turn_score = turn_number

                circle.rotate(7)
                turn_score += circle.pop()
                circle.rotate(-1)

                scorecard[pyr] += turn_score
            else:
                circle.rotate(-1)
                circle.append(turn_number)

            turn_number += 1
            bar()

    return max(scorecard)

high_score = game(num_players, last_marble)

print("\nThe winning score is {}".format(high_score))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

new_high_score = game(num_players, 100*last_marble)

print("\nThe new winning score is {}".format(new_high_score))
print("Runtime: {} seconds".format(time()-start))