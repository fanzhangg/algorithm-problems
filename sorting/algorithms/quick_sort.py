from collections import deque
"""
Use divide-and-conquer technique:
- Divide S into subsequences
  - Select pivot x as last element
  - L: S < x
  - E: S = x
  - G: S > x
- Recur to sort each subsequence
- Combine the sorted subsequences
"""


def quck_sort(s: deque):
    """
    Sort the elements of queue S using quick-sort algorithm
    :param s:
    :return:
    """
    n = len(s)
    if n < 2:   # List is sorted
        return

    # p = s.
    # l = PriorityQueue()
    # e = Queue()
    # g = Queue()
    #
    # while not s.empty():    # divide s into l, e, g
    #     if s.get() < p:
