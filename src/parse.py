from matplotlib import pyplot as plt
from structures import Grammar, Graph, Production


def get_breaks(f):
    breaks = []
    dicts = []
    cut = 0
    dict = 0
    for i, line in f:

        if line == "-->\n":
            labels = i + 1
            start = i + 2

        elif line == "--<\n":
            stop = i - 1

            if breaks != []:
                cut += 1

            if cut % 3 == 0:
                dict = 0
            breaks.append((labels, start, stop))

        elif line == "---\n" and cut % 3 == 0 and dict == 0:
            dict1 = i + 1
            dict2 = i + 3
            dict = 1
            dicts.append((dict1, dict2))

    return breaks, dicts


def read_vlabels(f, s):
    line = f[s][1]
    vlabels = []
    for j in line:
        if j != " " and j != "\n":
            vlabels.append(j)
    return vlabels


def read_edges(f, start, stop):
    edges = []
    for i, line in f:
        if i >= start and i <= stop:
            edges.append(get_edge(line))
    return edges


def get_edge(s):
    return (int(s[0]), s[2], int(s[4]))


def edges_to_adj(e, n):
    adj = [[] for _ in range(n)]
    for u, s, v in e:
        adj[u].append((v, s))
        adj[v].append((u, s))
    return adj


def read_dict(f, d):
    dict = []
    line = f[d][1]
    for el in line:
        if el == "-":
            dict.append(None)
        elif el != " " and el != "\n":
            dict.append(int(el))
    return dict


def make_dict(f, d1, d2):
    S = []
    S.append((read_dict(f, d1)))
    S.append((read_dict(f, d2)))
    return S


def get_graph(f, labels, start, stop):
    vlabels = read_vlabels(f, labels)
    edges = read_edges(f, start, stop)
    adjacency_list = edges_to_adj(edges, len(vlabels))
    return Graph(vlabels, adjacency_list)


def parse(f):
    ef = list(enumerate(f))
    breaks, dicts = get_breaks(ef)
    G = get_graph(ef, breaks[0][0], breaks[0][1], breaks[0][2])

    prods = []
    lkr = []
    for i in range(1, len(breaks)):
        labels, start, stop = breaks[i]
        g = get_graph(ef, labels, start, stop)
        lkr.append(g)
        if i % 3 == 0:
            dict = make_dict(ef, dicts[i // 3 - 1][0], dicts[i // 3 - 1][1])
            prods.append(Production(lkr[0], lkr[1], lkr[2], dict))
            # prods.append((lkr[0], lkr[1], lkr[2]))
            lkr = []

    return Grammar(G, prods)
    # return G, prods


# test co
if __name__ == "__main__":

    with open("ex4.txt") as f:
        grammar = parse(f)
        g = grammar.input_graph
        prods = grammar.production_list
        g.visualize()
        plt.show()

        for prod in prods:
            prod.left.visualize()
            plt.show()
            prod.connector.visualize()
            plt.show()
            prod.right.visualize()
            plt.show()
