from copy import deepcopy
from time import time
start = time()

player_reset = {'HP': 50, 'Armor': 0, 'Mana': 500, 'Effects': dict()}
boss_reset = {'HP': 58, 'Damage': 9}

store = dict()
store['Missile'] = {'type': 'inst', 'cost': 53, 'damage': 4, 'health': 0}
store['Drain'] = {'type': 'inst', 'cost': 73, 'damage': 2, 'health': 2}
store['Shield'] = {'type': 'effect', 'cost': 113, 'lifespan': 6}
store['Poison'] = {'type': 'effect', 'cost': 173, 'lifespan': 6}
store['Recharge'] = {'type': 'effect', 'cost': 229, 'lifespan': 5}

#### PART 1 ####

def do_effects(pyr, boss):
    player = deepcopy(pyr)
    enemy = deepcopy(boss)
    if len(player['Effects']) > 0:
        if 'Shield' in player['Effects'].keys():
            player['Armor'] = 7
        else:
            player['Armor'] = 0

        to_remove = []
        for eff in player['Effects'].keys():
            if eff=='Poison':
                enemy['HP'] -= 3
            if eff=='Recharge':
                player['Mana'] += 101

            player['Effects'][eff] -= 1
            if player['Effects'][eff] == 0:
                to_remove.append(eff)
            
        for eff in to_remove:
            player['Effects'].pop(eff)

    return player, enemy

def game_turn(pyr, boss, option=None, expenditure=0):
    # cum_expense = expenditure
    turn_expense = 0
    player = deepcopy(pyr)
    enemy = deepcopy(boss)
    if option:
        # print('---{}---'.format(option))
        # Player turn
        player, enemy = do_effects(player, enemy)

        if enemy['HP'] <= 0:
            return turn_expense

        player['Mana'] -= store[option]['cost']
        turn_expense += store[option]['cost']
        if store[option]['type']=='inst':
            enemy['HP'] -= store[option]['damage']
            player['HP'] += store[option]['health']
        if store[option]['type']=='effect':
            player['Effects'][option] = store[option]['lifespan']

        # print(player, enemy, '\n')

        if enemy['HP'] <= 0:
            return turn_expense

        # Boss turn
        player, enemy = do_effects(player, enemy)
        damage_dealt = enemy['Damage'] - player['Armor']
        if damage_dealt < 1:
            damage_dealt = 1
        player['HP'] -= damage_dealt

        # print(player, enemy, '\n')

        if player['HP'] <= 0:
            return None
    
    available_spells = []
    for spl in store.keys():
        if store[spl]['cost'] <= player['Mana'] and not(spl in player['Effects']):
            available_spells.append(spl)
    # print(available_spells)
    
    expenses = []
    for spl in available_spells:
        cum_spl_cost = game_turn(player, enemy, option=spl)
        if cum_spl_cost:
            expenses.append(cum_spl_cost)
    
    if len(expenses) > 0:
        return min(expenses) + turn_expense
    else:
        return turn_expense

least_mana = game_turn(player_reset, boss_reset)

print("\nYou must spend at least {} mana to win the fight".format(least_mana))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

# start = time()

# print("\nYou can spend at most {} gold and lose the fight".format(most_gold))
# print("Runtime: {} seconds".format(time()-start))