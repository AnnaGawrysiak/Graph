from errors import VertexAlreadyExists


class Vertex(object):
    def __init__(self, label, directed=True):
        self.label = label
        self.directed = directed
        self.__edges = set()

    def __str__(self):
        return str(self.label)

    def add_edge(self, edge):
        self.__edges.add(edge)

    def remove_edge(self, edge):
        self.__edges.remove(edge)

    def get_neighbours(self):

        neighbours = []

        for edge in self.__edges:
            if edge.end_vertex != self:
                neighbours.append(edge.end_vertex)
            else:
                neighbours.append(edge.start_vertex)

        return neighbours

    def get_outbound_edges(self):
        if not self.directed:
            return self.__edges

        outbound_edges = []
        for edge in self.__edges:
            if edge.start_vertex == self:
                outbound_edges.append(edge)

        return outbound_edges

    def get_inbound_edges(self):
        if not self.directed:
            return self.__edges

        inbound_edges = []
        for edge in self.__edges:
            if edge.end_vertex == self:
                inbound_edges.append(edge)

        return inbound_edges

    def __eq__(self, x):
        return self.label == x.label
