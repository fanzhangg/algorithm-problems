from unittest import TestCase

from breadth_first_search import bfs
from list_graph import Graph


class TestBfs(TestCase):
    def test_bfs(self):
        g = Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        start = g.get_vertex(0)
        bfs(start)
        print(g)
