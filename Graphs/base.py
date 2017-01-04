from collections import defaultdict, deque
from typing import List, Dict


class Graph:
    """ This class represents a directed graph using adjacency
    list representation

    """
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)  # type: Dict[int, List]

    def add_edge(self, u: int, v: int) -> None:
        """ Adds an edge to the graph from u to v

        :param u: origin node
        :param v: destination node
        """
        self.graph[u].append(v)

    def bfs(self, source_node: int) -> List[int]:
        """
        
        :param source_node: Source node for BFS
        :return order: Final order in which nodes were visited
        """

        # Store visited order in a list
        order = list() # type: List[int]

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))  # type: List[bool]

        # Create queue for BFS
        queue = deque()  # type: deque[int]

        # Mark the source node as visited and enqueue it
        queue.append(source_node)
        visited[source_node] = True

        while queue:
            next_node = queue.popleft()
            order.append(next_node)
            for adjacent_node in self.graph[next_node]:
                if visited[adjacent_node] is False:
                    queue.append(adjacent_node)
                    visited[adjacent_node] = True
        return order

    def dfs_util(self, next_node: int, visited: List[bool], order: List[int]) -> List[int]:
        """ Utility function for recursive Depth First

        :param order: order in which nodes are visited
        :param next_node: next_node to be considered
        :param visited: List of booleans signifying visited nodes
        """

        # Mark the current node as visited and print it
        visited[next_node] = True
        order.append(next_node)

        for adjacent_node in self.graph[next_node]:
            if visited[adjacent_node] is False:
                order = self.dfs_util(adjacent_node, visited, order)

        return order

    def recursive_dfs(self, source_node: int) -> List[int]:
        """ Performs a recursive version of Depth First Search

        :param source_node: Source node for DFS
        :return order: Final order in which nodes were visited
        """

        # Store visited order in a list
        order = list()  # type: List[int]

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))  # type: List[bool]
        return self.dfs_util(source_node, visited, order)

    def __str__(self) -> str:
        """ Prints the graph by printing nodes
        and and their respective adjacent nodes

        """
        to_print = list()  # type: list[str] 
        to_print.append("Nodes in graph:")
        for node in self.graph:
            to_print.append("\n\t")
            to_print.append(str(node))
            to_print.append("->")
            for adjacent_node in self.graph[node]:
                to_print.append(str(adjacent_node))
                to_print.append(",")
        return "".join(to_print)

    @staticmethod
    def test() -> None:
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(4, 4)
        g.add_edge(2, 4)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        g.add_edge(5, 5)
        g.add_edge(1, 5)
        print("BFS:")
        print(g.bfs(0))
        print("Recursive DFS:")
        print(g.recursive_dfs(0))
        print(g)

g = Graph()
g.test()