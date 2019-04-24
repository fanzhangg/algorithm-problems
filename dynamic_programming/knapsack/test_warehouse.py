import unittest
from warehouse import *


class WarehouseTest(unittest.TestCase):
    def test_get_max_copies(self):
        items = [Item(18, 5), Item(22, 6), Item(28, 7)]
        copies = get_max_object_copies(items, 11)
        for copy in copies:
            print(copy)

    def test_warehouse(self):
        items = [Item("1", 1, 1), Item("2", 6, 2), Item("3", 18, 5),
                 Item("4", 22, 6), Item("5", 28, 7)]
        result = warehouse(11, items)
        self.assertEqual((40, {'4', '3'}), result)
        result2 = warehouse(16, items)
        self.assertEqual((62, {'2', '5'}), result2)


if __name__ == '__main__':
    unittest.main()
