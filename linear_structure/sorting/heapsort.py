import matplotlib.pyplot as plt

from heapq import heappop
from heapq import heappush
from visualizer import *

"""
Heapsort algorithm using the module `heapq`

Divide its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the 
largest element and moving that to the sorted region

Reference: 
https://docs.python.org/3.7/library/heapq.html
https://en.wikipedia.org/wiki/Heapsort
"""


def sort(iterable):
    h = []
    l = iterable

    plt.figure(1)
    display_list(l)

    plt.figure(2)
    display_heap(h)

    for value in iterable:
        # Display the list and heap
        plt.figure(1)
        plt.title("List")
        display_list(l)
        plt.figure(2)
        plt.title("Heap")
        display_heap(h)

        # remove an item from the list and push to the heap
        l = l[1:]
        heappush(h, value)

    plt.figure(1)
    display_list(l)
    plt.figure(2)
    display_heap(h)

    for i in range(len(h)):
        plt.figure(2)
        display_heap(h)
        plt.figure(1)
        display_list(l)

        value = heappop(h)
        l.append(value)

    plt.figure(2)
    display_heap(h)
    plt.figure(1)
    display_list(l)

    return l


if __name__ == "__main__":
    random_l = create_random_list(10)
    sorted_l = sort(random_l)
    print(sorted_l)
