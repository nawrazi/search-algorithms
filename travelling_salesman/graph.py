from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.long = 0
        self.lat = 0

class Edge:
    def __init__(self, head, tail, weight, directed=False):
        self.head = head
        self.tail = tail
        self.weight = weight
        self.directed = directed

class Graph:
    def __init__(self, path):
        self.nodes = {}
        self.edges = defaultdict(list)

        self.buildGraphFromFile(path)
        # self.setLocationsFromFile()

    def addNode(self, node):
        self.nodes[node.val] = node

    def addEdge(self, edge):
        if edge.head.val not in self.nodes:
            self.addNode(edge.head)

        if edge.tail.val not in self.nodes:
            self.addNode(edge.tail)

        head, tail = self.nodes[edge.head.val], self.nodes[edge.tail.val]

        newEdge = Edge(head, tail, edge.weight)
        self.edges[head].append(newEdge)

        if not edge.directed:
            reverseEdge = Edge(tail, head, edge.weight)
            self.edges[tail].append(reverseEdge)

    def buildGraphFromFile(self, path):
        file = open(path, "r")
        data = [line.strip().split() for line in file.readlines()]

        for node1, node2, weight in data:
            self.addEdge(Edge(Node(node1), Node(node2), int(weight)))

        file.close()

    def setLocationsFromFile(self, path="data/location_data.txt"):
        file = open(path, "r")
        data = [line.strip().split() for line in file.readlines()]

        for val, lat, long in data:
            self.nodes[val].long = float(long)
            self.nodes[val].lat = float(lat)

        file.close()
