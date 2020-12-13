import random
import itertools
import json
from collections import Counter

# 1 = Head
# 2 = Bow
# 3 = Horse
# 4 = 1 Sword
# 5 = 2 Sword
# 6 = 3 Sword
battlecards = {"Name": "test", "Battlelines": [1, 2, 3]}
# battlecards = {"Name" : "test", "Battlelines" : [1,2,3, [1, 2]]}
# print(battlecards.get("Battlelines"))
# temp = battlecards.get("Battlelines")
# temp.append(9)
# print(type(temp))
# print(temp)
battleline = [1, 1]
master_numb_dice = 2
test = range(7, 0, -1)
for i in test:
    print(i)


def calc_battlecard_permutations(battlelines, n):
    temp_options = []
    for i in range(n, 0, -1):
        1
    return 1


# need to merge the 4, 5, 6 (swords) into single sword count
# calculate all combinations of dice rolls given a number of dice
def calc_dice_permutations(n):
    x = [1, 2, 3, 4, 5, 6]
    return [p for p in itertools.product(x, repeat=n)]


def calc_battlecard_permutations(battlelines, n):
    return 1


# get a random dice roll given a number of dice
def battleline_roll(num_dice):
    roll = []
    for i in range(0, num_dice):
        roll.append(random.randint(0, 5))
    return roll;


# calculate the probability of succeeding a battleline given the battleline and a number of dice
def battleline_roll_prob(symbols, numb_dice):
    dice_permutations = calc_dice_permutations(numb_dice)
    calc_permutation_counters = lambda x: Counter(x)
    permutation_counters = list(map(calc_permutation_counters, dice_permutations))
    battleline_counter = Counter(symbols)

    true_count = 0
    for i in range(0, len(permutation_counters)):
        count = 0
        for (key, value) in battleline_counter.items():  # range(0, len(battleline_counter)):
            if permutation_counters[i].get(key) is None:
                continue
            else:
                if permutation_counters[i].get(key) >= value: count += 1
        if count == len(battleline_counter): true_count += 1
    return true_count / len(permutation_counters)


print(battleline_roll_prob(battleline, master_numb_dice))
