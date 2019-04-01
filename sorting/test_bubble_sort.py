from unittest import TestCase
from bubble_sort import bubble_sort_2 as bubble_sort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], bubble_sort([4, 3, 1, 2, 5, 0]))
