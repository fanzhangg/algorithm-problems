from ds.tree.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary trees structure"""

    class _Node:
        """Private class for storing a node"""
        __slot__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            """Return Ture if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p: Position) -> _Node:
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # Convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node: _Node) -> Position or None:
        """Return Position instance for given node, or None if no node"""
        if node is not None:
            return self.Position(self, node)
        else:
            return None

    # Binary trees constructor
    def __init__(self):
        """Create an initially empty binary trees"""
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self)->Position or None:
        """:return: the root Position of the trees, or None if trees is empty"""
        return self._make_position(self._root)

    def parent(self, p: Position)->Position or None:
        """:return: the Position of p's parent, or None if p is root"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p: Position)->Position or None:
        """:return: the position of p's left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p: Position)->Position or None:
        """:return: the position of p's right child"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p: Position) -> int:
        """:return: the number of children of Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:  # Left child exists
            count += 1
        if node._right is not None:  # Right child exists
            count += 1
        return count

    def _add_root(self, e: any) -> Position:
        """
        Place element e at the root of an empty trees and return new Position
        Riase ValueError if trees nonempty
        """
        if self._root is not None:
            raise ValueError("Root exists. Cannot add root.")
        self._root = self._Node(e)
        self._size = 1

        return self._make_position(self._root)

    def _add_left(self, p: Position, e: any)->Position:
        """
        Create a new left child for Position p, storing element e
        :param p: Parent position
        :param e: Element of child node
        :return: Position of the new node
        :raise: ValueError if Position p is invalid or p already has a left child
        """
        node = self._validate(p)    # Check if position p is valid
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)    # Node is its parent
        return self._make_position(node._left)

    def _add_right(self, p: Position, e: any)->Position:
        """
        Create a new right child for Position p, storing element e
        :param p: Parent position
        :param e: Element of child node
        :return: Position of the new node
        :raise: ValueError if Position p is invalid or p already has a right child
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)   # Node is its parent
        return self._make_position(node._right)

    def _replace(self, p: Position, e: any)->Position:
        """
        Replace the element at position p with e, and return old element
        :param p: Position
        :param e: New element
        :return: Old element
        """
        node = self._validate(p)

        old = node._element
        node._element = e
        return old

    def _delete(self, p: Position)->any:
        """
        Delete the node at Position p, and replace it with its child
        :param p: Position
        :return: The element that had been stored at Position p
        :raise: ValueError if Position p is invalid or p has 2 children
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has 2 children")
        if node._left:
            child = node._left
        else:
            child = node._right

        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node  # Deprecate node
        return node._element

    def _attach(self, p: Position, t1, t2):
        """
        Attach tree t1 and t2 as left and right subtrees of external p
        :param p: Position
        :param t1: BinaryTree
        :param t2: BinaryTree
        :return: None
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Position must be a leaf")
        if not type(self) is type(t1) and type(t2):
            raise ValueError("Tree types must be match")
        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None # Set t1 instance to empty
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

