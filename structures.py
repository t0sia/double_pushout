import string

from typing import List


# structure representing graph
class Graph:
    # just making type hints
    def __init__(self, v_labels: List[string], adjacency_list: List[List[int]]):
        self.v_labels = v_labels
        self.adjacency_list = adjacency_list

    ''' feel free to implement your class methods'''


class Production:
    # just making type hints
    def __init__(self, left: Graph, connector: Graph, right: Graph):
        self.left = left
        self.connector = connector
        self.right = right

    ''' feel free to implement your class methods'''
