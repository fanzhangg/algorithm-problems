from queue import Queue

class Tree:
    """
    Abstract base class representing a trees structure
    """
    class Position:
        """
        An abstraction representing the location of a single element
        """
        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("Must be implemented by a subclass")

        def __eq__(self, other):
            """Return True if other represents the same location"""
            raise NotImplementedError("Must be implemented by a subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)

    def root(self):
        """Return position representing the trees's root, or None if empty"""
        raise NotImplementedError("Must be implemented by a subclass")

    def parent(self, p):
        """Return Position representing p's parent, or None if p is root"""
        raise NotImplementedError("Must be implemented by a subclass")

    def num_children(self, p):
        """Return the number of children that Position p has"""
        raise NotImplementedError("Must be implemented by a subclass")

    def children(self, p):
        """Generate an iteration of Position representing p's children"""
        raise NotImplementedError("Must be implemented by a subclass")

    def __len__(self):
        """Return the total number of element in the trees"""
        raise NotImplementedError("Must be implemented by a subclass")

    # Methods implemented in this class
    def is_root(self, p):
        """Return True if Position p represents the root of the trees"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p represents the leaf of the trees / does not have any children"""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the trees is empty"""
        return len(self) == 0

    def positions(self):
        """Return all postions of the tree"""
        return self.preorder()

    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p  # Visit p before its subtrees
        for c in self.children(p):  # For each child:
            for other in self._subtree_preorder(c):  # Do preorder of c's subtree
                yield other    # Yield each to our caller

    def postorder(self):
        """Generate a postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p"""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadth_first(self):
        queue = Queue()
        queue.put(self.root())
        while not queue.empty():  # Queue is not empty
            p = queue.get()
            yield p
            for child in self.children(p):
                queue.put(child)

