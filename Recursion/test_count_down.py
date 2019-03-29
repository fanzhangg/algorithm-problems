from unittest import TestCase
from count_down import *


class TestCountDown(TestCase):
    def test_step_eq_1(self):
        count_down(10)

    def test_end_eq_0(self):
        count_down(10, -2)

    def test_end_ne_0(self):
        count_down(10, -3)

    def test_step_ge_0(self):
        with self.assertRaises(ValueError):
            count_down(0, 10)
