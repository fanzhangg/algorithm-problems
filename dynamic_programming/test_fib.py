import unittest
from fibonnaci import memoized_fib as fib


class FibTest(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(0, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(1, fib(2))
        self.assertEqual(2, fib(3))
        self.assertEqual(3, fib(4))
        self.assertEqual(5, fib(5))


if __name__ == '__main__':
    unittest.main()
