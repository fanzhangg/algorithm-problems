import unittest
from find_median import *


class QueryTest(unittest.TestCase):
    def test_query(self):
        l = [0, 1, 2, 3, 4, 5]
        self.assertEqual(0, query(0, l))


class FindMedianTest(unittest.TestCase):
    def test_find_median(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [6, 7, 8, 9, 10]
        self.assertEqual(5, get_median(l1, l2))
        l1 = [1, 2, 3, 4]
        l2 = [6, 7, 8, 9]
        self.assertEqual(4, get_median(l1, l2))

    def test_2(self):
        l1 = [1, 3, 10, 20, 25, 27]
        l2 = [2, 5, 7, 9, 10, 11]
        self.assertEqual(7, get_median(l1, l2))


if __name__ == '__main__':
    unittest.main()
