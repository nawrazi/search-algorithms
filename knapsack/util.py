from random import random, randint

class Util:
    @staticmethod
    def readFile(path='data/data.txt'):
        data = []
        with open(path, 'r') as file:
            for line in file.readlines():
                data.append(line.strip().split(','))

        return data[2:]

    @staticmethod
    def generate(items=10):
        with open('data/data.txt', 'w') as file:
            file.write(f'{items * 5}\n')
            file.write('item,weight,value\n')
            for i in range(items):
                file.write(f'item{i + 1},')
                file.write('{:.1f}'.format(0.1 + random() * items / 2))
                file.write(f',{randint(2 * items, 100 * items)}\n')


# if __name__ == '__main__':
#     Util.generate(15)
#     Util.readFile()
