from random import random, randint

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = float(weight)
        self.value = float(value)


class FileUtil:
    @staticmethod
    def readFile(path):
        items = []
        with open(path, 'r') as file:
            capacity = int(file.readline())
            for line in file.readlines()[1:]:
                name, weight, value = line.strip().split(',')
                items.append(Item(name, weight, value))

        return capacity, items

    @staticmethod
    def generate(items=10):
        with open('data/data.txt', 'w') as file:
            file.write(f'{items * 5}\n')
            file.write('item,weight,value\n')
            for i in range(items):
                file.write(f'item{i + 1},')
                file.write('{:.1f}'.format(0.1 + random() * items / 2))
                file.write(f',{randint(2 * items, 100 * items)}\n')

