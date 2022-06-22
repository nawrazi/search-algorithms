import random


class Chromosome:
    # accepts size of chromosome and 
    # boolean value to check whether it has to generate a chromosome or not
    def __init__(self, size, generate=False) -> None:
        self.size = size
        self.genes = [0] * size if not generate else self.generate()

    # generates random list with values representing presence or absence of a gene
    def generate(self) -> list:
        li = [random.randint(0, 3) for i in range(self.size)]
        return li

    # accepts list of items available and returns the fitness(total) value of a chromo
    def fitness(self, items, capacity) -> int:
        fitness = 0
        weight = 0
        for gene in (range(len(self.genes))):
            fitness = fitness + items[gene].value * self.genes[gene]
            weight = weight + items[gene].weight * self.genes[gene]

        return fitness if weight <= capacity else -1 * fitness


class Population:
    # contains chromosomes
    def __init__(self, items_no, size=6) -> None:
        self.chromosomes = [Chromosome(items_no, True) for i in range(size)]


class GeneticAlgo:
    def __init__(self) -> None:
        self.mutationPerc = 40
        self.capacity = None
        self.items = None
        self.population = None
        self.best = None

    def solve(self, capacity, items) -> dict:
        self.capacity = capacity
        self.items = items
        self.population = Population(len(self.items), 6)
        self.best = (0 , Chromosome(len(self.items)))
        return self.main()

    # returns  the fittest chromosome and its fitness
    def fittest(self) -> tuple:
        fittest = None
        fitness = 0
        for i in range(len(self.population.chromosomes)):
            if self.population.chromosomes[i].fitness(self.items, self.capacity) > fitness:
                fitness = self.population.chromosomes[i].fitness(self.items, self.capacity)
                fittest = self.population.chromosomes[i]
        self.best = (fitness , fittest) if fitness > self.best[0] else self.best
       
        return (fitness, fittest)

    # returns two possible parents for the next generation
    def selection(self) -> list:
        posblParents = []
        temp = len(self.population.chromosomes) - 1
        for i in range(2):
            pr1 = self.population.chromosomes[random.randint(0, temp)]
            pr2 = self.population.chromosomes[random.randint(0, temp)]
            if pr1.fitness(self.items, self.capacity) >= pr2.fitness(self.items, self.capacity):
                posblParents.append(pr1)
            else:
                posblParents.append(pr2)
        return posblParents

    # accepts to chromos as parent and generates two new chromos as child
    def crossover(self, parent1, parent2) -> Chromosome:

        crPoint = random.randint(0, len(parent1.genes) - 1)
        child1 = Chromosome(len(self.items))
        child2 = Chromosome(len(self.items))
        child1.genes = parent1.genes[:crPoint] + parent2.genes[crPoint:]
        child2.genes = parent2.genes[:crPoint] + parent1.genes[crPoint:]
        fittest = None
        if child1.fitness(self.items, self.capacity) >= child2.fitness(self.items, self.capacity):
            fittest = child1
        else:
            fittest = child2
        return fittest

    # changes a single chromosome from the population based on the mutation rate
    def mutation(self, chromosome) -> None:
        temp = random.randint(0, 100)
        mutPoint = random.randint(0, len(chromosome.genes) - 1)
        if temp <= self.mutationPerc:
            sign = random.randint(0, 1)
            val = chromosome.genes[mutPoint]
            if val == 0:
                chromosome.genes[mutPoint] += 1
            elif val == 3:
                chromosome.genes[mutPoint] -= 1
            else:
                if sign:
                    chromosome.genes[mutPoint] += 1
                else:
                    chromosome.genes[mutPoint] -= 1

    def main(self) -> dict:

        generationNo = 1
        for i in range(2000):
            for k in range(len(self.population.chromosomes)):
                parent1, parent2 = self.selection()
                offspring = self.crossover(parent1=parent1, parent2=parent2)
                self.mutation(offspring)
                self.population.chromosomes[k] = offspring

            fittest = self.fittest()
            self.best = (fittest[0], fittest[1]) if fittest[0] > self.best[0] else self.best
            generationNo += 1

        solution = {self.items[i].name.strip(): self.best[1].genes[i] for i in range(len(self.items))}

        print("Solution ====>", solution)
        print("Value    ====>", self.best[0])
        return solution
