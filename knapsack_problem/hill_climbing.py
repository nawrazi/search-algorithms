from random import choice, randint

class HillClimbing:
    def __init__(self):
        self.cur_sack = []
        self.all_items = []
        self.sack_capacity = None
        self.cur_weight = 0
        self.cur_value = 0
        self.optimum_value = 0
        self.optimum_weight = 0
        self.optimum_sack = []

    def getRandomSolution(self):
        sack = self.cur_sack.copy()
        idx = randint(0, len(self.cur_sack) - 1)

        sack[idx] += choice(
            list({i for i in range(1, 4)}.difference({sack[idx]}))
        )
        return sack

    def getAllNeighbour(self, current_thing):

        list_neighbour = []

        for i in range(len(self.cur_sack)):
            new_sack = current_thing.copy()
            if self.cur_sack[i] + 1 > 3:
                continue
            new_sack[i] = choice(list({j for j in range(1, 4)}.difference({new_sack[i]})))
            while new_sack[i] > 3:
                new_sack[i] = choice(list({j for j in range(1, 4)}.difference({new_sack[i]})))

            list_neighbour.append(new_sack)

        return list_neighbour

    def getValue(self, sack):
        total_value, total_weight = 0, 0

        for i, count in enumerate(sack):
            total_value += count * self.all_items[i].value
            total_weight += count * self.all_items[i].weight

        return (total_value, total_weight) if total_weight <= self.sack_capacity else (0, 0)

    def hillClimbing(self):

        self.cur_sack = [0 for _ in range(len(self.all_items))]

        sack = self.getRandomSolution().copy()
        self.cur_value, self.cur_weight = self.getValue(sack)

        while self.cur_weight < self.sack_capacity:
            all_neighbours = self.getAllNeighbour(sack)
            la = 0
            for neighbour in all_neighbours:
                next_val, next_weight = self.getValue(neighbour)
                diff = next_val - self.cur_value

                if diff > 0:
                    la += 1
                    sack = neighbour
                    self.cur_value = next_val
                    self.cur_weight = next_weight

            if la == 0:
                return self.cur_value, sack

        return self.cur_value, sack

    def solve(self, sack_capacity, all_items):
        self.all_items = all_items
        self.sack_capacity = sack_capacity
        solution = {}

        for _ in range(10):
            best_value, list_of_items = self.hillClimbing()
            
            if best_value >= self.optimum_value:
                self.optimum_value = best_value
                self.optimum_sack = list_of_items

        for i in range(len(all_items)):
            solution[all_items[i].name.strip()] = self.optimum_sack[i]

        print(f'Selections: {solution}')
        print(f'Sack value: {self.optimum_value}')

        return solution



