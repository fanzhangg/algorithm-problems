import unittest

from list_graph import Graph


class TestListGraph(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.add_vertex(1)
        print(g)
        self.assertEqual(g.vert_list[1].value, 1)
        self.assertEqual(g.vert_num, 1)

    def test_get_vertex(self):
        g = Graph()
        g.add_vertex(1)
        self.assertEqual(g.get_vertex(1).value, 1)
        self.assertEqual(g.get_vertex(0), None)

    def test_add_edge(self):
        g = Graph()
        # g.add_vertex(1)
        g.add_edge(1, 2, 3)
        print(g)
        for e in g.edge_list:
            print(e)
        to_v = g.get_vertex(1).out_neighbors
        values, keys = to_v.values(), to_v.keys()
        self.assertEqual(list(keys)[0].value, 2)
        self.assertEqual(list(values)[0], 3)

    def test_add_undirected_edge(self):
        g = Graph()
        g.add_undirected_edge(1, 2, 3)
        print(g)
        for e in g.edge_list:
            print(e)


    def test_str(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(1, 2)
        print(g)


if __name__ == '__main__':
    unittest.main()
