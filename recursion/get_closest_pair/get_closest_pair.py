from typing import List, Tuple
import math
from itertools import combinations

"""
@author: Fan Zhang
@date: Apr 14, 2019
@credits: Lauren Milne, Algorithm Design (Kleinberg Tardos 2005)
"""


def get_closest_pair(points_x: List[Tuple], points_y: List[Tuple])->Tuple[float, Tuple]:
    """
    Find the closest pair among n points
    :param points_x: points list sorted by x-coordinator
    :param points_y: points list sorted by y-coordinator
    :return: the two points that are closest together (two point i, j: minimize (i.x - j.x) ^ 2 - (i.y - j.y) ^ 2)
    """
    if len(points_x) <= 3:
        return do_base_case(points_x)

    # TODO: x-value of middle element in Px?

    mid_x = get_mid_x(points_x)

    mid_i = get_mid_i(points_x)

    # points in point_x with x-coordinates less than or equal to mid_x
    left_x = points_x[:mid_i + 1]

    # points in point_x with x-coordinates greater than mid_x
    right_x = points_x[mid_i + 1:]

    # points in points_y with x-coordinates less than or equal to mid_x
    left_y = points_y[:mid_i + 1]

    # points in points_y with x-coordinates greater than mid_x
    right_y = points_y[mid_i + 1:]

    left_min_dist, left_min_pair = get_closest_pair(left_x, left_y)
    right_min_dist, right_min_pair = get_closest_pair(right_x, right_y)

    min_dist, min_pair = min((left_min_dist, left_min_pair), (right_min_dist, right_min_pair),
                             key=lambda point: point[0])

    close_to_line_points = get_close_to_line_points(points_y, min_dist, mid_x)

    for p in close_to_line_points:
        # compute distance between p and next 7 points in close_to_line_points
        for i in range(7):
            try:
                close_point = close_to_line_points[i]
                if close_point is not p:
                    close_distance = get_distance(p, close_point)
                    if close_distance < min_dist:
                        min_dist = close_distance
                        min_pair = (p, close_point)
            except IndexError:
                break
    return min_dist, min_pair


def get_next_7_points_distances(p: Tuple, closest_points: List[Tuple])->List[float]:
    """
    :param p:
    :param closest_points: points in points_y that are within min_dist of mid_x
    :return: distance between p and next 7 points in closest_points
    """
    result = []
    for i in range(7):
        try:
            dist = get_distance(p, closest_points[i])
            result.append(dist)
        except IndexError:
            break
    return result


def get_close_to_line_points(points_y: List[Tuple], min_dist: float, mid_x: float)->List[Tuple]:
    """
    :param points_y:
    :param min_dist: a distant that minimize (left distance, right distance)
    :param mid_x: the middle element in points_x
    :return: points in points_y that are within min_dist of mid_x
    """
    result = []
    for p in points_y:
        if abs(p[0] - mid_x) <= min_dist:
            result.append(p)
    return result


def get_distance(point_1: Tuple, point_2: Tuple)->float:
    """
    :param point_1: a point coordinate (x, y)
    :param point_2: a point coordinate (x, y)
    :return: the Euclidean distance between two pairs
    """
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def do_base_case(points: List[Tuple])->Tuple[float, Tuple]:
    """
    :param points:
    :return: return the smallest distance, smallest pair of points
    """
    # Computer all pairwise distance
    point_pairs = list(combinations(points, 2))
    point_distances = [get_distance(p[0], p[1]) for p in point_pairs]
    # Return the smallest distance & smallest pair of points
    min_dis = point_distances[0]
    min_pair = point_pairs[0]
    for i in range(len(point_distances)):
        if point_distances[i] <= min_dis:
            min_dis = point_distances[i]
            min_pair = point_pairs[i]
    return min_dis, min_pair


def get_mid_i(points: list)->int:
    """
    :points: a sorted list
    :return: the floor median index
    """
    return (len(points) - 1) // 2


def get_mid_x(points: list)->float:
    """
    :points: a sorted list
    :return: the item of floor median index in the list
    """
    mid_i = get_mid_i(points)
    return points[mid_i][0]

