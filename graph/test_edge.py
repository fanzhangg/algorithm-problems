import unittest
from list_graph import Edge


class TestEdge(unittest.TestCase):
    def test_from_v(self):
        edge = Edge(0, 1, 1)
        self.assertEqual(0, edge.from_value)
        self.assertEqual(1, edge.to_value)

    def test_str(self):
        edge = Edge(0, 1, 1)
        self.assertEqual("(0)--1-->(1)", str(edge))


if __name__ == '__main__':
    unittest.main()
