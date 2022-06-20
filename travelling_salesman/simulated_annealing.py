import random
import numpy
from graph import Graph

class SimulatedAnnealing:
    def __init__(self, temperature=10):
        self.graph = None
        self.temperature = temperature
        self.cooldown_rate = 0.9
        self.cur_path = []
        self.shortest_distance = float('inf')

    def isLikely(self, diff):
        return numpy.exp(diff / self.temperature) > random.random()

    def getPathLength(self, path):
        total_distance = 0
        distance = lambda node1, node2: (node1.lat - node2.lat) ** 2 + (node1.long - node2.long) ** 2

        for i in range(1, len(path)):
            total_distance += distance(self.graph.nodes[path[i]], self.graph.nodes[path[i-1]])

        return total_distance

    def getRandomSolution(self):
        path = self.cur_path.copy()
        idx1, idx2 = random.randint(0, len(path) - 1), random.randint(0, len(path) - 1)
        path[idx1], path[idx2] = path[idx2], path[idx1]
        return path

    def simulate(self):
        cities = list({city for city in self.graph.nodes.keys()})
        self.cur_path = cities + [cities[0]]
        self.shortest_distance = self.getPathLength(self.cur_path)

        for i in range(10_000):
            next_path = self.getRandomSolution()
            next_distance = self.getPathLength(next_path)
            diff = self.shortest_distance - next_distance

            if diff > 0 or self.isLikely(diff):
                self.cur_path = next_path
                self.shortest_distance = next_distance

            self.temperature *= self.cooldown_rate

    def solve(self, graph):
        self.graph = graph
        self.simulate()

        return self.shortest_distance


if __name__ == '__main__':
    grp = Graph('data/graph_data.txt')
    algo = SimulatedAnnealing()

    print(algo.solve(grp))
