"""
Given: n sound recordings of either A or B, m judgements ("same" or "different")
Return: True if data is consistent. False if not.

* judgments:
For each pair of recordings (i, j):
- label "same" or "different" or "ambiguous

* inconsistent if exist (i, j) labeled same, i and j have the different label or (i, j)
labeled different, i and j have the same label.
"""

from list_graph import Graph
from list_graph import Vertex
import my_queue


def get_graph(judgments: list, recordings: list)->Graph:
    g = Graph()
    for r in recordings:
        g.add_vertex(r)
    for j in judgments:
        v1, v2, weight = j
        g.add_undirected_edge(v1, v2, weight)
    return g


def color_nodes_in_subgraph(s: Vertex):
    s.color = "r"
    q = my_queue.Queue()
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in u.get_out_neighbors():
            if not v.color:
                q.put(v)
                if u.get_weight(v) == 1:
                    if u.color == "r":
                        v.color = "b"
                    else:
                        v.color = "r"
                else:
                    if u.color == "r":
                        v.color = "r"
                    else:
                        v.color = "b"


def color_all_nodes(g: Graph):
    for v_key in g.get_vertices():
        v = g.get_vertex(v_key)
        if not v.color:
            color_nodes_in_subgraph(v)


def test_consistency(g:Graph)->bool:
    for edge in g.edge_list:
        v_1 = edge.from_v
        v_2 = edge.to_v
        weight = edge.weight
        if weight == 1:
            print(edge)
            print(v_1.color)
            print("v2:", v_2)
            print("v2 color:", v_2.color)
            if v_1.color == v_2.color:
                return False
        else:
            print(edge)
            print(v_1.color)
            print(v_2.color)
            if not v_1.color == v_2.color:
                return False
    return True

