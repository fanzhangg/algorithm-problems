from typing import List


def min_stops(dists: List[int], max_walk: int):
    """
    :param dists: a list of distances between the current stop and the former stop, let the start stop be stop 0
    :param max_walk: miles per time of the maximum traveling distance
    :return: the indices of stops minimize the number of stops
    :idea: choose stop i such as maximize valid (dists[i] - dists[i-1]); a stop i is valid if d[i] - d[i-1] <= max_walk
    """
    selected_stops = []
    walk_dist = 0

    for i in range(len(dists)):
        if dists[i] > max_walk:
            return None
            # the former stop is the valid stop max(dists[i] - dists[i -1])
        else:
            walk_dist += dists[i]

        if walk_dist > max_walk:
            print(dists[i])
            selected_stops.append(i)
            walk_dist = dists[i]
    return selected_stops
