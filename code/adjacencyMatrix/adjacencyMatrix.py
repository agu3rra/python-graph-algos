import numpy as np
from functools import wraps
from graph import Graph

def _validate_vertex_index(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        v = args[0]
        if v < 0 or v >= self.num_vertices:
            raise ValueError('Cannot access vertex {}'.format(v))
    return wrapper

class AdjacencyMatrix(Graph):

    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrix, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or \
            v2 >= self.num_vertices or \
            v1 < 0 or v2 < 0:
            message = 'Vertices {} and {} are out of bounds.'.format(v1, v2)
            raise ValueError(message)

        if weight < 1:
            raise ValueError('An edge cannot have weight < 1.')

        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    @_validate_vertex_index    
    def get_adjacent_vertices(self, v):
        

        adjacent_vertices = []
        for item in range(self.num_vertices):
            if self.matrix[v][item] > 0:
                adjacent_vertices.append(item)
        return adjacent_vertices

    @_validate_vertex_index
    def get_indegree(self, v):
        indegree = 0
        for item in range(self.num_vertices):
            if self.matrix[item][v] > 0:
                indegree += 1

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print('{}-->{}'.format(i, v))