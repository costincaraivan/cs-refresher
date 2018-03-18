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
        visited = [ False ] * len(self.node_list)
        queue = []
        path = []

        queue.append(self.node_list[0])
        visited[0] = True

        while queue:
            current_node = queue.pop(0)

            path.append(current_node)

            for connected_node in current_node.get_connections():
                if(not visited[connected_node.get_id()]):
                    queue.append(connected_node)
                    visited[connected_node.get_id()] = True

        return path

    # Depth first traversal.
    def dft(self):
        stack = []
        path = []

        stack.append(self.node_list[0])

        while stack:
            current_node = stack.pop()

            if current_node in path:
                continue

            path.append(current_node)

            for neighbor in current_node.get_connections():
                stack.append(self.node_list[neighbor.get_id()])

        return path

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
        logging.info("path: {}".format(str([ x.get_id() for x in self.sut.bft() ])))

    def test_dft(self):
        logging.info("path: {}".format(str([ x.get_id() for x in self.sut.dft() ])))

if __name__ == "__main__":
    unittest.main(verbosity = 2)