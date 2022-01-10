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
        plt.figure()
        n = len(self.v_labels)
        edges = {(v1, v2): label for v1 in range(n) for v2, label in self.adjacency_list[v1]}

        G = nx.Graph()
        G.add_nodes_from(range(n))
        G.add_edges_from(edges.keys())

        # feel free to change
        options = {
            "node_size": 500,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 0.5,
            "width": 0.5,
            "verticalalignment": "top"
        }

        pos = nx.spring_layout(G)

        nx.draw_networkx(G, pos, **options)
        nx.draw_networkx_labels(G, pos, {v: self.v_labels[v] for v in range(n)}, font_size=10,
                                verticalalignment="baseline")
        nx.draw_networkx_edge_labels(G, pos, edges)
        return plt.gcf()

    def remove(self, i):
        self.v_labels.pop(i)
        for v in range(len(self.adjacency_list)):
            newV = []
            for a in self.adjacency_list[v]:
                if a[0] < i:
                    newV.append(a)
                else:
                    if a[0] > i:
                        newV.append((a[0] - 1, a[1]))
            self.adjacency_list[v] = newV
        self.adjacency_list.pop(i)

    def remove_edge(self, edges, GV):
        for k in edges:
            edge = (GV[k[0]], k[1])
            for tab in self.adjacency_list:
                if edge in tab:
                    tab.remove(edge)

    def add_node(self, label, edges, KR, i):
        self.v_labels.append(label)
        edge_list = []
        for edge in edges:
            if KR[edge[0]] is not None:
                edge_list.append((KR[edge[0]], edge[1]))
                self.adjacency_list[KR[edge[0]]].append((len(self.v_labels) - 1, edge[1]))
        self.adjacency_list.append(edge_list)
        KR[i] = len(self.v_labels) - 1
        return KR

    ''' feel free to implement your class methods'''


class Production:
    # just making type hints
    def __init__(self, left: Graph, connector: Graph, right: Graph, dict_array):
        self.left = left
        self.connector = connector
        self.right = right
        self.dict = dict_array

    ''' feel free to implement your class methods'''


class Grammar:
    # just making type hints
    def __init__(self, input_graph: Graph, production_list: List[Production]):
        self.input_graph = input_graph
        self.production_list = production_list


# example - make sure arguments are correct - otherwise exception is thrown
if __name__ == '__main__':
    G = Graph(
        ["A", "B", "C"],
        [
            [(1, "a"), (2, "b")],
            [(0, "a"), (2, "c")],
            [(0, "b"), (1, "c")]
        ]
    )

    G.visualize()
    plt.show()
