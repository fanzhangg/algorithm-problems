class Vertex:
    """Lightwieght vertex structure for a graph"""
    __slots__ = '_element'

    def __init__(self, x):
        """Do not call it directly. Use Graph's insert_vertex instead"""
        self._element = x

    def element(self):
        """
        :return: element associated with the vertex
        """
        return self._element

    def __hash__(self):
        """
        Allow the vertex to be a map/set key
        :return:
        """
        return hash(id(self))


class Edge:
    """Edge structure for a graph"""
    __slots__ = "_origin", "_destination", "_element"

    def __init__(self, u, v, x):
        """
        Do not call it directly. Use Graph's insert_edge(u, v, x)
        """
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """
        :return: (u, v) for vertices u, v
        """
        return (self._origin, self._destination)

    def opposite(self, v):
        """
        :return: the vertex that is opposite v on the edge
        """
        if v is self._origin:
            return self._destination
        else:
            return self._origin

    def element(self):
        """
        :return: element associated with the edge
        """
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))


class Graph:
    """Represent a simple graph using an adjacency"""
    def __init__(self, directed=False):
        """
        Create an empty graph (undirected, by default)
        :param directed: True if graph is directed
        """
        self._outgoing = {}
        if directed:
            self._incoming = {}

    def is_directed(self):
        """
        :return: True if this is a directed graph; False if undirected
        """
        return self._incoming is not self._outgoing # Directed if maps are distinct

    def vertex_count(self):
        """
        :return: the number of vertices in the graph
        """
        return len(self._outgoing)

    def vertices(self):
        """
        :return: an iteration of all vertices of the graph
        """
        return self._outgoing.keys()

    def edge_count(self):
        """
        :return: the number of edges in the graph
        """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        if self.is_directed():
            return total
        else:   # Not double-count edges
            return total // 2

    def edges(self):
        """
        :return: a set of all edges of the graph
        """
        result = set()
        for secondary_map in self._outgoing.values():
            return