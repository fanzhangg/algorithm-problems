from unittest import TestCase
from factorial import *


class TestFactorial(TestCase):
    def test_factorial(self):
        self.assertEqual(6, factorial(3))

    def test_raise_error(self):
        with self.assertRaises(ValueError):
            factorial(-3)
