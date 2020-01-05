"""Represent a graph G={V,E} as a matrix of booleans"""

__about__ = """
The size of the matrix is V*V where V is the number of vertices in the graph
The value of an entry Aij is either 1 if there is an edge from vi to vj or 0 if there is not.

- matrix is symmetric in case of undirected graph

Pros:
- O(1) to remove / check an edge
- First choice if the graph is dense and the number of edges is large
- If the matrix is sparse, represent it using data structures for sparse matrix
- Get important insights into the nature of the graph and the relationship between its vertices

Cons
- V*V space takes lots of memory
- Adjacency list is the first choice if the graphs don't have many edges
- Operations like `inEdges` and `outEdges` are expensive
"""


class Graph(object):
    def __init__(self, size: int):
        self.matrix = []
        self.size = size

        for i in range(size):
            self.matrix.append([0 for i in range(size)])

    def add_edge(self, v1: int, v2: int):
        self.matrix[v1][v2] = 1

    def remove_edge(self, v1: int, v2: int):
        if self.matrix[v1][v2] == 0:
            raise LookupError(f"No edge between {v1} and {v2}")
        else:
            self.matrix[v1][v2] = 0

    def contains_edge(self, v1: int, v2: int) -> bool:
        if self.matrix[v1][v2]:
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __str__(self):
        s = ""
        for row in self.matrix:
            row_s = ' '.join([str(i) for i in row])
            s = '\n'.join((s, row_s))
        return s
