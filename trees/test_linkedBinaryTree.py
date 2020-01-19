from unittest import TestCase
from trees.linked_binary_tree import LinkedBinaryTree


class TestLinkedBinaryTree(TestCase):
    def test__validate(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)

    def test__make_position(self):
        pass

    def test_root(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        self.assertEqual(0, root.element())

    def test_parent(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_left(root, 1)
        left = tree.left(root)
        parent = tree.parent(left)
        self.assertEqual(parent, root)

    def test_left(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_left(root, 1)
        left = tree.left(root)
        self.assertEqual(1, left.element())

    def test_right(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_right(root, 1)
        right = tree.right(root)
        self.assertEqual(1, right.element())

    def test_num_children(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_right(root, 1)
        tree._add_left(root, 2)

        self.assertEqual(2, tree.num_children(root))

    def test__add_root(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()
        self.assertEqual(0, root.element())

    def test__add_left(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_left(root, 1)
        left = tree.left(root)
        self.assertEqual(1, left.element())

    def test__add_right(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_right(root, 1)
        right = tree.right(root)
        self.assertEqual(1, right.element())

    def test__replace(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_right(root, 1)

        tree._replace(root, 6)

        root = tree.root()
        self.assertEqual(root.element(), 6)

        right = tree.right(root)
        self.assertEqual(right.element(), 1)

    def test__delete(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_right(root, 1)

        tree._delete(root)

        root = tree.root()
        self.assertEqual(root.element(), 1)

        self.assertTrue(tree.is_root(root))

    def test__attach(self):
        tree = LinkedBinaryTree()
        tree._add_root(0)
        root = tree.root()

        tree._add_right(root, 1)

        right = tree.right(root)

        tree1 = LinkedBinaryTree()
        tree1._add_root(2)

        tree2 = LinkedBinaryTree()
        tree2._add_root(3)

        tree._attach(right, tree1, tree2)

        right = tree.right(root)
        e1 = tree.left(right)
        e2 = tree.right(right)

        self.assertEqual(2, e1.element())
        self.assertEqual(3, e2.element())
