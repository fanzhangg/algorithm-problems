from unittest import TestCase
from min_stops import *


class TestMinStops(TestCase):
    def test_valid_stops(self):
        dists = [1, 3, 10, 3, 5, 4, 10, 2, 8, 9]
        self.assertEqual([3, 6], min_stops(dists, 20))

    def test_invalid_stops(self):
        dists = [6, 2, 2, 2, 2, 2, 2, 2]
        self.assertIsNone(min_stops(dists, 4))
        self.assertIsNone(min_stops([2, 5, 2, 2], 4))
        self.assertIsNone(min_stops([2, 2, 2, 5], 4))

