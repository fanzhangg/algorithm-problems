from unittest import TestCase
from get_closest_pair.get_closest_pair import *
import copy

"""
@author: Fan Zhang
@date: Apr 14, 2019
"""


class TestGetDistance(TestCase):
    def test_get_distance(self):
        self.assertEqual(5, get_distance((0, 3), (4, 0)))
        self.assertEqual(3.1622776601683795, get_distance((5, 4), (2, 3)))


class TestDoBaseCase(TestCase):
    def test_do_base_case(self):
        self.assertEqual((get_distance((1, 2), (3, 5)), ((1, 2), (3, 5))), do_base_case([(1, 2), (3, 5), (10, 10)]))


class TestGetMidX(TestCase):
    def test_odd_items(self):
        self.assertEqual(2, get_mid_x([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]))

    def test_even_items(self):
        self.assertEqual(2, get_mid_x([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]))


class TestGetMidI(TestCase):
    def test_odd_items(self):
        self.assertEqual(2, get_mid_i([0, 1, 2, 3, 4]))
        self.assertEqual(2, get_mid_i([0, 1, 2, 3, 4, 5]))


class TestGetClosestToLinePoints(TestCase):
    def test_get_closest_to_line_points(self):
        # get_close_to_line_points(points_y: List[Tuple], min_dist: float, mid_x: float)->List[Tuple]:
        points_y = [(1, 2), (3, 2), (5, 2), (6, 2), (9, 2), (15, 2), (17, 2), (18, 2)]
        points = get_close_to_line_points(points_y, 4, 8)
        self.assertEqual([(5, 2), (6, 2), (9, 2)], points)


class TestGetNext7Points(TestCase):
    def test_points_lt_7(self):
        self.assertEqual([3, 2, 1], get_next_7_points_distances((8, 2), [(5, 2), (6, 2), (9, 2)]))

    def test_points_gt_7(self):
        points = [(1, 0), (2, 0), (3, 0), (4, 0),
                  (6, 0), (7, 0), (8, 0), (9, 0)]
        self.assertEqual([4, 3, 2, 1, 1, 2, 3], get_next_7_points_distances((5, 0), points))


class TestGetClosestPair(TestCase):
    def test_get_closest_pair(self):
        points = [(1, 0), (3, 0), (5, 0), (6, 0), (8, 0), (10, 0), (12, 0), (15, 0)]
        points.sort(key=lambda p: p[0])
        points_x = copy.deepcopy(points)
        points.sort(key=lambda p: p[1])
        points_y = copy.deepcopy(points)
        points = get_closest_pair(points_x, points_y)
        print(points)

    def test_get_closest_pair_1(self):
        points = [(0, 0), (1, 0), (5, 0), (8, 100), (12, -30), (20, -45), (50, 1000)]
        points.sort(key=lambda p: p[0])
        points_x = copy.deepcopy(points)
        points.sort(key=lambda p: p[1])
        points_y = copy.deepcopy(points)
        points = get_closest_pair(points_x, points_y)
        print(points)
