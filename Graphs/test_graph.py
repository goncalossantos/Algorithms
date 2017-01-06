from unittest import TestCase

from Graphs.base import Graph, Edge


def graph_for_transversal():
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
    return g


class TestGraph(TestCase):
    def test_prim_mst_with_heap(self):
        expected = set()
        expected.update([
            Edge(source=0, destination=1, weight=2),
            Edge(source=1, destination=2, weight=3),
            Edge(source=0, destination=3, weight=6),
            Edge(source=1, destination=4, weight=5),
        ])

        g = Graph(5)
        g.add_edge(0, 1, 2)
        g.add_edge(0, 3, 6)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 8)
        g.add_edge(2, 4, 7)
        g.add_edge(3, 4, 9)
        g.add_edge(1, 4, 5)

        assert g.prim_mst_with_heap() == expected

    def test_prim_mst(self):
        expected = set()
        expected.update([
            Edge(source=0, destination=1, weight=2),
            Edge(source=1, destination=2, weight=3),
            Edge(source=0, destination=3, weight=6),
            Edge(source=1, destination=4, weight=5),
        ])

        g = Graph(5)
        g.add_edge(0, 1, 2)
        g.add_edge(0, 3, 6)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 8)
        g.add_edge(2, 4, 7)
        g.add_edge(3, 4, 9)
        g.add_edge(1, 4, 5)
        # This symmetry is needed for adjacency matrix version
        g.add_edge(1, 0, 2)
        g.add_edge(3, 0, 6)
        g.add_edge(2, 1, 3)
        g.add_edge(3, 1, 8)
        g.add_edge(4, 2, 7)
        g.add_edge(4, 3, 9)
        g.add_edge(4, 1, 5)

        assert g.prim_mst() == expected

    def test_kruskal_mst(self):
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

    def test_cycle(self):
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

    def test_bfs(self):
        g = graph_for_transversal()
        assert g.bfs(0) == [0, 1, 2, 5, 4, 3]

    def test_recursive_dfs(self):
        g = graph_for_transversal()
        assert g.recursive_dfs(0) == [0, 1, 2, 4, 3, 5]
