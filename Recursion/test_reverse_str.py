from unittest import TestCase
from reverse_str import *


class TestReverseStr(TestCase):
    def test_reverse_str(self):
        self.assertEqual("olleh", reverse_str("hello"))
        self.assertEqual("dlrow", reverse_str("world"))

    def test_get_palindrome(self):
        self.assertEqual("anna", get_palindrome("an"))
