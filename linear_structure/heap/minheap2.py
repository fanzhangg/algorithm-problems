"""Heap queue algorithm (a. k. a. priority queue)

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.For the sake of comparison,
non-existing elements are considered to be infinite. The interesting
property of a heap is that a[0] is always its smallest elements

The API differs from textbook heap algorithm as follows:

- We use 0-base index.

- Our heappop() method returns the smallest item, not the largest.

These two make it possible to view the heap as a regular Python list
without surprise: heap[0] is the smallest item, and heap.sort()
maintains the heap invariant.
"""

import math

__about__ = """Heap queues
- remove the top item: 
  - remove index 0
  - find the next winner
    - move some loser into 0 position
    - percolate the new 0 down the tree
    - exchange values until the invariant is re-established
    
  - run time: O(nlog(n))

- insert:
  - run time: O(log(n))
  
- implications:
  - event scheduler
  - disk sorts
"""


def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _shiftdown(heap, 0, len(heap) - 1)


def _shiftdown(heap, startpos, pos):
    """

    :param heap:
    :param startpos:
    :param pos:
    :return:
    """
    pos = pos
    while pos > startpos:
        target = math.ceil(pos / 2) - 1
        if heap[pos] < heap[target]:
            heap[pos], heap[target] = heap[target], heap[pos]
            # update pos
            pos = target
        else:
            break


def heappop(heap):
    """
    Pop the smallest item off the heap, maintaining the heap invariant.
    :heap: a heap
    :return: a heap after poping the smallest item
    """
    if heap:
        returnitem = heap[0]
        heap = heap[1:]
        return returnitem
    else:
        raise IndexError
