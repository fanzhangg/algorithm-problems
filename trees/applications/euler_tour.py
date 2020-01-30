from trees.tree import Tree


class EulerTour:
    """
    Abstract base class for performing Euler tour of a tree
    _hook_previsit and _hook_positive may be overridden by subclasses
    """
    def __init__(self, tree):
        """Prepare an Euler tour template for given tree"""
        self._tree = tree

    def tree(self)->Tree:
        """
        :return: reference to the tree being traversed
        """
        return self._tree

    def execute(self):
        """
        Perform the tour
        :return: result from post visit of root
        """
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, pos: Tree.Position, dep: int, path: [int]):
        """
        Perform tour of subtree rooted at Position p
        :param pos: Position of current node being visited
        :param dep: Depth of `pos` in the tree
        :param path: List of indices of children on path from root to `pos`
        """
        self._hook_previsit(pos, dep, path)     # Previsit
        results = []
        path.append(0)      # Add new index to end of path before recursion
        for c in self._tree.children(pos):
            results.append(self._tour(c, dep + 1, path))    # Recursion on the children's subtree
            path[-1] += 1   # Increment index
        path.pop()
        ans = self._hook_postvisit(pos, dep, results)  # post visit p
        return ans

    def _hook_previsit(self, pos: Tree.Position, dep: int, path: [int]):
        """Can be overridden"""
        pass

    def _hook_postvisit(self, pos: Tree.Position, dep: int, path: [int]):
        """Can be overridden"""
        pass


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, pos: Tree.Position, dep: int, path: [int]):
        print(2 * dep * " " + str(pos.element()))


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, pos: Tree.Position, dep: int, path: [int]):
        if path and path[-1] > 0:
            print(", ", end="")
        print(pos.element(), end="")
        if not self.tree().is_leaf(pos):
            print(" (", end="")

    def _hook_postvisit(self, pos: Tree.Position, dep: int, path: [int]):
        if not self.tree().is_leaf(pos):
            print(")", end="")
