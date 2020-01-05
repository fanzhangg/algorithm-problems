from visualizer import *

"""
The insertion sort algorithm sorts an unordered list by stepping through the list, removing the unordered item, and then 
shuffle the other items forward in the list until the correct position is found for the removed item
"""


def sort(l: list) -> list:
    for i in range(1, len(l)):
        # move the item down the list until the item to its left is smaller than it
        # i > 0 in case of i is out of range
        while i > 0 and l[i - 1] > l[i]:
            l[i], l[i - 1] = l[i - 1], l[i]
            display(l, i, i - 1)
            i -= 1
    return l


if __name__ == "__main__":
    random_l = create_random_list(10)
    sort(random_l)
    plt.show()
    plt.pause(100)
