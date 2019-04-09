from unittest import TestCase
from fibonacci import *


class TestFib(TestCase):
    def test_fib(self):
        self.assertEqual(0, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(13, fib(7))
