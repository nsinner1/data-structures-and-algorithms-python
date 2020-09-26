import pytest
from graph.graph import Graph, Vertex, Edge 


def test_add_graph():
    graph = Graph()
    assert graph


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('spam')
    assert vertex.value == 'spam'


def test_add_edge():
    graph = Graph()
    spam = graph.add_vertex('spam')
    egg = graph.add_vertex('eggs')
    graph.add_edge(spam, egg)
    assert True


def test_add_edge_test_size_pass():
    graph = Graph()
    spam = graph.add_vertex('spam')
    egg = graph.add_vertex('eggs')
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) == 2


def test_add_edge_test_size_fail():
    graph = Graph()
    spam = graph.add_vertex('spam')
    egg = graph.add_vertex('eggs')
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) != 3


def test_edge_start_node_not_in_graph():
    graph = Graph()
    start = Vertex('start')
    end = graph.add_vertex('end')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_edge_end_node_not_in_graph():
    graph = Graph()
    end = Vertex('end')
    start = graph.add_vertex('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_neighbors_no_neighbors():
    graph = Graph()
    spam = graph.add_vertex('spam')
    neighbors = graph.get_neighbors(spam)
    assert len(neighbors) == 0
    assert neighbors == []

