import numpy as np
from queue import Queue # FIFO
from adjacencySet import AdjacencySet

def breadth_first(graph: AdjacencySet, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeroes(graph.num_vertices)

    while not queue.empty():
        vertex = queue.get()
        if visited[vertex] == 1:
            continue
        print('Visit: {}'.format(vertex))
        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)

def depth_first(graph: AdjacencySet, visited, current=0):
    if visited[current] == 1:
        return
    visited[current] = 1
    print('Visit: {}'.format(current))

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)

graph = AdjacencySet(9)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,7)
graph.add_edge(2,4)
graph.add_edge(2,3)
graph.add_edge(1,5)
graph.add_edge(5,6)
graph.add_edge(6,3)
graph.add_edge(3,4)
graph.add_edge(6,8)

visited = np.zeros(graph.num_vertices)
depth_first(graph, visited)