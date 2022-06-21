import random
import numpy

class SimulatedAnnealing:
    def __init__(self, temperature=10):
        self.temperature = temperature
        self.cooldown_rate = 0.98
        self.graph = None
        self.cur_path = []
        self.cur_distance = 0
        self.shortest_distance = float('inf')

    def isLikely(self, diff):
        return numpy.exp(diff / self.temperature) > random.random()

    def distance(self, node1, node2):
        if (node1, node2) not in self.graph.all_distances:
            node1, node2 = node2, node1

        return self.graph.all_distances[(node1, node2)]

    def getPathLength(self, path):
        total_distance = 0

        for i in range(1, len(path)):
            total_distance += self.distance(path[i-1], path[i])

        return total_distance

    def getRandomSolution(self):
        path = self.cur_path.copy()
        idx1, idx2 = random.randint(1, len(path) - 2), random.randint(1, len(path) - 2)
        path[idx1], path[idx2] = path[idx2], path[idx1]
        return path

    def simulate(self):
        if not self.cur_path:
            cities = list({city for city in self.graph.nodes.keys()})
            self.cur_path = cities + [cities[0]]

        self.cur_distance = self.getPathLength(self.cur_path)

        for i in range(100):
            next_path = self.getRandomSolution()
            next_distance = self.getPathLength(next_path)
            diff = self.shortest_distance - next_distance

            if diff > 0 or self.isLikely(diff):
                self.cur_path = next_path
                self.cur_distance = next_distance

                self.shortest_distance = min(self.cur_distance, self.shortest_distance)

            self.temperature *= self.cooldown_rate

    def solve(self, graph):
        self.graph = graph
        graph.findAllDistances()

        for _ in range(100):
            self.simulate()
            self.shortest_distance = min(self.cur_distance, self.shortest_distance)

        print(f"Optimal Path: {' -> '.join(self.cur_path)}")
        print(f'Shortest Distance: {self.shortest_distance}')

        return self.shortest_distance
