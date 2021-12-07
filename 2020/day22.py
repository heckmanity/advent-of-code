from copy import deepcopy
from time import time
start = time()

with open("2020/inputs/day_22_input.txt") as f:
    raw_data = f.readlines()

decks = []
for line in raw_data:
    if line[:6]=="Player":
        decks.append([])
    elif line=="\n":
        continue
    else:
        decks[-1].append(int(line[:-1]))

deck_reset = deepcopy(decks)

#### PART 1 ####

def Combat(decks):
    while all([len(D)>0 for D in decks]):
        hand = [D.pop(0) for D in decks]
        hand_winner = max([i for i in range(len(hand))], key=lambda x: hand[x])
        decks[hand_winner] += sorted(hand, reverse=True)

    winning_player = [len(D)>0 for D in decks].index(True)
    winning_deck = decks[winning_player]

    winning_score = 0
    for mult in range(1, len(winning_deck)+1):
        winning_score += mult * winning_deck[len(winning_deck)-mult]
    
    return winning_score

winning_score = Combat(decks)

print("\nThe winning player's Combat score will be {}".format(winning_score))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

# game_num = 1

def Recursive_Combat(decks, lvl=0):
    # print("\n=== Game {} ===".format(game_num))
    prev_rounds = set()
    # round_num = 1

    while all([len(D)>0 for D in decks]):
        # print("\n-- Round {} (Game {}) --".format(round_num, game_num))
        # print("Player 1's deck: {}".format(decks[0]))
        # print("Player 2's deck: {}".format(decks[1]))

        game_state = tuple([tuple(D) for D in decks])
        if game_state in prev_rounds:
            if lvl==0:
                return "winning_score"
            else:
                return 0 # Player 1 wins
        else:
            prev_rounds.add(game_state)
        
        hand = [D.pop(0) for D in decks]

        # print("Player 1 plays: {}".format(hand[0]))
        # print("Player 2 plays: {}".format(hand[1]))

        if all([len(decks[i])>=hand[i] for i in range(len(hand))]):
            sub_decks = [decks[i][:hand[i]] for i in range(len(hand))]
            # print("Playing a sub-game to determine the winner...")
            hand_winner = Recursive_Combat(sub_decks, lvl=lvl+1)
            
            if hand_winner:
                hand = hand[::-1]
            decks[hand_winner] += hand
        else:
            hand_winner = max([i for i in range(len(hand))], key=lambda x: hand[x])
            decks[hand_winner] += sorted(hand, reverse=True)
        
        # print("Player {} wins round {} of game {}!".format(hand_winner+1, round_num, game_num))
        # round_num += 1

    winning_player = [len(D)>0 for D in decks].index(True)
    winning_deck = decks[winning_player]

    winning_score = 0
    for mult in range(1, len(winning_deck)+1):
        winning_score += mult * winning_deck[len(winning_deck)-mult]
    
    if lvl==0:
        return winning_score
    else:
        # print("The winner of game {} is player {}!".format(game_num, winning_player-1))
        return winning_player

decks = deepcopy(deck_reset)
winning_score = Recursive_Combat(decks)

print("\nThe winning player's Recursive Combat score will be {}".format(winning_score))
print("Runtime: {} seconds".format(time()-start))