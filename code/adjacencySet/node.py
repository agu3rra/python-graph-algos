class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set() # initialize it empty

    def add_edge(self, v):
        if self.vertex_id == v:
            message='Vertex {} cannot be adjacent to itself.'.format(v)
            raise ValueError(message)
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)
