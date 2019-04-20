from unittest import TestCase
from knapsack import knapsack, Item


class TestKnapsack(TestCase):
    def test_knapsack(self):
        items = [Item(1, 1), Item(6, 2), Item(18, 5), Item(22, 6), Item(28, 7)]
        self.assertEqual(40, knapsack(11, items))

