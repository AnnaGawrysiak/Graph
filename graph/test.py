# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

import pytest
from graph import Graph

def test_graph_constructor_vertices():
    graph1 = Graph()

    graph1.add_vertex("A")
    graph1.add_vertex("B")
    graph1.add_vertex("C")
    graph1.add_vertex("D")
    graph1.add_vertex("E")
    graph1.add_vertex("F")
    graph1.add_vertex("G")
    graph1.add_vertex("H")

    graph1.add_edge("A", "B")
    graph1.add_edge("B", "D")
    graph1.add_edge("B", "C")
    graph1.add_edge("C", "D")
    graph1.add_edge("C", "E")
    graph1.add_edge("D", "E")
    graph1.add_edge("H", "E")
    graph1.add_edge("G", "H")
    graph1.add_edge("A", "G")
    graph1.add_edge("G", "F")
    graph1.add_edge("F", "E")
    graph1.add_edge("F", "C")

    for item in graph1.get_vertices().keys():
        print(item)

    #assert 'A' in graph1.get_vertices()
    assert all(key in graph1.get_vertices() for key in ['A', 'B', 'C', 'D','E', 'F', 'G', 'H'])

def test_graph_constructor_edges():

    graph1 = Graph()

    graph1.add_vertex("A")
    graph1.add_vertex("B")
    graph1.add_vertex("C")
    graph1.add_vertex("D")
    graph1.add_vertex("E")
    graph1.add_vertex("F")
    graph1.add_vertex("G")
    graph1.add_vertex("H")

    graph1.add_edge("A", "B")
    graph1.add_edge("B", "D")
    graph1.add_edge("B", "C")
    graph1.add_edge("C", "D")
    graph1.add_edge("C", "E")
    graph1.add_edge("D", "E")
    graph1.add_edge("H", "E")
    graph1.add_edge("G", "H")
    graph1.add_edge("A", "G")
    graph1.add_edge("G", "F")
    graph1.add_edge("F", "E")
    graph1.add_edge("F", "C")

    for item in graph1.get_edges():
        print(item)

def test_vertex_get_neighbours():
    graph1 = Graph()

    graph1.add_vertex("A")
    graph1.add_vertex("B")
    graph1.add_vertex("C")
    graph1.add_vertex("D")
    graph1.add_vertex("E")
    graph1.add_vertex("F")
    graph1.add_vertex("G")
    graph1.add_vertex("H")

    graph1.add_edge("A", "B")
    graph1.add_edge("B", "D")
    graph1.add_edge("B", "C")
    graph1.add_edge("C", "D")
    graph1.add_edge("C", "E")
    graph1.add_edge("D", "E")
    graph1.add_edge("H", "E")
    graph1.add_edge("G", "H")
    graph1.add_edge("A", "G")
    graph1.add_edge("G", "F")
    graph1.add_edge("F", "E")
    graph1.add_edge("F", "C")

    vertex = graph1.get_vertex('C')
    neighbours = vertex.get_neighbours(vertex)

    assert all(key in neighbours for key in [graph1.get_vertex('B').label, graph1.get_vertex('D').label, graph1.get_vertex('E').label,graph1.get_vertex('F').label])

def test_vertex_get_vertex():
    graph1 = Graph()

    graph1.add_vertex("A")
    graph1.add_vertex("B")
    graph1.add_vertex("C")
    graph1.add_vertex("D")
    graph1.add_vertex("E")
    graph1.add_vertex("F")
    graph1.add_vertex("G")
    graph1.add_vertex("H")

    graph1.add_edge("A", "B")
    graph1.add_edge("B", "D")
    graph1.add_edge("B", "C")
    graph1.add_edge("C", "D")
    graph1.add_edge("C", "E")
    graph1.add_edge("D", "E")
    graph1.add_edge("H", "E")
    graph1.add_edge("G", "H")
    graph1.add_edge("A", "G")
    graph1.add_edge("G", "F")
    graph1.add_edge("F", "E")
    graph1.add_edge("F", "C")

    vertex = graph1.get_vertex('A')

        # assert vertex.label == 'A' and vertex.get_neighbours ==

test_graph_constructor_vertices()
test_graph_constructor_edges()
#test_vertex_get_vertex()
test_vertex_get_neighbours()