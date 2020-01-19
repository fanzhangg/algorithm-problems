from trees.tree import Tree


class BinaryTree(Tree):
    """Abstract class representing a binary trees structure"""
    def left(self, p):
        """
        Return a Position representing p's left child
        Return None if p does not have a left child
        """
        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        """
        Return a Position representing p's right child
        Return None if p does not have a right child
        """
        raise NotImplementedError("Must be implemented by subclass")

    def sibling(self, p):
        """
        Return a Position representing p's sibling
        Return None if no sibling
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if self.left(parent): # Could be None
                return self.right(parent)
            else:   # Could be None
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Position representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.left(p) is not None:
            yield self.right(p)
