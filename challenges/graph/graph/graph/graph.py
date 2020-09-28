from stacks_and_queues_graph import Queue, Node, Stack


class Graph:

    def __init__(self):
        """Class to implement Graph object with the given methods"""
        self.adjacency_list = {}

    def add_vertex(self, value):
        """
        Adds a new vertex to the graph
        Input: the value of that vertex
        Output: the added vertex
        """
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=1):
        """
        Adds a new edge between two nodes in the graph with ability to add weight
        Input: two vertexes to be connected by the edge
        *Both nodes should already be in the Graph
        """
        if start not in self.adjacency_list:
            raise KeyError('Start Vertex not in the graph')
        if end not in self.adjacency_list:
            raise KeyError('End Vertex not in the graph')

        edge = Edge(end, weight)
        adjacencies = self.adjacency_list[start]
        adjacencies.append(edge)

    def size(self):
        """Returns the total number of nodes in the graph"""
        return len(self.adjacency_list)


    def get_vertex(self):
        """Returns all of the nodes in the graph as a collection"""
        return self.adjacency_list.keys()


    def get_neighbors(self, vertex):
        """
        Returns a collection of vertexes connected to the given vertex with the weights of their connections
        Input: Takes in a given vertex
        """
        return self.adjacency_list[vertex]


    def breadth_first(self, starting_vertex):
        """
        Method to do breadth-first traversal on a graph.
        Input: starting vertex
        Output: list of vertices in the breadth-first order
        """
        vertices = []
        breadth = Queue()

        if starting_vertex not in self.adjacency_list:
            raise ValueError

        breadth.enqueue(starting_vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            vertices.append(front)

            for neighbor in self.get_neighbors(front):
                if not neighbor[0].visited:
                    neighbor[0].visited = True
                    breadth.enqueue(neighbor[0])

        for node in self.adjacency_list:
            node.visited = False

        return vertices


class Vertex:
    def __init__(self, value):
        """Class to create Vertex with the given value"""
        self.value = value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


