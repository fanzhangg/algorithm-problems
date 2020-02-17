from ds.list.doubly_linked_list import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""

    class Position:
        """An abstraction representing the location of a single element"""
        def __init__(self, container, node):
            """Warning: constructor not invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """
            :return: the element stored at this Position
            """
            return self._node._element

        def __eq__(self, other):
            """
            :return: True if other is a Position representing the same location
            """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """
            :return: Trye if other does not represent the same location
            """
            return not (self == other)

    # Utility method

    def _validate(self, p):
        """
        :return: position's node, or raise appropriate error if invalid
        """
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to the container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """
        :return: Position instance for given node, or None if sentinel
        """
        if node is self._header or node is self._trailer:
            return None # Boundary violation
        else:
            return self.Position(self, node)    # Legitimate postion

    # Accessors

    def first(self):
        """
        :return: the first Position in the list, or None if list is empty
        """
        return self._make_position(self._header._next)

    def last(self):
        """
        :return: the last Position in the list, or None if list is empty
        """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """
        :param: p: Position
        :return: the Position just before Position p, or None if p is first
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        :param: p: Position
        :return: the Position after Position p, or None if p is last
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """
        :yield: a forward iteration of teh element of the list
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after()

    def _insert_between(self, e, predecessor, successor):
        """
        Override function to return Position
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        Insert element e at the front of the list
        :param e: element
        :return: new position
        """
        return self._insert_between(e, self._header, self._trailer)

    def add_last(self, e):
        """
        Insert element e at the back of the list
        :param e: element
        :return: new position
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """
        Insert element e into list before Position p
        :param p: Position
        :param e: element
        :return: new Position
        """
        origin = self._validate(p)
        return self._insert_between(e, origin._prev, origin)

    def add_after(self, p, e):
        """
        Insert element e into list after Position p
        :param p:
        :param e:
        :return: new Position
        """
        origin = self._validate(p)
        return self._insert_between(e, origin, origin._next)

    def delete(self, p):
        """
        Remove the element at Position p
        :param p: Position
        :return: the element at Position p
        """
        origin = self._validate(p)
        return self._delete_node(origin)

    def replace(self, p, e):
        """
        Replace the element at Position p with e
        :param p: Position
        :param e: element
        :return: The element formerly at Position p
        """
        origin = self._validate(p)
        old_value = origin._element
        origin._element = e
        return old_value
