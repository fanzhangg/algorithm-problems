from unittest import TestCase
from trees.linked_binary_tree import LinkedBinaryTree
from trees.applications.euler_tour import PreorderPrintIndentedTour, ParenthesizeTour


class TestEulerTour(TestCase):
    def test_PreorderPrintIndentedTour(self):
        t = LinkedBinaryTree()
        root = t._add_root("Data Structure")
        left = t._add_left(root, "Tree")
        t._add_right(root, "List")

        t._add_left(left, "Array Tree")
        right = t._add_right(left, "Linked Tree")

        t._add_left(right, "Binary Tree")
        t._add_right(right, "RB Tree")

        et = PreorderPrintIndentedTour(t)
        et.execute()

    def test_ParenthesizeTour(self):
        t = LinkedBinaryTree()
        root = t._add_root("Data Structure")
        left = t._add_left(root, "Tree")
        t._add_right(root, "List")

        t._add_left(left, "Array Tree")
        right = t._add_right(left, "Linked Tree")

        t._add_left(right, "Binary Tree")
        t._add_right(right, "RB Tree")

        et = ParenthesizeTour(t)
        et.execute()
