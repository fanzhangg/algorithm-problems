"""Implementing Graph in adjacent list"""

import pandas as pd


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.color = None
        self.distance = 0

        # variables related to neighbors
        self.out_neighbors = {}
        self.in_neighbors = {}
        self.indegree = len(self.in_neighbors)
        self.outdegree = len(self.out_neighbors)
        self.degree = self.indegree + self.outdegree

    def __dict__(self):
        out_l = [v.value for v in self.out_neighbors.keys() if v is not None]
        in_l = [v.value for v in self.in_neighbors.keys() if v is not None]
        return {
            "color": self.color,
            "out": str(out_l),
            "in": str(in_l)}

    def __str__(self):
        """
        :return: i.e. "1 (color: "white", out-neighbors: [a, b, c], in-neighbors: [d]"
        """

        df = pd.DataFrame(self.__dict__(), index=[self.value])

        return str(df)
        # return "".join((str(self.value), " (",
        #                 "color:", str(self.color),
        #                 "\tout:", out_neighbors_list,
        #                 "\tin:", in_neighbors_list,
        #                 ")"))

    def add_in_neighbor(self, in_nbr, weight=0):
        """Add a in-neighbor: in_nbr has an edge to current vertex"""
        self.in_neighbors[in_nbr] = weight

    def add_out_neighbor(self, out_nbr, weight=0):
        """Add a out-neighbor: out_nbr with an edge from current vertex"""
        self.out_neighbors[out_nbr] = weight

    def get_out_neighbors(self):
        """Return all connected vertices"""
        return self.out_neighbors.keys()

    def get_weight(self, nbr):
        """Return the weight of the edge from this vertex to the vertex passed as a parameter"""
        return self.out_neighbors[nbr]


class Edge(object):
    def __init__(self, from_value: int, to_value: int, weight=0):
        # self.from_v = self.__set_from_v(from_value, to_value, weight)
        # self.to_v = self.__set_to_v(from_value, to_value, weight)
        self.from_value = from_value
        self.to_value = to_value
        self.weight = weight

    @staticmethod
    def __set_from_v(from_value, to_value, weight):
        from_v = Graph.vert_list.get(from_value, Vertex(from_value))
        to_v = Graph.vert_list.get(to_value, Vertex(to_value))
        from_v.add_out_neighbor(to_v, weight)
        return from_v

    @staticmethod
    def __set_to_v(from_value, to_value, weight):
        from_v = Graph.vert_list.get(from_value)
        to_v = Graph.vert_list.get(to_value, Vertex(to_value))
        to_v.add_in_neighbor(from_v, weight)
        return to_v

    def __str__(self):
        return "".join(("(", str(self.from_value), ")--", str(self.weight), "-->(", str(self.to_value), ")"))


class Graph:
    """Holds the master list of vertices
    Maps vertex names to vertex object"""

    # class variable
    vert_list = {}
    edge_list = []

    def __init__(self):
        self.vert_num = 0

    def add_vertex(self, key):
        self.vert_num += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vert_list

    def add_edge(self, from_key, to_key, weight=0):
        # Add the edge to the edge list
        edge = Edge(from_key, to_key, weight)
        self.edge_list.append(edge)

        # Update the neighbors of the two vertices connected by the edge
        if from_key not in self.vert_list:
            self.add_vertex(from_key)
        if to_key not in self.vert_list:
            self.add_vertex(to_key)
        from_v = self.vert_list[from_key]
        from_v.add_out_neighbor(self.vert_list[to_key], weight)

    def add_undirected_edge(self, key1, key2, weight=0):
        # out_edge = Edge(key1, key2, weight)
        # self.edge_list.append(out_edge)
        # in_edge = Edge(key2, key1, weight)
        # self.edge_list.append(in_edge)
        self.add_edge(key1, key2, weight)
        self.add_edge(key2, key1, weight)

    def get_weight(self, edge):
        # TODO: add the get_weight
        pass

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        """Loop over all the vertex objects in a graph"""
        return iter(self.vert_list.values())

    def __str__(self):
        dic_l = [v.__dict__() for v in self.vert_list.values()]
        v_values = [v.value for v in self.vert_list.values()]
        df = pd.DataFrame(dic_l, index=v_values)
        return str(df)
        # return "\n".join((str(v) for v in self.vert_list.values()))
