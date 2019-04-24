from typing import List, Tuple


class Item(object):
    def __init__(self, name: str, value: int, weight: int):
        self.name = name
        self.value = value
        self.weight = weight

    def __str__(self):
        return self.name


def knapsack(max_weight: int, items: List[Item])->Tuple[int, set]:
    """
    :param max_weight: the capacity of knapsack (W > 0)
    :param items: n items, each item has a weight > 0 and a name >0
    :return: a set of items, such as the total weights <= W, and the total name is maximized
    """
    # a matrix opt[items size(0,...,n)[weight(0, ..., total_weight]]
    opt = [[-1 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]
    item_sets = [[set() for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]

    for w in range(max_weight + 1):
        opt[0][w] = 0

    for i in range(1, len(items) + 1):
        for w in range(max_weight + 1):
            if items[i - 1].weight > w:
                opt[i][w] = opt[i - 1][w]
                item_sets[i][w] = item_sets[i - 1][w]
            else:
                if opt[i - 1][w] >= items[i - 1].value + opt[i - 1][w - items[i - 1].weight]:
                    opt[i][w] = opt[i - 1][w]
                    item_sets[i][w] = item_sets[i - 1][w]
                else:
                    opt[i][w] = items[i - 1].value + opt[i - 1][w - items[i - 1].weight]
                    item_set = item_sets[i - 1][w - items[i - 1].weight].copy()
                    item_set.add(items[i - 1].name)
                    item_sets[i][w] = item_set
    return opt[-1][-1], item_sets[-1][-1]

