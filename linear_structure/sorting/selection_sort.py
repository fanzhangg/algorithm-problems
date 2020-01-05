from visualizer import *

"""
The selection sort algorithm steps through an unordered list, keeping tack of the smallest value it encounters,
and once it has iterated through the entire list, it moves this value to the start of the list.
The repeated until the list is sorted
"""


def sort(l: list) -> list:
    for i in range(len(l)):
        min_num = l[i]
        min_index = i
        # get the minimum number and its index
        for j in range(i + 1, len(l)):
            if l[j] < min_num:
                min_num = l[j]
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
        display(l, i, min_index)
    return l


if __name__ == "__main__":
    random_l = create_random_list(10)
    sort(random_l)
