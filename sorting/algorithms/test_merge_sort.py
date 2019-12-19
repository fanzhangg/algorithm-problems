from unittest import TestCase
from mergesort import *


class TestMergeSort(TestCase):
    def test_split(self):
        self.assertEqual(([8, 1], [6, 4, 0]), split([8, 1, 6, 4, 0]))

    def test_merge(self):
        self.assertEqual([1, 2, 3, 5, 7, 8], merge([1, 2, 7], [3, 5, 8]))
        self.assertEqual([1, 1, 2, 3], merge([1], [1, 2, 3]))
        self.assertEqual([1, 5, 7, 8], merge([1, 5, 7], [8]))

    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([4, 2, 1, 3, 5]))
        self.assertEqual([8, 8, 10, 17], merge_sort([17, 8, 10, 8]))
