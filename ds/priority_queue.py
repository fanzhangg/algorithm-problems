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
