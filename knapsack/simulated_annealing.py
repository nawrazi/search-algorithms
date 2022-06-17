from util import *

class SimulatedAnnealing:
    def __init__(self, temperature):
        self.items = None
        self.capacity = None
        self.temperature = temperature
        self.optimum = float('-inf')
        ...

    def getRandomSolution(self):
        ...

    def getProbability(self, ):
        ...

    def solve(self, capacity, items):
        self.items = items
        self.capacity = capacity
        ...


# if __name__ == '__main__':
#     FileUtil.generate(15)
#     algo = SimulatedAnnealing(2)
#     capacity, items = FileUtil.readFile()
#     algo.solve(capacity, items)
