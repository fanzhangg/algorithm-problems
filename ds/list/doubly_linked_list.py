class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation
    """

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node"""
        __slots__ = "_element", "_prev", "_next"  # Streamline memory

        def __init__(self, element, prev, next):
            """
            Initialize node's field
            :param element:
            :param prev: previous element
            :param next: next element
            """
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # Trailer is after header
        self._trailer._prev = self._header  # Header is before trailer
        self._size = 0  # Number of elements

    def __len__(self):
        """
        :return: the number of elements in the list
        """
        return self._size

    def is_empty(self):
        """
        :return: True if list is empty
        """
        return self._size == 0

    def _insert_between(self, e, predecessor: _Node, successor: _Node):
        """
        Add element e between exisiting nodes
        :return: new node
        """
        newest = self._Node(e, predecessor, successor)  # Linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node: _Node):
        """
        Delete non-sentinel node from the list
        :return: its element
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # Record deleted elemnt
        node._prev = node._next = node._element = None  # Deprecate node
        return element

