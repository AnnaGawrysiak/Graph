from graph import Graph

if __name__ == '__main__':

    graph = Graph() # Graph(directed=false) for undirected graph

    graph.add_vertex("New York")
    graph.add_vertex("Bratislava")
    graph.add_vertex("Kyiv")
    graph.add_vertex("Warsaw")
    graph.add_vertex("Atlanta")

    graph.add_edge("New York", "Bratislava", 7)
    graph.add_edge("Bratislava", "Warsaw", 3)
    graph.add_edge("Warsaw", "New York", 12)
    graph.add_edge("Warsaw", "Kyiv", 5)
    graph.add_edge("Kyiv", "Bratislava", 4)
    graph.add_edge("Atlanta", "Kyiv", 11)

    graph.remove_vertex("New York")
    graph.remove_edge("Atlanta", "Kyiv")

    # get Kyiv vertex and all outbound edges
    vertex = graph.get_vertex("Warsaw")
    outbound_edges = vertex.get_outbound_edges()

    # iterate over outbound edges and get end vertex
    for edge in outbound_edges:
        neighbour = edge.end_vertex
        weight = edge.weight
        #print(neighbour)
        #print(weight)

    #graph.display_graph()

    graph1 = Graph()  # Graph(directed=false) for undirected graph

    graph1.add_vertex("A")
    graph1.add_vertex("B")
    graph1.add_vertex("C")
    graph1.add_vertex("D")
    graph1.add_vertex("E")
    graph1.add_vertex("F")
    graph1.add_vertex("G")
    graph1.add_vertex("H")

    graph1.add_edge("A", "B")
    graph1.add_edge("A", "C")
    graph1.add_edge("A", "D")
    graph1.add_edge("A", "E")
    graph1.add_edge("B", "C")
    graph1.add_edge("B", "G")
    graph1.add_edge("C", "D")
    graph1.add_edge("D", "H")
    graph1.add_edge("D", "E")
    graph1.add_edge("E", "F")
    graph1.add_edge("F", "G")
    graph1.add_edge("F", "H")
    graph1.add_edge("G", "B")

    #print([edge.end_vertex.label for edge in graph1.get_vertex("C").get_outbound_edges()])

    path1 = graph1.bfs_shortest_path("A", "G")

    path_exists = graph1.if_path_exists('C', 'G')
    #print(path_exists)

    #print(path1)

    graph2 = Graph(directed=True)

    graph2.add_vertex("1")
    graph2.add_vertex("2")
    graph2.add_vertex("3")
    graph2.add_vertex("4")
    graph2.add_vertex("5")
    graph2.add_vertex("0")

    graph2.add_edge("0", "1")
    graph2.add_edge("2", "0")
    graph2.add_edge("0", "3")
    graph2.add_edge("3", "1")
    graph2.add_edge("5", "1")
    graph2.add_edge("2", "4")
    graph2.add_edge("4", "3")
    graph2.add_edge("4", "5")


    sorted_graph = graph2.topological_sort_by_kahn_algo()
    print(f"Sorted by Khan algo: {sorted_graph}")

    #path2 = graph1.DFS("A")
    #print(f'DFS: {path2}')