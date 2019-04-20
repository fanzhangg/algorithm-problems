from typing import List


class Item(object):
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight


def knapsack(max_weight: int, items: List[Item])->int:
    """
    :param max_weight: the capacity of knapsack (W > 0)
    :param items: n items, each item has a weight > 0 and a value >0
    :return: a set of items, such as the total weights <= W, and the total value is maximized
    """
    # a matrix opt[items size(0,...,n)[weight(0, ..., total_weight]]
    opt = [[-1 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]
    for w in range(max_weight + 1):
        opt[0][w] = 0
    for i in range(1, len(items) + 1):
        for w in range(max_weight + 1):
            if items[i - 1].weight > w:
                opt[i][w] = opt[i - 1][w]
            else:
                opt[i][w] = max(opt[i - 1][w], items[i - 1].value + opt[i - 1][w - items[i - 1].weight])
    return opt[-1][-1]
