from maths.linear.functions import *
import unittest


class TestFunctions(unittest.TestCase):
    def test_int_dec_to_bin(self):
        ans = int_dec_to_bin(53)
        self.assertEqual(ans, "110101")

    def test_frac_dec_to_bin(self):
        ans = frac_dec_to_bin(0.7, 6)
        self.assertEqual(ans, "101100")

    def test_float_dec_to_bin(self):
        ans = float_dec_to_bin(53.7, 6)
        self.assertEqual(ans, "110101.101100")

    def test_int_bin_to_dec(self):
        ans = int_bin_to_dec("10101")
        self.assertEqual(ans, 21)

    def test_float_bin_to_dec(self):
        ans = frac_bin_to_dec("1011")
        print(ans)
