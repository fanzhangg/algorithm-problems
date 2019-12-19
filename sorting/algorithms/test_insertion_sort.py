from unittest import TestCase
from insertion_sort import insertion_sort


class TestInsertionSort(TestCase):
    def test_insertion_sort(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], insertion_sort([5, 1, 2, 3, 4, 0]))
        self.assertEqual([0, 1, 2, 3, 4, 5], insertion_sort([3, 1, 2, 4, 0, 5]))
