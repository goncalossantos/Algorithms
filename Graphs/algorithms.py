from math import inf
from typing import List

from Graphs.base import Graph
from Graphs.priority_queue import MinHeap


def dijkstra_shortest_path(graph_object: Graph, start_node: int) -> List[float]:
    """ Computes the dijkstra's shortest path algorithm

    :param graph_object:
    :param start_node:
    :return: Returns a list. A node is represented by the index, and each List[index] is the distance from the original
    position to that node
    """

    def init_distance(g, s):
        d = [inf] * len(g)  # type: List[float]
        d[s] = 0.0
        return d

    # Assign a key value to all vertices in the input graph.
    # Initial value is inf for all but the first one
    distance = init_distance(graph_object, start_node)
    priority_queue = MinHeap.build([(i, priority) for i, priority in enumerate(distance)])

    while priority_queue:  # Priority queue has O(V) elements
        min_index = priority_queue.pop()  # O(log(V))
        for edge in graph_object.graph[min_index]:  # A graph has at most 2E Edges in adjacency list, so O(E)
            source, destination, edge_weight = edge
            if priority_queue.contains_item(destination) and distance[source] + edge_weight < distance[destination]:
                distance[destination] = distance[source] + edge_weight
                priority_queue.push(item=destination, priority=edge_weight)  # O(log(V))

    return distance
