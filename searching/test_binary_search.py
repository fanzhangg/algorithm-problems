from unittest import TestCase
from binary_search import binary_search_2 as binary_search


class TestBinarySearch(TestCase):
    def test_true_case_odd_list(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))
        self.assertTrue(binary_search([0, 1, 2, 3, 4, 5, 6, 7], 1))

    def test_true_cse_even_list(self):
        self.assertTrue(binary_search([0, 1, 2, 3, 4, 5], 0))
        self.assertTrue(binary_search([0, 1, 2, 3, 4, 5], 5))

    def test_false_case(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 8))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], -10))
