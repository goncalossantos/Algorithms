from collections import defaultdict, deque, namedtuple
from typing import List, Dict, Optional

# TODO: Build a builder for the Graph class
# TODO: Subclass the graph class to handle max nodes
# TODO: Handle construction of graph better better
# TODO: Subclass different types of graphs

Edge = namedtuple("Edge", ["source", "destination", "weight"])


class Graph:
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

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """ Adds an edge to the graph from u to v

        :param weight:
        :param u: origin node
        :param v: destination node
        """
        # If the graph was constructed with a max number of edges we must check for this
        if self.v is not None and self.v < len(self.graph) + 1:
            raise Exception("Graph's max size reached")

        # Checks if edge already exists - This makes adding slow
        new_edge = Edge(source=u, destination=v, weight=weight)
        if new_edge not in self.graph[u]:
            self.graph[u].append(new_edge)

    def bfs(self, source_node: int) -> List[int]:
        """
        
        :param source_node: Source node for BFS
        :return order: Final order in which nodes were visited
        """

        # Store visited order in a list
        order = list()  # type: List[int]

        # Mark all the vertices as not visited
        visited = [False] * (len(self))  # type: List[bool]

        # Create queue for BFS
        queue = deque()  # type: deque[int]

        # Mark the source node as visited and enqueue it
        queue.append(source_node)
        visited[source_node] = True

        while queue:
            next_node = queue.popleft()
            order.append(next_node)
            for edge in self.graph[next_node]:
                # Check the edge object
                assert isinstance(edge, Edge)
                assert isinstance(edge.destination, int)
                adjacent_node = edge.destination
                if visited[adjacent_node] is False:
                    queue.append(adjacent_node)
                    visited[adjacent_node] = True
        return order

    def recursive_dfs_util(self, next_node: int, visited: List[int], order: List[int]) -> List[int]:
        """ Utility function for recursive Depth First

        :param order: order in which nodes are visited
        :param next_node: next_node to be considered
        :param visited: List of booleans signifying visited nodes
        """

        # Mark the current node as visited and print it
        visited[next_node] = True
        order.append(next_node)

        for edge in self.graph[next_node]:
            # Check the edge object
            assert isinstance(edge, Edge)
            assert isinstance(edge.destination, int)
            adjacent_node = edge.destination
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
        visited = [False] * (len(self))  # type: List[bool]
        return self.recursive_dfs_util(source_node, visited, order)

    #
    def find_parent(self, parents_array: List[int], node_index: int) -> int:
        """ A utility function to find the subset of an element node_index

        :param parents_array:
        :param node_index:
        :return: Returns the final index of the node's parent
        """
        if parents_array[node_index] == -1:
            return node_index
        if parents_array[node_index] != -1:
            return self.find_parent(parents_array, parents_array[node_index])

    def union(self, parents_array: List[int], x: int, y: int) -> None:
        """ A utility function to do union of two subsets

        :param parents_array: marks the parent of each node
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
        parents_array = [init_value] * (len(self))  # type: List[int]


        for i in self.graph:
            for edge in self.graph[i]:
                assert isinstance(edge, Edge)
                assert isinstance(edge.destination, int)
                j = edge.destination
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

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def kruskal_mst(self) -> List[Edge]:
        """ Computes the minimum spanning tree with Kruskal's method

        :return: returns a list with the minimum spanning tree
        """
        init_value = -1
        edges_so_far = 0  # type:int
        total_vertices = len(self)  # type: int
        parents_array = [init_value] * (len(self))  # type: List[int]
        target_number_edges = len(self) - 1  # type: int
        result = list()  # type: List[Edge]

        sorted_edges = self.sort_edges_by_weight()  # type: List[Edge]
        for edge in sorted_edges:
            source, destination, weight = edge
            parent_source = self.find_parent(parents_array, source)
            parent_destination = self.find_parent(parents_array, destination)
            if parent_source != parent_destination:
                result.append(edge)
                edges_so_far += 1
                if edges_so_far == target_number_edges:
                    break
                self.union(parents_array=parents_array, x=parent_source, y=parent_destination)

        return result

    def sort_edges_by_weight(self) -> List[Edge]:
        edges_list = [edge for node in self.graph for edge in self.graph[node]]
        sorted_edges = sorted(edges_list, key=lambda x: x.weight)
        return sorted_edges

    def __str__(self) -> str:
        """ Prints the graph by printing nodes and and their respective adjacent nodes

        """
        to_print = list()  # type: List[str]
        to_print.append("Nodes in graph:")
        for node in self.graph:
            to_print.append("\n\t")
            to_print.append(str(node))
            to_print.append("->")
            for edge in self.graph[node]:
                assert isinstance(edge, Edge)
                assert isinstance(edge.destination, int)
                adjacent_node = edge.destination
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


def test_kruskal_mst():
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    expected = [
        Edge(source=2, destination=3, weight=4),
        Edge(source=0, destination=3, weight=5),
        Edge(source=0, destination=1, weight=10)
    ]
    assert g.kruskal_mst() == expected


test()
test_cycle()
test_kruskal_mst()
