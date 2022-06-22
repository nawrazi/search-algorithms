from itertools import count
from random import randint
from random import choice
from pygame import init
from util import *
     
     
class knapsack:
    def __init__(self):
        self.cur_sack = []
        self.all_items = []
        self.sack_capacity = None
        self.cur_weight = 0
        self.cur_value = 0
        self.optimum_value = 0
        self.optimum_weight = 0

        
        

    def getRandomSolution(self):
        sack = self.cur_sack.copy()
        idx = randint(0, len(self.cur_sack) - 1)
        
        sack[idx] += choice(
            list({i for i in range(4)}.difference({sack[idx]}))
        )
        return sack


    def getAllNeighbour(self, current_thing):

        list_neighbour = []

        for i in range(len(self.cur_sack)):
            new_sack = current_thing.copy()
            if self.cur_sack[i] + 1 > 3:
                continue
            new_sack[i] = choice(list({j for j in range(4)}.difference({new_sack[i]})))
            while new_sack[i] > 3:
                new_sack[i] = choice(list({j for j in range(3)}.difference({new_sack[i]})))

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
        print("first thing is :", self.cur_sack)
        
        sack = self.getRandomSolution().copy()
        self.cur_value, self.cur_weight = self.getValue(sack)

        print(sack)
        print("/////////////////////////////////////////////")
        while self.cur_weight < self.sack_capacity:
            all_neighbours = self.getAllNeighbour(sack)
            print(all_neighbours)
            la = 0
            for neighbour in all_neighbours:
                next_val, next_weight = self.getValue(neighbour)
                diff = next_val - self.cur_value
                
                if diff > 0:
                    la += 1
                    print(la, )
                    sack = neighbour
                    self.cur_value = next_val
                    self.cur_weight = next_weight

                    self.optimum_value = max(self.cur_value, self.optimum_value)
                    self.optimum_weight = max(self.cur_weight, self.optimum_weight)
                    
            if la == 0:
                return self.cur_value
            # if self.cur_value < :
            #     print("babay baby baby babay baby baby babay baby baby")
            #     print(next_val, self.cur_value)
            #     return self.cur_value


    def solve(self, sack_capacity, all_items):

        self.all_items = all_items
        self.sack_capacity = sack_capacity

        self.hillClimbing()
        self.optimum_value = max(self.cur_value, self.optimum_value)
        self.optimum_weight = max(self.cur_weight, self.optimum_weight)

        print(f'Selections: {self.cur_sack}')
        print(f'Sack value: {self.optimum_value}')
        print(f'Sack weight: {self.optimum_weight}')

        return self.optimum_value


reade = FileUtil()
reade.generate(10)
capacity, items = reade.readFile('data/data.txt')
print(capacity)
print("------------------------")
print(items[5].name, items[5].weight, items[5].value)

obj = knapsack()
obj.solve(capacity, items)
