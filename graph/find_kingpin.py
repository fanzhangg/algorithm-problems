"""
Given: $n$ gang members exchange money. An edge u -> v means u paid money to v.
Output: If there is a kingpin, return kingpin. Else return None.

* Kingpin is a person who has received money from all n-1 other people in the gang
and has not given any moeny to anyone else. (a node with indegree n - 1 and outgree 0.)
"""

from matrix_graph import Graph


def find_best(g: Graph):
    """Find the best candidate of kingpin"""
    best = g.get_node(0)
    for v in g.nodes[1:]:
        if not g.contains_edge(v, best) or g.contains_edge(best, v):
            best = v
    return best


def test_best(best, g: Graph):
    """
    Test if the best candidate is kingpin
    :return: best if best is kingpin, None if best is not
    """
    for v in g.nodes:
        if v is not best:
            if not g.contains_edge(v, best) or g.contains_edge(best, v):
                return None
    return best

