from typing import List, Tuple
from knapsack import knapsack, Item


def get_max_object_copies(items: List[Item], max_weight)->List[Item]:
    """
    :param items: a list of item, each has a name and a weight
    :param max_weight: the capacity of the warehouse
    :return: a list of item copies, number of copies of each item is maximized
    """
    copies = []
    for i in items:
        num = max_weight // i.weight
        for _ in range(num):
            copies.append(i)
    return copies


def warehouse(max_weight: int, items: List[Item])->Tuple[int, set]:
    """
    :param max_weight: the capacity of the warehouse
    :param items: a list of item, each has a name and a weight
    :return: a set of items, two item can be the same, the total weights <= W, and the total name is maximized
    """
    copies = get_max_object_copies(items, max_weight)
    return knapsack(max_weight, copies)
