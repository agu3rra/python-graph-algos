import abc
import numpy as np


class Graph(abc.ABC):

    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        # v1 and v2 are vertices
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        # return the adjacent vertices for a given vertex
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        # return the number of edges for a given vertex
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        # return the weight for the edge between the given vertices
        pass

    @abc.abstractmethod
    def display(self):
        # prints out the current graph to the terminal
        pass
