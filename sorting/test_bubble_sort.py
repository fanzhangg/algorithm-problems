from unittest import TestCase
from bubble_sort import bubble_sort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], bubble_sort([4, 3, 1, 2, 5, 0]))
        self.assertEqual([0, 1, 2, 3, 4, 5], bubble_sort([5, 1, 3, 2, 4, 0]))
