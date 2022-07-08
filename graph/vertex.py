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



