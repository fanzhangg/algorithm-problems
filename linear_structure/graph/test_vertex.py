import unittest

import list_graph


class MyTestCase(unittest.TestCase):
    def test_add_neighbor(self):
        v = list_graph.Vertex(1)
        v.add_out_neighbor(2, 5)
        v.add_out_neighbor(3, 3)
        self.assertEqual(v.out_neighbors, {2: 5, 3: 3})

    def test_get_connections(self):
        v = list_graph.Vertex(1)
        v.add_out_neighbor(2, 5)
        v.add_out_neighbor(3, 3)
        self.assertEqual([i for i in v.get_out_neighbors()], [2, 3])

    def test_get_weight(self):
        v = list_graph.Vertex(1)
        v.add_out_neighbor(2, 5)
        v.add_out_neighbor(3, 3)
        self.assertEqual(v.get_weight(2), 5)

    def test_str(self):
        v0 = list_graph.Vertex(0)
        v1 = list_graph.Vertex(1)
        v2 = list_graph.Vertex(2)
        v1.add_out_neighbor(v2)
        v1.add_in_neighbor(v0)
        print(v1)


if __name__ == '__main__':
    unittest.main()
