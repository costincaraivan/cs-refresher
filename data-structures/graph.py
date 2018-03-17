# Completely silly exercises, in real life use a graph library.

import unittest
import logging

logging.basicConfig(level = logging.INFO)


class GraphNode:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return "{} connected to {}".format(str(self.id), str([x.get_id() for x in self.connected_to]))


class Graph:
    def __init__(self):
        self.node_list = {}
        self.node_count = 0

    def add_node(self, key):
        self.node_count += 1
        newNode = GraphNode(key)
        self.node_list[key] = newNode
        return newNode

    def get_node(self, key):
        if key in self.node_list:
            return self.node_list[key]
        else:
            return None

    def add_edge(self, fromNode, toNode, cost=0):
        if fromNode not in self.node_list:
            self.add_node(fromNode)
        if toNode not in self.node_list:
            self.add_node(toNode)
        self.node_list[fromNode].add_neighbor(self.node_list[toNode], cost)

    def get_nodes(self):
        return self.node_list

    # Breadth first traversal.
    def bft(self):
        visited = [ False for x in self.node_list ]
        queue = []

        visited[0] = True
        queue.append(self.node_list[0])

        while len(queue) != 0:
            current_node = queue.pop()
            logging.info(current_node)

            for connected_node in current_node.get_connections():
                if(not visited[connected_node.get_id()]):
                    visited[connected_node.get_id()] = True
                    queue.append(connected_node)

    # Depth first traversal.
    def dft(self):
        pass

    def __contains__(self, node):
        return node in self.node_list

    def __iter__(self):
        return iter(self.node_list.values())


class GraphTests(unittest.TestCase):
    sut = None

    def setUp(self):
        self.sut = Graph()

        for node in range(7):
            self.sut.add_node(node)

        self.sut.add_edge(0, 1, 1)
        self.sut.add_edge(0, 4, 1)
        self.sut.add_edge(1, 2, 1)
        self.sut.add_edge(2, 3, 1)
        self.sut.add_edge(2, 6, 1)
        self.sut.add_edge(4, 5, 1)

    def test_bft(self):
        self.sut.bft()

if __name__ == "__main__":
    unittest.main(verbosity = 2)