from typing import List


def min_stops(dists: List[int], max_walk: int):
    """
    :param dists: a list of distances between the current stop and the former stop
    :param max_walk: the person can travel at most x miles per time
    :return: the stops minimize the number of stops
    :idea: choose stop i such as maximize valid (dists[i] - dists[i-1]); a stop i is valid if d[i] - d[i-1] <= max_walk
    """
    selected_stops = []
    # do we assume a valid solution always exist?
    # is stop n Kholinar?
    walk_dist = 0

    for i in range(0, len(dists)):
        if dists[i] > max_walk:
            return None
            # the former stop is the valid stop max(dists[i] - dists[i -1])
        else:
            walk_dist += dists[i]

        if walk_dist > max_walk:
            selected_stops.append(i - 1)
            walk_dist = dists[i]
    return selected_stops
