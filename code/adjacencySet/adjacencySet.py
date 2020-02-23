from graph import Graph
from node import Node


class AdjacencySet(Graph):

    def __init__(self, num_vertices, directed=False):
        super(AdjacencySet, self).__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(self.num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1>=self.num_vertices or v2>=self.num_vertices or v1<0 or v2<0:
            message = 'Vertices ({},{}) are out of bounds.'.format(v1, v2)
            raise ValueError(message)
        if weight != 1:
            raise ValueError('This class can only represent unweighted edges.')

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v<0 or v>= self.num_vertices:
            raise ValueError('Cannot access vertex {}.'.format(v))
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v<0 or v>=self.num_vertices:
            raise ValueError('Cannot access vertex {}.'.format(v))
        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1 # since we implemented it unweighted.

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print('{}-->{}'.format(i, v))