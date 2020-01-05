import unittest

from stack.balanced_symbol import *


class TestBalancedSymbols(unittest.TestCase):
    def test_match(self):
        self.assertTrue(match("(", ")"))
        self.assertFalse(match("{", ")"))

    def test_balanced_case(self):
        self.assertTrue(is_balanced_symbols("()()[]"))

    def test_more_open_symbols_case(self):
        self.assertFalse(is_balanced_symbols("((([]))"))

    def test_more_close_symbol_case(self):
        self.assertFalse(is_balanced_symbols("{{{[]]}}}"))

    def test_diff_open_close_symbol_case(self):
        self.assertFalse(is_balanced_symbols("{[}}"))


if __name__ == '__main__':
    unittest.main()
