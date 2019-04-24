from unittest import TestCase
from cout_coins import *


class TestCountCoins(TestCase):
    def test_count_coins(self):
        coins = [Coin(5), Coin(1), Coin(5), Coin(1)]
        max_sum = count_coins(coins)
        print(max_sum)
