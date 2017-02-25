"""
Author:
      Tian Lan
"""
from graphviz import Digraph;
# import json

def make_graph(graph):
    """
    Arguments:
             graph: graph in representation of python dictionary. 
             {node1: {neighbour1: weight1}, {neighbour2: weight2}}
             E.g. {1: {2: 3}, 2: {}}
    Returns: None
    """
    graph_draw = Digraph(comment='output graph');

    for node in graph.keys():
        graph_draw.node(str(node) , color = 'purple');
    for node in graph.keys():
        for neighbour, weight in graph[node].iteritems():
            graph_draw.edge(str(node), str(neighbour), label = str("%.2f" % weight), weight = str(float(weight)), color = 'red')#str(weight))


    graph_draw.render('./test-output.gv', view=True);

def main():
    graph = dict(input("input graph: "));
    make_graph(graph);

if __name__ == "__main__":
    main();