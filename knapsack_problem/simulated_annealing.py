import random
import numpy

class SimulatedAnnealing:
    def __init__(self, temperature=10):
        self.temperature = temperature
        self.cooldown_rate = 0.98
        self.sack_capacity = None
        self.all_items = []
        self.cur_sack = []
        self.cur_value = 0
        self.cur_weight = 0
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
        idx1 = random.randint(0, len(self.cur_sack) - 1)
        idx2 = random.randint(0, len(self.cur_sack) - 1)
        sack[idx1] = random.choice(
            list({i for i in range(4)}.difference({sack[idx1]}))
        )
        sack[idx2] = random.choice(
            list({i for i in range(4)}.difference({sack[idx2]}))
        )
        return sack

    def simulate(self):
        if not self.cur_sack:
            self.cur_sack = [0 for _ in range(len(self.all_items))]
            for i in range(len(self.cur_sack)):
                if self.cur_sack[i] % 3:
                    self.cur_sack[i] = 1
            self.cur_value, self.cur_weight = self.getValue(self.cur_sack)

        for i in range(100):
            next_sack = self.getRandomSolution()
            next_val, next_weight = self.getValue(next_sack)
            diff = next_val - self.cur_value

            if diff > 0 or self.isLikely(diff):
                self.cur_sack = next_sack
                self.cur_value = next_val
                self.cur_weight = next_weight

                self.optimum_value = max(self.cur_value, self.optimum_value)
                self.optimum_weight = max(self.cur_weight, self.optimum_weight)

            self.temperature *= self.cooldown_rate

    def solve(self, sack_capacity, all_items):
        self.all_items = all_items
        self.sack_capacity = sack_capacity

        for _ in range(1000):
            self.simulate()
            self.optimum_value = max(self.cur_value, self.optimum_value)
            self.optimum_weight = max(self.cur_weight, self.optimum_weight)

        if not self.optimum_value:
            self.optimum_value, _ = self.getValue(self.cur_sack)

        solution = {self.all_items[i].name.strip(): self.cur_sack[i] for i in range(len(self.all_items))}

        print(f'Selections: {solution}')
        print(f'Sack value: {self.optimum_value}')

        return self.optimum_value
