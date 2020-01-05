from unittest import TestCase

from my_queue import Queue


class TestQueue(TestCase):
    def test_put(self):
        q = Queue()
        q.put(1)
        self.assertEqual([1], q.items)

    def test_get(self):
        q = Queue()
        q.put(1)
        i = q.get()
        self.assertEqual(1, i)
        with self.assertRaises(IndexError):
            i = q.get()

    def test_empty(self):
        q = Queue()
        self.assertTrue(q.empty())
        q.put(1)
        self.assertFalse(q.empty())

    def test_size(self):
        q = Queue()
        self.assertEqual(0, q.size())
        q.put(1)
        self.assertEqual(1, q.size())
