from adjacencySet import AdjacencySet

def sample_run(graph):
    print('---\nRunning sample...')
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(2, 3)

    for i in range(4):
        print('Adjacent to: {} = {}'.format(i, graph.get_adjacent_vertices(i)))

    for i in range(4):
        print('Indegree: {} = {}'.format(i, graph.get_indegree(i)))

    for i in range(4):
        for j in graph.get_adjacent_vertices(i):
            print('Edge weight for ({},{}): {}'.format(
                i, j, graph.get_edge_weight(i, j)
            ))

    graph.display()
# Sample undirected graph
graph = AdjacencySet(4)
sample_run(graph)

# Sample directed graph
graph = AdjacencySet(4, directed=True)
sample_run(graph)