from unittest import TestCase
from sum_after import *


class TestSumAfter(TestCase):
    def test_sum_after(self):
        self.assertEqual(3, sum_after([1, 1, 1]))
        self.assertEqual(3, sum_after([1, 1, 1], 0))
        self.assertEqual(6, sum_after([1, 1, 2, 2, 2], 2))

    def test_pos_out_index(self):
        self.assertEqual(0, sum_after([1, 2, 1], 10))

    def test_pos_less_0(self):
        self.assertEqual(3, sum_after([1, 1, 1], -3))
