from unittest import TestCase

from stack.simple_balanced_parentheses import is_balanced_parentheses


class TestIsBalancedParentheses(TestCase):
    def test_more_opening_par(self):
        self.assertFalse(is_balanced_parentheses("(()"))

    def test_more_closing_par(self):
        self.assertFalse(is_balanced_parentheses("())"))

    def test_balanced_par(self):
        self.assertTrue(is_balanced_parentheses("(())()(())"))
