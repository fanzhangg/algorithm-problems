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

    def __len___(self):
        """Return the total number of element in the trees"""
        raise NotImplementedError("Must be implemented by a subclass")

    # Methods implemented in this class
    def is_root(self, p):
        """Return True if Position p represents the root of the trees"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p represents the leaf of the trees / does not have any children"""
        return self.num_children == 0
    
    def is_empty(self):
        """Return True if the trees is empty"""
        return len(self) == 0
