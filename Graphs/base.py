from collections import defaultdict, deque
from typing import List, Dict, Optional


# TODO: Build a builder for the Graph class
# TODO: Subclass the graph class to handle max nodes
# TODO: Handle construction of graph better better


class Graph():
    """ This class represents a directed graph using adjacency
    list representation

    """

    def __init__(self, vertices: Optional[int] = None) -> None:
        """ Constructor

        :param vertices: Size of graph - This is optional
        """
        if vertices is not None:
            assert isinstance(vertices, int)
        self.v = vertices
        # Default dictionary to store graph
        self.graph = defaultdict(list)  # type: Dict[int, List]

    def __len__(self):

        if self.v is not None:
            return self.v
        else:
            return len(self.graph)

    def add_edge(self, u: int, v: int) -> None:
        """ Adds an edge to the graph from u to v

        :param u: origin node
        :param v: destination node
        """
        # If the graph was constructed with a max number of edges we must check for this
        if self.v is not None and self.v < len(self.graph) + 1:
            raise Exception("Graph's max size reached")
        # Checks if edge already exists - This makes adding slow
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def bfs(self, source_node: int) -> List[int]:
        """
        
        :param source_node: Source node for BFS
        :return order: Final order in which nodes were visited
        """

        # Store visited order in a list
        order = list()  # type: List[int]

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

    def recursive_dfs_util(self, next_node: int, visited: List[bool], order: List[int]) -> List[int]:
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
                order = self.recursive_dfs_util(adjacent_node, visited, order)

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
        return self.recursive_dfs_util(source_node, visited, order)

    #
    def find_parent(self, parents_array, node_index) -> int:
        """ A utility function to find the subset of an element node_index

        :param parents_array:
        :param node_index:
        :return: Returns the final index of the node's parent
        """
        if parents_array[node_index] == -1:
            return node_index
        if parents_array[node_index] != -1:
            return self.find_parent(parents_array, parents_array[node_index])

    def union(self, parents_array, x, y) -> None:
        """ A utility function to do union of two subsets

        :param parent:
        :param x: First node to join
        :param y: Second node to join
        """
        x_set = self.find_parent(parents_array, x)
        y_set = self.find_parent(parents_array, y)
        parents_array[x_set] = y_set

    def contains_cycle(self) -> bool:
        """ The main function to check whether a given graph contains cycle or not

        This function assumes that there are no self loops in the graph

        :return: Returns True if a cycle is found, False if it isn't
        """
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        init_value = -1  # type: int
        if self.v is None:
            parents_array = [init_value] * (len(self.graph))  # type: List[int]
        else:
            parents_array = [init_value] * self.v  # type: List[int]

        for i in self.graph:
            for j in self.graph[i]:
                if i == j:
                    # Self loop found
                    raise Exception("Graph has self loop")
                parent_of_i = self.find_parent(parents_array, i)
                parent_of_j = self.find_parent(parents_array, j)
                if parent_of_i == parent_of_j:
                    # Cycle found
                    return True
                self.union(parents_array, parent_of_i, parent_of_j)
        return False

    def __str__(self) -> str:
        """ Prints the graph by printing nodes and and their respective adjacent nodes

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


def test_cycle() -> None:
    """ Tests if the union-find algorithm for finding cycles is working

    :return:
    """
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    # g.add_edge(0, 0)
    assert g.contains_cycle() is False
    g.add_edge(1, 2)
    assert g.contains_cycle() is True


g = Graph()
test()
test_cycle()
