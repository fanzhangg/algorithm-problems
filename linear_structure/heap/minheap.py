"""Heap queue algorithm inspired by the source code of heapq

Reference: https://docs.python.org/3.7/library/heapq.html

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

__name__ = ["heappush", "heappop", "_siftup", "_siftdown"]

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
    _siftdown(heap, 0, len(heap) - 1)


def heappop(heap):
    """Pop the smallest item off the heap, maingtaining the heap invariant."""
    lastelt = heap.pop()  # raise appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def _siftup(heap, pos):
    """
    If the child indices of heap index pos are already heaps, and we want to make
    a heap at index pos too. We do this by bubbling the smaller child of pos up
    (and so on with that child's children, etc) until hitting a leaf, then using
    _siftdown to move the item originally at index pos into place.
    :heap: a heap whose children are heaps but the item at index pos is not variant
    :pos: the position of an invariant item
    :return: a variant heap
    """
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        # Right child exists and is the smaller child.
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now. Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def _siftdown(heap, startpos, pos):
    """Restore the heap invariant.
    :param heap:  a heap at all indices >= startpos, except possibly for pos
    :param startpos: the start position of the returned heap
    :param pos: the index of a leaf with a possibly out-of-order value
    :return: a variant heap
    """
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if parent > newitem:
            # shift up parent to the position of newitem
            heap[pos] = parent
            pos = parentpos
            continue
        break
    # add the newitem to position of the last parent > newitem
    heap[pos] = newitem
