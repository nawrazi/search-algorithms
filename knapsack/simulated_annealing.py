from util import *

class SimulatedAnnealing:
    def __init__(self, temperature):
        self.items = None
        self.temperature = temperature
        self.optimum = float('-inf')
        ...

    def getRandomSolution(self):
        ...

    def getProbability(self, ):
        ...

    def solve(self, items):
        self.items = items
        ...


# if __name__ == '__main__':
#     FileUtil.generate()
#     algo = SimulatedAnnealing(2)
#     algo.solve(FileUtil.readFile())
