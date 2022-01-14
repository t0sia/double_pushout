from matplotlib import pyplot as plt
from src.structures import Grammar, Graph, Production

def get_breaks(f):
    breaks = []
    for i, line in f:

        if line == "-->\n":
            labels = i + 1
            indexes = i + 2
            start = i + 3

        elif line == "--<\n":
            stop = i - 1
            breaks.append((labels, indexes, start, stop))

    return breaks


def read_vlabels(f, labels, indexes):
    i = f[indexes][1].split()
    l = f[labels][1].split()
    vlabels = []
    for j in range(len(l)):
        vlabels.append((int(i[j]), l[j]))

    return dict(vlabels)


def read_edges(f, start, stop):
    edges = []
    for i, line in f:
        if i >= start and i <= stop:
            edges.append(get_edge(line))
    return edges


def get_edge(s):
    res = s.split()
    res[0] = int(res[0])
    res[len(res)-1] = int(res[len(res)-1])
    return res


def edges_to_adj(e, n, labels):
    adj = [[] for _ in range(n+1)]
    for u, s, v in e:
        adj[u].append((v, s))
        adj[v].append((u, s))

    out = []
    for u in labels:
        out.append((u, adj[u]))

    return dict(out)


def get_graph(f, labels, indexes, start, stop):
    vlabels = read_vlabels(f, labels, indexes)
    n = 0
    for label in vlabels:
        n = max(n, label)
    edges = read_edges(f, start, stop)
    adjacency_list = edges_to_adj(edges, n, vlabels)
    return Graph(vlabels, adjacency_list)


def parse(f):
    ef = list(enumerate(f))
    breaks = get_breaks(ef)
    G = get_graph(ef, breaks[0][0], breaks[0][1], breaks[0][2], breaks[0][3] )

    prods = []
    lkr = []
    for i in range(1, len(breaks)):
        labels, indexes, start, stop = breaks[i]
        g = get_graph(ef, labels, indexes, start, stop)
        lkr.append(g)
        if i % 3 == 0:
            prods.append(Production(lkr[0], lkr[1], lkr[2]))
            lkr = []

    return Grammar(G, prods)


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
