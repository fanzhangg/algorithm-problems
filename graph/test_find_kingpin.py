import unittest
from matrix_graph import Graph
from find_kingpin import *


class TestFindKingpin(unittest.TestCase):
    nodes = [0, 1, 2, 3]
    g = Graph(nodes)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(3, 1)
    g.add_edge(3, 2)

    def test_g(self):
        print(self.g)

    def test_get_best(self):
        best = find_best(self.g)
        self.assertEqual(best, 2)

    def test_kingpin(self):
        best = find_best(self.g)
        kingpin = test_best(best, self.g)
        self.assertEqual(kingpin, 2)

    def test_no_kingpin(self):
        nodes = [0, 1, 2, 3]
        g = Graph(nodes)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(3, 1)
        g.add_edge(3, 2)

        best = find_best(g)
        self.assertEqual(best, 2)

        kingpin = test_best(best, g)
        self.assertIsNone(kingpin)


if __name__ == '__main__':
    unittest.main()
