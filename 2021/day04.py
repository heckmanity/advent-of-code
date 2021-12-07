from time import time
start = time()

with open("2021/inputs/day_4_input.txt") as f:
    raw_data = f.readlines()

cards = []
next_card = []
for i, data in enumerate(raw_data):
    if i==0:
        order = [int(j) for j in data.split(',')]
        continue
    if data=='\n':
        if not(i==1):
            cards.append(next_card)
            next_card = []
        continue
    next_card.append([int(k) for k in data.strip('\n').split(' ') if not(k=='')])

def check_win(card, called):
    for row in card:
        if all([num in called for num in row]):
            return True
    card_T = [ [ rw[i] for rw in card ] for i in range(len(card[0])) ]
    for col in card_T:
        if all([num in called for num in col]):
            return True
    return False

def sum_unmarked(card, called):
    total = 0
    for row in card:
        for num in row:
            if not(num in called):
                total += num
    return total

#### PART 1

winner = False
num_called = 0
while not winner:
    num_called += 1
    for card in cards:
        if check_win(card, order[:num_called]):
            winner = card
            break

score = sum_unmarked(winner, order[:num_called]) * order[num_called - 1]

print("\nThe final score of the winning board is {}".format(score))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

num_called = 0
while cards:
    if len(cards)==1:
        winner = cards[0]
    winners = []
    num_called += 1
    for i, card in enumerate(cards):
        if check_win(card, order[:num_called]):
            winners.append(i)
    for j in winners[::-1]:
        cards.pop(j)

score = sum_unmarked(winner, order[:num_called]) * order[num_called - 1]

print("The final score of the last-to-win board is {}".format(score))
print("Runtime: {} seconds".format(time()-start))