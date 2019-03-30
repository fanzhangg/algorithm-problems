from unittest import TestCase
from convert_int_to_str import *


class TestConvertIntToStr(TestCase):
    def test_binary(self):
        self.assertEqual("100100", convert_int_to_str(36, 2))

    def test_oct(self):
        self.assertEqual("1232", convert_int_to_str(666, 8))

    def test_hex(self):
        self.assertEqual("29A", convert_int_to_str(666, 16))
