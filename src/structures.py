from typing import List, Tuple, Dict

import networkx as nx
from matplotlib import pyplot as plt


# structure representing graph
class Graph:
    # just making type hints
    def __init__(self, v_labels: Dict[int, str], adjacency_list: Dict[int, List[Tuple[int, str]]]):
        self.v_labels = v_labels
        self.adjacency_list = adjacency_list
        if not self.is_correct():
            raise TypeError("graph not implemented correctly")

    # checking if adjacency list is correct and coherent with vertex labels
    def is_correct(self):
        # check if indexes (keys) are matching
        if set(self.v_labels.keys()) != set(self.adjacency_list.keys()):
            return False

        # iterate over keys
        for v1 in self.adjacency_list:
            # iterate over elements
            for v2, label in self.adjacency_list[v1]:
                if not (v1, label) in self.adjacency_list[v2]:
                    return False

        return True

    def visualize(self):
        plt.figure()
        edges = {(v1, v2): label for v1 in self.adjacency_list for v2, label in self.adjacency_list[v1]}

        G = nx.Graph()
        G.add_nodes_from(index for index in self.v_labels)
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
        nx.draw_networkx_labels(G, pos, {v: self.v_labels[v] for v in self.adjacency_list}, font_size=10,
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

    ''' feel free to implement your class methods'''


class Grammar:
    # just making type hints
    def __init__(self, input_graph: Graph, production_list: List[Production]):
        self.input_graph = input_graph
        self.production_list = production_list
        # to be able to go back once
        self.previous_graph = None


# example - make sure arguments are correct - otherwise exception is thrown
if __name__ == '__main__':
    G = Graph(
        {5: "A", 1: "B", 2: "C"},
        {
            5: [(1, "a"), (2, "b")],
            1: [(5, "a"), (2, "c")],
            2: [(5, "b"), (1, "c")]
        }
    )

    G.visualize()
    plt.show()
