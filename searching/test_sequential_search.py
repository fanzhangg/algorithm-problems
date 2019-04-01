from unittest import TestCase
from sequential_search import *


class TestSequentialSearch(TestCase):
    def test_sequential_search(self):
        self.assertTrue(sequential_search([1, 2, 3], 1))
        self.assertFalse(sequential_search([1, 2, 3], 4))
