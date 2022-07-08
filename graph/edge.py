from vertex import Vertex

class Edge(object):
    def __init__(self, start_vertex, end_vertex, weight=1, directed=True):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

    def __str__(self):
        if self.__directed:
            return f"{self.start_label} -{self.weight}-> {self.end_label}"
        else:
            return f"{self.start_label} <-{self.weight}-> {self.end_label}"