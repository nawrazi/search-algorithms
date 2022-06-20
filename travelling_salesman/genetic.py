import random
from util import FileUtil

class Chromosome:
    # accepts size of chromosome and 
    # boolean value to check whether it has to generate a chromosome or not
    def __init__(self,size,generate = False) -> None:
        pass
        
    #generates random list with values representig presence or absence of a gene
    def generate(self) -> int:
        pass
    # accepts list of items availabe and returns the fitness(total) value of a chromo
    def fitness(self,items,capacity) -> int:
        pass
    
class Population:
    #contains chromosmes
    def __init__(self,itemsNo,size = 6 ) -> None:
        pass
        
    
             
class GeneticAlgo:
    def __init__(self) -> None:
        pass
       

    #returns value of the fittest chromosome
    def fittest(self) -> int:
        pass

    #returns two possible parents for the next generation
    def selection(self) -> list:
        pass

    #accepts to chromos as parent and generates two new chromos as child
    def crossover(self, parent1 , parent2) -> Chromosome:
        pass
   
    #mutates an offspring based on the mutation rate
    def mutation(self , chromosome) -> None:
        pass

    def main(self) -> None:
        pass


if __name__ == "__main__" :  
    FileUtil.generate()    
    GeneticAlgo()
    
