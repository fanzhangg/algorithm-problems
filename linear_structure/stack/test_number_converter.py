from unittest import TestCase

from number_converter import *


class TestNumberConverter(TestCase):
    def test_dec_to_bin(self):
        num = 233
        bin_str = dec_to_bin(num)
        self.assertEqual("11101001", bin_str)

    def test_dec_to_oct(self):
        self.assertEqual("30444", dec_to_oct(12580))

    def test_dec_to_hex(self):
        self.assertEqual("3124", dec_to_hex(12580))
        self.assertEqual("7DE", dec_to_hex(2014))
