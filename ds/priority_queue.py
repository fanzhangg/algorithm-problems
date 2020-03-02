from ds.list.positional_list import PositionalList


class PriorityQueueBase:
    """Abstract base class for a priority queue"""
    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            """
            Compare items based on their keys
            :param other: the other item
            """
            return self._key < other._key

    def is_empty(self):
        """
        :return: True if the priority queue is empty
        """
        return len(self) == 0


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list"""

    def __init__(self):
        """
        Create a new empty priority queue
        """
        self._data = PositionalList()

    def __len__(self):
        """
        :return: the number of items in the priority queue
        """
        return len(self._data)

    def add(self, key, value):
        """
        Add a key-value pair
        """
        newest = self._Item(key, value)
        walk = self._data.last()   # Walk backward for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)   # New key is the smallest
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """
        :return: (k, v) tuple with minimum key (not remove)
        """
        if self.is_empty():
            raise LookupError("Priority queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove the (k, v) tuple with minimum key
        :return: (k, v) tuple with minimum key
        """
        if self.is_empty():
            raise LookupError("Priority queue is empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""
    # Private methods
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # Check if index > end of list

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):  # Check if right is smaller
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child) # Recur at position of small child

    def _heapify(self):
        start = self._parent(len(self) - 1)     # Start at parent pf last leaf
        for j in range(start, -1, -1):  # Going to and including the root
            self._downheap(j)

    # Public methods
    def __init__(self, contents=()):
        """Create a new empty priority queue"""
        self._data = [self._Item(k, v) for k, v in contents]     # Empty by default
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        """
        :return: the number of items in the priority queue
        """
        return len(self._data)

    def add(self, key, value):
        """
        Add a key-value pair to priority queue
        :param key:
        :param value:
        :return:
        """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)   # Upheap newly added position

    def min(self):
        """
        :return: (k, v) tuple with minimum key (do not remove)
        :raise KeyError exception if it is empty
        """
        if self.is_empty():
            raise KeyError("Priority queue is empty")
        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        """
        Remove the (k, v) tupe with minimum key
        :return: the (k, v) tupe with minimum key
        :raise KeyError exception if it is empty
        """
        if self.is_empty():
            raise KeyError("Priority queue is empty")
        self._swap(0, len(self._data) - 1)  # Put the minimum item at the end
        item = self._data.pop() # Remove it from the list
        self._downheap(0)   # Fix new root
        return item._key, item._value
