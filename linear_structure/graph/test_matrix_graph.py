import unittest

from matrix_graph import Graph


class TestMatrixGraph(unittest.TestCase):
    def test_init(self):
        g = Graph(2)
        self.assertEqual(g.size, 2)
        self.assertEqual(g.matrix, [[0, 0], [0, 0]])

    def test_add_edge(self):
        g = Graph(2)
        g.add_edge(0, 1)
        self.assertEqual(g.matrix, [[0, 1], [0, 0]])

    def test_remove_edge(self):
        g = Graph(2)
        g.add_edge(0, 1)
        g.remove_edge(0, 1)
        self.assertEqual(g.matrix, [[0, 0], [0, 0]])

    def test_contains_edge(self):
        g = Graph(2)
        g.add_edge(0, 1)
        self.assertTrue(g.contains_edge(0, 1))
        self.assertFalse(g.contains_edge(0, 0))

    def test_len(self):
        g = Graph(2)
        self.assertEqual(len(g), 2)

    def test_str(self):
        g = Graph(2)
        print(g)


if __name__ == '__main__':
    unittest.main()
