import argparse
from knapsack_problem.simulated_annealing import *
from knapsack_problem.genetic import *
from knapsack_problem.hill_climbing import *
from knapsack_problem.util import *
from graph_plotter import plot_graph

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, required=True)
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    capacity, items = FileUtil.readFile(args.file)

    if args.algorithm == 'ga':
        print('Solving with Genetic Algorithm...')
        solution = GeneticAlgo().solve(capacity, items)
        # plot_graph(solution, "Genetic")
    elif args.algorithm == 'hc':
        print('Solving with Hill Climbing Algorithm...')
        solution = HillClimbing().solve(capacity, items)
        plot_graph(solution, "Hills Climbing")

    elif args.algorithm == 'sa':
        print('Solving with Simulated Annealing Algorithm...')
        solution = SimulatedAnnealing().solve(capacity, items)
        plot_graph(solution, "Simulated Annealing")


    else:
        raise Exception(f'Invalid Algorithm: {args.algorithm}')
