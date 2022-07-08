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
        print(neighbour)
        print(weight)
    
    #graph.display_graph()

