from ds.tree.tree import Tree


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

    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.inorder()

    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p"""
        left = self.left(p)
        if left:
            for other in self._subtree_inorder(left):
                yield other

        yield p

        right = self.right(p)
        if right:
            for other in self._subtree_inorder(right):
                yield other
