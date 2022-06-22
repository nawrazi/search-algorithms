import heapq
from collections import defaultdict
import heapq

class Node:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

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
        self.all_distances = {}
        self.buildGraphFromFile(path)

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

    def findAllDistances(self):
        def dijkstra(start, target):
            heap = [(0, self.nodes[start])]
            seen = {node: float("inf") for node in self.nodes}
            seen[start] = 0

            while heap:
                cur_distance, cur_node = heapq.heappop(heap)
                if cur_node.val == target:
                    return cur_distance

                for edge in self.edges[cur_node]:
                    nex_node = edge.tail
                    nex_distance = cur_distance + edge.weight

                    if nex_distance > seen[nex_node.val]:
                        continue
                    if nex_distance < seen[nex_node.val]:
                        heapq.heappush(heap, (nex_distance, nex_node))
                        seen[nex_node.val] = nex_distance

        for start_node in self.nodes:
            for target_node in self.nodes:
                if start_node == target_node or (target_node, start_node) in self.all_distances:
                    continue
                self.all_distances[(start_node, target_node)] = dijkstra(start_node, target_node)
