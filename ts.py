import argparse
from travelling_salesman.simulated_annealing import *
from travelling_salesman.graph import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, required=True)
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    graph = Graph(args.file)

    if args.algorithm == 'ga':
        print('Solving with Genetic Algorithm...')
        print('GENETIC ALGORITHM: NOT IMPLEMENTED YET')

    elif args.algorithm == 'hc':
        print('Solving with Hill Climbing Algorithm...')
        print('HILL CLIMBING NOT: IMPLEMENTED YET')

    elif args.algorithm == 'sa':
        print('Solving with Simulated Annealing Algorithm...')
        solution = SimulatedAnnealing().solve(graph)

    else:
        raise Exception(f'Invalid Algorithm: {args.algorithm}\n Please use ga, hc or sa')
