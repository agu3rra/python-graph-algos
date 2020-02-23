from adjacencyMatrix import AdjacencyMatrix

graph = AdjacencyMatrix(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 3)

for i in range(4):
    print('Adjacent to: {} {}'.format(i, graph.get_adjacent_vertices(i)))