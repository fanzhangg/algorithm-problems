import math

"""
given: n points in the plane, each specified by (x, y) coordinates
output: the pair of points that are closest together.
"""


def get_distance(a, b)->float:
    x_diff = b[0] - a[0]
    y_diff = b[1] - a[1]
    return math.sqrt(x_diff**2 + y_diff**2)


def find_closest_points_pair(l: list)->float:
    closest_distance = get_distance(l[0], l[1])
    for x in l:
        for y in l:
            if not x == y:
                distance = get_distance(x, y)
                if distance < closest_distance:
                    closest_distance = distance
    return closest_distance


if __name__ == "__main__":
    points = [(0, 0), (1, 0), (10, 10)]
    closest_distance = find_closest_points_pair(points)
    print(closest_distance)
