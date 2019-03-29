from unittest import TestCase
from sum_range import *


class TestSumRange(TestCase):
    def test_low_gt_high(self):
        self.assertEqual(0, sum_range(10, 0))

    def test_low_eq_high(self):
        self.assertEqual(10, sum_range(10, 10))

    def test_low_lt_high(self):
        self.assertEqual(6, sum_range(1, 3))
        self.assertEqual(15, sum_range(1, 5))

    def test_step_gt_1(self):
        self.assertEqual(9, sum_range(1, 5, 2))
        self.assertEqual(9, sum_range(1, 6, 2))
