from src.structures import Graph, Production
from copy import deepcopy


def check_node(graph: Graph, prod: Graph, v, u, prod_dict, A):
    if graph.v_labels[v] != prod.v_labels[u]:
        return False
    prodIt = 0
    adjacencyProd = deepcopy(prod.adjacency_list[u])
    adjacencyGraph = deepcopy(graph.adjacency_list[v])
    for i in adjacencyProd:
        temp = (A[prod_dict.index(i[0])], i[1])
        if temp in adjacencyGraph:
            prodIt += 1
            adjacencyGraph.remove(temp)
    if len(adjacencyProd) == prodIt:
        return True
    return False


def check_if_right(G: Graph, L: Graph, Nodes, L_dict, A):
    if len(Nodes) != len(L.adjacency_list):
        raise ValueError("Incorrect number of vertexes.")
    for i in range(len(Nodes)):
        if not check_node(G, L, Nodes[i], L_dict[i], L_dict, A):
            raise ValueError("Incorrect order of vertexes or vertexes.")
    return True


def which_edge(L_list, K_list):
    ans = []
    for i in L_list:
        if i not in K_list:
            ans.append(i)
    return ans


def first_step(L, K, G, givenNodes, L_dict):
    for i in L.adjacency_list:
        if i not in K.adjacency_list:
            G.remove(givenNodes[L_dict.index(i)])
    for i in L.adjacency_list:
        if i in K.adjacency_list and L.adjacency_list[i] != K.adjacency_list[i]:
            edges = which_edge(L.adjacency_list[i], K.adjacency_list[i])
            G.remove_edge(edges, givenNodes, L_dict)


def second_step(G, R, K, arr, GR):
    for i in R.adjacency_list:
        if i not in K.adjacency_list:
            GR = G.add_node(R.v_labels[i], R.adjacency_list[i], GR, i, arr)
    for i in R.adjacency_list:
        if R.adjacency_list[i] != G.adjacency_list[arr[GR.index(i)]]:
            for k in R.adjacency_list[i]:
                temp = (arr[GR.index(k[0])], k[1])
                if temp not in G.adjacency_list[arr[GR.index(i)]]:
                    G.add_edge(temp, arr[GR.index(i)])


def dpo(G, Prod: Production, arr):
    L_dict = []
    for key in Prod.left.adjacency_list.keys():
        L_dict.append(key)
    if check_if_right(G, Prod.left, arr, L_dict, arr):
        first_step(Prod.left, Prod.connector, G, arr, L_dict)
        GR = deepcopy(L_dict)
        second_step(G, Prod.right, Prod.connector, arr, GR)
