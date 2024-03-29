
import random

class Chromosome:
    # accepts items to be included in a chromosome and 
    # boolean value to check whether it has to generate a chromosome or not
    def __init__(self, cities, generate=False) -> None:
        self.genes = [] if not generate else self.generate(cities)
   
    # generates random list with values representing presence or absence of a gene
    def generate(self, cities) -> None:
        def rndmSwap(lst) -> None:
            idx1 = random.randint(0, len(lst) - 1)
            idx2 = random.randint(0, len(lst) - 1)
            lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
        
        li = cities.copy()
        random.shuffle(li)
        return li

    # accepts list of items available and returns the fitness(total) value of a chromosome
    def fitness(self, graph) -> int:
        value = 0
        leng = len(self.genes)
        for i in range(len(self.genes)):
            if (self.genes[i % leng], self.genes[(i + 1) % leng]) in graph.all_distances:
                value += graph.all_distances[(self.genes[(i) % leng], self.genes[(i + 1) % leng])]
            else:
                value += graph.all_distances[(self.genes[(i + 1) % leng], self.genes[(i) % leng])]
        return value


class Population:
    # contains chromosomes
    def __init__(self, cities, size=100) -> None:
        self.size = size
        self.chromosomes = [Chromosome(cities, True) for i in range(self.size)]


class GeneticAlgo:
    def __init__(self) -> None:
        self.mutationPerc = 10
        self.best = (float('inf'), None)
        self.graph = None
        self.cities = None
        self.population = None
        self.popSize = 100

    def solve(self, graph , gen = 1000, popSize = 100) -> None:
        self.graph = graph
        graph.findAllDistances()
        self.popSize = popSize
        self.cities = list(self.graph.nodes.keys())
        self.population = Population(self.cities , popSize)
        self.main(gen)
    
    # returns  the fittest chromosome and its fitness
    def fittest(self) -> tuple:
        fittest = None
        fitness = float('inf')
        for chromo in self.population.chromosomes:
            if chromo.fitness(self.graph) < fitness:
                fitness = min(fitness, chromo.fitness(self.graph))
                fittest = chromo
        return fitness, fittest
     
     # returns two possible parents for the next generation
    def selection(self) -> list:
        idx1 = random.randint(0, self.population.size - 1)
        idx2 = random.randint(0, self.population.size - 1)
        parent1 = self.population.chromosomes[idx1]
        parent2 = self.population.chromosomes[idx2]
        return [parent1, parent2]
   
    # accepts to chromos as parent and generates  new chromo as a child
    def crossover(self, parent1, parent2) -> Chromosome:

        prnt1copy = Chromosome(self.cities)
        prnt2copy = Chromosome(self.cities)
        prnt1copy.genes = parent1.genes.copy()
        prnt2copy.genes = parent2.genes.copy()
        leng = len(parent1.genes) // 2

        for i in range(leng):
            temp = parent2.genes[i]
            idx = prnt1copy.genes.index(temp)
            prnt1copy.genes[idx] , prnt1copy.genes[i] = prnt1copy.genes[i] , prnt1copy.genes[idx]
        for i in range(leng):
            temp = parent1.genes[i]
            idx = prnt2copy.genes.index(temp)
            prnt2copy.genes[idx] , prnt2copy.genes[i] = prnt2copy.genes[i] , prnt2copy.genes[idx]

        if prnt1copy.fitness(self.graph) <= prnt2copy.fitness(self.graph):
            return prnt1copy
        else:
            return prnt2copy
    
    # changes a single chromosome from the population based on the mutation rate
    def mutation(self, chromosome) -> None:

        def rndmSwap(lst) -> None:
            idx1 = random.randint(0 , len(lst) - 1)
            idx2 = random.randint(0 , len(lst) - 1)
            lst[idx1] , lst[idx2] = lst[idx2] , lst[idx1]

        temp = random.randint(0, 100)
        if temp <= self.mutationPerc:
            for i in range(len(chromosome.genes)//4):
               rndmSwap(chromosome.genes)
     
    def main(self ,gen) -> tuple:
        generationNo = 1
        for i in range(gen):
            for k in range(len(self.population.chromosomes)):
                parent1, parent2 = self.selection()
                offspring = self.crossover(parent1=parent1, parent2=parent2)
                self.mutation(offspring)
                self.population.chromosomes[k] = offspring
            fittest = self.fittest()
            self.best = (fittest[0] , fittest[1]) if fittest[0] < self.best[0] else self.best
       
            generationNo += 1
        print(f"Optimal Path: {' -> '.join(self.best[1].genes)}")
        print(f'Shortest Distance: {self.best[0]}')
 
        return self.best
