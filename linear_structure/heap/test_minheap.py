import unittest

from heap import minheap as minheap


class MyTestCase(unittest.TestCase):
    def test_siftdown(self):
        heap1 = [1, 5, 8, 10, 11, 6]
        minheap._siftdown(heap1, 0, len(heap1) - 1)
        self.assertEqual(heap1, [1, 5, 6, 10, 11, 8])

        heap2 = [3, 4, 5, 6, 7, 1]
        minheap._siftdown(heap2, 0, len(heap2) - 1)
        self.assertEqual(heap2, [1, 4, 3, 6, 7, 5])

    def test_heappush(self):
        heap1 = [1, 5, 8, 10, 11]
        minheap.heappush(heap1, 6)
        self.assertEqual(heap1, [1, 5, 6, 10, 11, 8])

        # test the case when the item will be shifted down to index 0
        heap2 = [3, 4, 5, 6, 7]
        minheap.heappush(heap2, 1)
        self.assertEqual(heap2, [1, 4, 3, 6, 7, 5])

    def test_siftup(self):
        heap1 = [1, 2, 3, 4, 5]
        minheap.heappop(heap1)
        self.assertEqual([2, 4, 3, 5], heap1)


if __name__ == '__main__':
    unittest.main()
