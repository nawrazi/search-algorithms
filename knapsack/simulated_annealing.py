from util import FileUtil, Item
import random
import numpy

class SimulatedAnnealing:
    def __init__(self, temperature):
        self.temperature = temperature
        self.cooldown_rate = 0.98
        self.sack_capacity = None
        self.all_items = []
        self.cur_sack = []
        self.optimum_value = 0
        self.optimum_weight = 0

    def isLikely(self, diff):
        return numpy.exp(diff / self.temperature) > random.random()

    def getValue(self, sack):
        total_value, total_weight = 0, 0
        for i, count in enumerate(sack):
            total_value += count * self.all_items[i].value
            total_weight += count * self.all_items[i].weight

        return (total_value, total_weight) if total_weight <= self.sack_capacity else (0, 0)

    def getRandomSolution(self):
        sack = self.cur_sack.copy()
        idx = random.randint(0, len(self.cur_sack) - 1)
        sack[idx] = random.choice(
            list({i for i in range(4)}.difference({sack[idx]}))
        )
        return sack

    def simulate(self):
        self.cur_sack = [1 for _ in range(len(self.all_items))]
        self.optimum_value, self.optimum_weight = self.getValue(self.cur_sack)

        for i in range(10_000):
            next_sack = self.getRandomSolution()
            next_val, next_weight = self.getValue(next_sack)
            diff = next_val - self.optimum_value

            if diff > 0 or self.isLikely(diff):
                self.cur_sack = next_sack
                self.optimum_value = next_val
                self.optimum_weight = next_weight

            self.temperature *= self.cooldown_rate

    def solve(self, sack_capacity, all_items):
        self.all_items = all_items
        self.sack_capacity = sack_capacity
        self.simulate()

        print(f'Selections: {self.cur_sack}')
        print(f'Sack value: {self.optimum_value}')
        print(f'Sack weight: {self.optimum_weight}')


if __name__ == '__main__':
    # FileUtil.generate(15)
    algo = SimulatedAnnealing(2)
    capacity, items = FileUtil.readFile()
    algo.solve(capacity, items)

    # test_vals = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
    # test_weights = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
    #
    # test_items = [Item('test', w, v) for w, v in zip(test_vals, test_weights)]
    # # algo.solve(sum(test_weights), test_items)
    # # algo.solve(101, test_items)
