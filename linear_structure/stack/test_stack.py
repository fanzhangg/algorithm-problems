from unittest import TestCase

from stack.stack import *


class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual([1], stack.items)
        stack.push(2)
        self.assertEqual([1, 2], stack.items)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.peek())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())

    def test_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.size())

    def test_isempty(self):
        stack = Stack()
        self.assertTrue(stack.isempty())
        stack.push(1)
        self.assertFalse(stack.isempty())
