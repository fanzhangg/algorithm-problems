from unittest import TestCase
from is_palindrome import *


class TestIsPalindrome(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("hannah"))
        self.assertFalse(is_palindrome("mark"))

