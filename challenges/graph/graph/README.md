# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

## Approach & Efficiency
add_node() time Big O(1), space Big O(1)
add_edge() time Big O(1), space Big O(1)
get_nodes() time Big O(1), space Big O(1)
get_neighbors() time Big O(1), space Big O(1)
size() time Big O(1), space Big O(1)

## API
AddNode()
Adds a new node to the graph
Takes in the value of that node
Returns the added node
AddEdge()
Adds a new edge between two nodes in the graph
Include the ability to have a “weight”
Takes in the two nodes to be connected by the edge
Both nodes should already be in the Graph
GetNodes()
Returns all of the nodes in the graph as a collection (set, list, or similar)
GetNeighbors()
Returns a collection of edges connected to the given node
Takes in a given node
Include the weight of the connection in the returned collection
Size()
Returns the total number of nodes in the graph