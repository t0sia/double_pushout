from structures import Graph, Production


def check_vs(graph: Graph, prod: Graph, v, u):
    if graph.v_labels[v] != prod.v_labels[u]:
        return False
    prodIt = 0
    adjacencyProd = prod.adjacency_list[u]
    adjacencyGraph = graph.adjacency_list[v]
    for i in adjacencyProd:
        graphIt = 0
        for j in adjacencyGraph:
            if i[1] == j[1] and graph.v_labels[j[0]] == prod.v_labels[i[0]]:
                adjacencyGraph.pop(graphIt)
                prodIt += 1
                break
            graphIt += 1
    if len(adjacencyProd) == prodIt:
        return True
    return False


def check_if_right(graph: Graph, left: Graph, v1, v2):
    if len(v1) != len(v2):
        raise TypeError("Incorrect number of vertexes.")
    for i in range(len(v1)):
        if not check_vs(graph, left, v1[i], v2[i]):
            raise TypeError("Incorrect vertexes. Change order of vertexes or vertexes.")
    return True


def which_edge(A, B):
    ans = []
    for i in range(len(A)):
        val = False
        for j in range(len(B)):
            if A[i] == B[j]:
                val = True
        if val is False:
            ans.append(A[i])
    return ans


def first_step(L, K, G, LK, GV):
    for i in range(len(LK)):
        if LK[i] is None:
            G.remove(GV[i])
            L.remove(i)
    for i in range(len(K.adjacency_list)):
        if L.adjacency_list[LK[i]] != K.adjacency_list[i]:
            edges = which_edge(L.adjacency_list[LK[i]], K.adjacency_list[i])
            print(edges)
            G.remove_edge(edges, GV)


def second_step(G, R, A, GR):
    for i in range(len(A)):
        if A[i] is None:
            GR = G.add_node(R.v_labels[i], R.adjacency_list[i], GR, A, i)


def dpo(G, Prod: Production, arr):
    D = Prod.dict
    GR = [None]*len(Prod.right.v_labels)
    LV = []
    for k in D[1]:
        if k is not None:
            GR[D[1].index(k)] = arr[D[0].index(k)]
    for i in range(len(Prod.left.v_labels)):
        LV.append(i)
    if check_if_right(G, Prod.left, arr, LV):
        G.visualize().show()
        first_step(Prod.left, Prod.connector, G, D[0], arr)
        G.visualize().show()
        second_step(G, Prod.right, D[1], GR)
        G.visualize().show()
        