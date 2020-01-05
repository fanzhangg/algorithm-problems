import unittest
from bird_sounds import *


class TestBirdSounds(unittest.TestCase):
    def test_get_graph(self):
        recordings = [0, 1, 2, 3, 4]
        judgments = [[0, 1, 1], [0, 2, -1], [1, 2, 1], [1, 3, 1], [2, 3, -1]]
        g = get_graph(judgments, recordings)

    def test_color_nodes_in_subgraph(self):
        recordings = [0, 1, 2, 3, 4]
        judgments = [[0, 1, 1], [0, 2, -1], [1, 2, 1], [1, 3, 1], [2, 3, -1]]
        g = get_graph(judgments, recordings)
        start = g.get_vertex(0)
        color_nodes_in_subgraph(start)
        # print(g)

    def test_color_all_nodes(self):
        recordings = [0, 1, 2, 3, 4]
        judgments = [[0, 1, 1], [0, 2, -1], [1, 2, 1], [1, 3, 1], [2, 3, -1]]
        g = get_graph(judgments, recordings)
        start = g.get_vertex(0)
        color_nodes_in_subgraph(start)
        color_all_nodes(g)
        print(g)
        v_4 = g.get_vertex(4)
        self.assertEqual("r", v_4.color)

    def test_test_consistency(self):
        recordings = [0, 1, 2, 3, 4]
        judgments = [[0, 1, 1], [0, 2, -1], [1, 2, 1], [1, 3, 1], [2, 3, -1]]
        g = get_graph(judgments, recordings)
        color_all_nodes(g)
        print(g)
        consist = test_consistency(g)
        print(consist)


if __name__ == '__main__':
    unittest.main()
