from typing import List, Tuple

import networkx as nx
from matplotlib import pyplot as plt


# structure representing graph
class Graph:
    # just making type hints
    def __init__(self, v_labels: List[str], adjacency_list: List[List[Tuple[int, str]]]):
        self.v_labels = v_labels
        self.adjacency_list = adjacency_list
        if not self.is_correct():
            raise TypeError("graph not implemented correctly")

    # checking if adjacency list is correct and coherent with vertex labels
    def is_correct(self):
        if len(self.v_labels) != len(self.adjacency_list):
            return False

        for v1 in range(len(self.adjacency_list)):
            for v2, label in self.adjacency_list[v1]:
                if not (v1, label) in self.adjacency_list[v2]:
                    return False

        return True

    def visualize(self):
        n = len(self.v_labels)
        edges = {(v1, v2): label for v1 in range(n) for v2, label in self.adjacency_list[v1]}

        G = nx.Graph()
        G.add_nodes_from(range(n))
        G.add_edges_from(edges.keys())

        # feel free to change
        options = {
            "node_size": 3000,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 5,
            "width": 5,
            "verticalalignment": "top"
        }

        pos = nx.spring_layout(G)

        nx.draw_networkx(G, pos, **options)
        nx.draw_networkx_labels(G, pos, {v: self.v_labels[v] for v in range(n)}, font_size=30, verticalalignment="baseline")
        nx.draw_networkx_edge_labels(G, pos, edges)

        plt.show()

    ''' feel free to implement your class methods'''


class Production:
    # just making type hints
    def __init__(self, left: Graph, connector: Graph, right: Graph):
        self.left = left
        self.connector = connector
        self.right = right

    ''' feel free to implement your class methods'''


# example - make sure arguments are correct - otherwise exception is thrown
G = Graph(
    ["A", "B", "C"],
    [
        [(1, "a"), (2, "b")],
        [(0, "a"), (2, "c")],
        [(0, "b"), (1, "c")]
    ])

G.visualize()


