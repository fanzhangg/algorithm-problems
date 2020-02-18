from ds.list.positional_list import PositionalList


class FavoritesList:
    """List of elements ordered from most frequently accessed to least"""
    class _Item:
        __slots__ = "_value", "_count"

        def __init__(self, e):
            self._value = e     # The user's element
            self._count = 0     # Access count initially 0

    # Non-public utilities
    def _find_position(self, e):
        """
        Search for element
        :return: its Position, or None if not found
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """
        Move item at Position p earlier in the list based on access count
        :param p: Position
        """
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count: # shift forward
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # Public methods
    def __init__(self):
        """Create an empty list favorite"""
        self._data = PositionalList()

    def __len__(self):
        """
        :return: number of entries on favorites list
        """
        return len(self._data)

    def is_empty(self):
        """
        :return: True if the list is empty
        """
        return len(self._data) == 0

    def access(self, e):
        """
        Access element e, thereby increasing its access count
        :param e: Element
        """
        p = self._find_position(e)  # Try to locate existing element
        if p is not None:
            self._data.delete(p)    # Delete if found

    def top(self, k):
        """
        Generate sequence of top k elements in terms of access count
        :param k: int
        :return:
        """
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()   # Element of list
            yield item._value
            walk = self._data.after(walk)
