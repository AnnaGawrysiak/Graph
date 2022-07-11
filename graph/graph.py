from queue import Queue
from collections import defaultdict
import pydot
from PIL import Image
import tempfile
from vertex import Vertex
from edge import Edge


class Graph(object):
    def __init__(self, directed=True):
        self.__directed = directed
        self.__vertices = {}
        self.__edges = set()

    def add_vertex(self, label):
        self.__vertices[label] = Vertex(label)

    def get_edge(self, start_label, end_label):

        for edge in self.__edges:
            if edge.start_vertex.label == start_label and edge.end_vertex.label == end_label:
                return edge

        return None

    def get_vertex(self, label):
        return self.__vertices[label]

    def add_edge(self, start_label, end_label, weight=1):
        start_vertex = self.get_vertex(start_label)
        end_vertex = self.get_vertex(end_label)
        edge = Edge(start_vertex, end_vertex, weight, self.__directed)
        self.__edges.add(edge)
        start_vertex.add_edge(edge)
        end_vertex.add_edge(edge)

    def remove_vertex(self, label):

        edges_list = [edge for edge in self.__edges if edge.start_vertex.label == label or edge.end_vertex.label == label]

        for edge in edges_list:
            self.__edges.remove(edge)

        del self.__vertices[label]


    def remove_edge(self, start_label, end_label):

        edge = self.get_edge(start_label, end_label)
        self.__edges.remove(edge)

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def is_directed(self):
        return self.__directed


    #
    # def display_graph(self):
    #
    #     graph_type = "digraph" if self.is_directed() else "graph"
    #     pydot_graph = pydot.Dot(graph_type=graph_type)
    #
    #     # draw vertices
    #     for vertex in self.__vertices.values():
    #         node = pydot.Node(str(vertex))
    #         pydot_graph.add_node(node)
    #
    #     # draw edges
    #
    #     for edge in self.__edges:
    #         start_vertex_label = edge.start_vertex.label
    #         end_vertex_label = edge.end_vertex.label
    #         weight = edge.weight
    #
    #         pydot_edge = pydot.Edge(start_vertex_label, end_vertex_label)
    #         pydot_edge.label = weight
    #         pydot_graph.add_edge(pydot_edge)
    #
    #     temp = tempfile.NamedTemporaryFile()
    #     pydot_graph.write_png(temp.name)
    #
    #     image = Image.open(temp.name)
    #     temp.close()
    #
    #     image.show()

    def if_path_exists(self, start_label, target_label):

        vertex = self.get_vertex(start_label)
        seen = []
        # Mark all the vertices as not visited
        queue = Queue()

        # Add the start_node to the queue and visited list
        queue.put(vertex)
        path_found = False

        while not queue.empty():
            current_node = queue.get()

            if current_node not in seen:
                seen.append(current_node)

            if current_node.label == target_label:
                path_found = True
                return path_found

            for vertex in current_node.get_neighbours(current_node):
                if vertex not in seen:
                    queue.put(vertex)

        return path_found

    def BFS(self, start_label):

        vertex = self.get_vertex(start_label)
        seen = []
        queue = Queue()

        # Add the start_node to the queue and visited list

        queue.put(vertex)
        path =[]

        while not queue.empty():
            current_node = queue.get()

            if current_node not in seen:
                seen.append(current_node)
                path.append(current_node.label)

            for vertex in current_node.get_neighbours(current_node):
                if vertex not in seen:
                    queue.put(vertex)

        return path

    def DFS(self, start_label):

        vertex = self.get_vertex(start_label)
        seen = []
        queue = Queue()

        # Add the start_node to the queue and visited list

        queue.put(vertex)
        path = []

        while not queue.empty():
            current_node = queue.get()

            if current_node not in seen:
                seen.append(current_node)
                path.append(current_node.label)

            for vertex in current_node.get_neighbours(current_node):
                if vertex not in seen:
                    queue.put(vertex)

        return path