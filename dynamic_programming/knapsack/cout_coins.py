from typing import List, Set


class Coin(object):
    def __init__(self, value: int):
        self.value = value


def count_coins(coins: List[Coin])->int:
    """
    :recurrence relation:
    - If i = 1, OPT[i] = v
    - If i = 0, OPT[i] = 0
    - Else, OPT[i] = max(OPT[i-1], vi + OPT[i-2])

    :param coins: a list of coins, each coin i has value > 0
    :return: a set of coins such as the sum of their values is maximized, and no two coins are adjacent
    """
    opt = [None for _ in range(len(coins) + 1)]
    opt[0] = 0
    opt[1] = 1
    opt_coins = []

    def get_coins(j):
        if j == 1 or j == 0:
            pass
        elif coins[j - 2].value + opt[j - 2] > opt[j - 1]:
            opt_coins.append(coins[j - 2].value)
            get_coins(j - 2)
        else:
            get_coins(j - 1)

    for i in range(2, len(coins) + 1):
        opt[i] = max(coins[i - 2].value + opt[i - 2], opt[i - 1])

    get_coins(len(coins) + 1)
    return opt[-1], opt_coins
