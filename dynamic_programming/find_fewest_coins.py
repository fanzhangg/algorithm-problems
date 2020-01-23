def find_fewest_coins(amount: int, coins: [int])->dict:
    """
    A greedy method to calculate the fewest coins. Not appliable for all cases
    """
    coin_nums = {}  # A dictionary to keep track of the number of every coin
    coins.sort(reverse=True)
    remain = amount

    for coin in coins:
        num = remain // coin
        remain = amount % coin
        coin_nums[coin] = num
    return coin_nums

def rec_count_coins(coin_vlaue_li: [int], change: int):
    """
    A recursive approach to calculate the fewest coins. Not efficient.
    """
    min_coins = change
    if change in coin_vlaue_li:
        return 1
    else:
        for x in [c for c in coin_vlaue_li if c <= change]:
            num_coins = 1 + rec_count_coins(coin_vlaue_li, change - x)
            if num_coins < min_coins:
                min_coins = num_coins
        return min_coins

def rec_dynamic_count_coins(coin_value_li: [int], change: int, results: [[int]]):
    min_coins = change
    if change in coin_value_li:
        return 1
    elif results[change] > 0:
        return results[change]
    else:
        for x in [c for c in coin_value_li if c <= change]:
            num_coins = 1 + rec_dynamic_count_coins(coin_value_li, change - x, results)
            if num_coins < min_coins:
                min_coins = num_coins
                results[change] = min_coins
    return min_coins

def dp_make_change(coins_value_li: [int], change: int, min_coins: [int], used_coins: [int]):
    """
    A dynamic approach to calculate the fewest number of coins to make a change
    coins_value_li: a list of each coin's value
    change: the amount of change to make
    min_coins: the minimal number of coins
    used_coins: the used coins
    """
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coins_value_li if c <= cents]:
            new_count = min_coins[cents - j] + 1
            if new_count < coin_count:
                coin_count = new_count
                new_coin = j
        min_coins[cents] = coin_count
        used_coins[cents] = new_coin
    return min_coins[change]

def print_coins(used_coins: [int], change: int):
    coin = change
    while coin > 0:
        this_coin = used_coins[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin

coin_li = [1, 5, 10, 21, 25]
amount = 63
used_coins = [0] * (amount + 1)
coin_counts = [0] * (amount + 1)
print("Making change for", amount, "requires", dp_make_change(coin_li, amount, coin_counts, used_coins), "coins")
print("They are:")
print_coins(used_coins, amount)
