from unittest import TestCase
from knapsack import knapsack, Item
import csv


class TestKnapsack(TestCase):
    @staticmethod
    def get_items() -> list:
        items = []
        with open("knapsackItems.csv") as file:
            reader = csv.reader(file)
            line_num = 0
            for row in reader:
                if line_num == 0:
                    pass
                else:
                    name = row[0]
                    value = int(row[1])
                    weight = int(row[2])
                    items.append(Item(name, value, weight))
                line_num += 1
        return items

    def test_knapsack(self):
        items = self.get_items()
        print(knapsack(11, items))
        self.assertEqual((40, {'item4', 'item3'}), knapsack(11, items))

