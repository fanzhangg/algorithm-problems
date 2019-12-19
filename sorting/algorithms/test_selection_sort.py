from unittest import TestCase
from selection_sort import selection_sort


class TestSelectionSort(TestCase):
    def test_selection_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], selection_sort([9, 8, 1, 5, 4, 3, 7, 2, 10, 6]))
        self.assertEqual([1, 2, 3, 4, 5], selection_sort([5, 1, 3, 4, 2]))
