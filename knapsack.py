import argparse
from knapsack_problem.simulated_annealing import *
from knapsack_problem.genetic import *
from knapsack_problem.util import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, required=True)
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    capacity, items = FileUtil.readFile(args.file)

    if args.algorithm == 'ga':
        print('Solving with Genetic Algorithm...')
        solution = GeneticAlgo().solve(items, capacity)

    elif args.algorithm == 'hc':
        print('Solving with Hill Climbing Algorithm...')
        print('HILL CLIMBING NOT IMPLEMENTED YET')

    elif args.algorithm == 'sa':
        print('Solving with Simulated Annealing Algorithm...')
        solution = SimulatedAnnealing().solve(capacity, items)

    else:
        raise Exception(f'Invalid Algorithm: {args.algorithm}')
