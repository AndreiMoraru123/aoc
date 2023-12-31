import networkx as nx
from collections import defaultdict

lines = open("input.txt").read().splitlines()

components = defaultdict(set)
for l in lines:
    source, destinations = l.split(":")
    for d in destinations.split():
        components[source].add(d)
        components[d].add(source)

graph = nx.DiGraph()
for node, links in components.items():
    for l in links:
        graph.add_edge(node, l, capacity=1.0)
        graph.add_edge(l, node, capacity=1.0)

for x in [list(components.keys())[0]]:
    for y in components.keys():
        if x == y:
            continue
        cut, (left, right) = nx.minimum_cut(graph, x, y)
        if cut == 3:
            print(len(left) * len(right))
            break
