import random
from graph import Graph
from dikstruh import dijkstra


class TravelsMan:
    def __init__(self):
        self.graph = None
        self.shortest_distance = float('inf')
        self.cur_path = []
        

    def getRandomSolution(self, cities):
        connected = set()
        initial_solution = []
        length_of_initial = 0
        while length_of_initial < len(cities):
            selected_city = random.choice(cities)
            if selected_city not in connected:
                length_of_initial+=1
                connected.add(selected_city)
                initial_solution.append(selected_city)
        return initial_solution
    
    

    def getRoutingCost(self, path):
        total_distance = 0

        for i in range(1, len(path)):
            total_distance += dijkstra(self.graph, path[i-1], path[i])
        
        return total_distance


    def getAllneighbours(self, path):
        list_of_neighbour = []
        for j in range(len(path)):
            for i in range(1,len(path)):
                new_path = path.copy()
                new_path[j] , new_path[i] = path[i], path[j]
                list_of_neighbour.append(new_path)
                
        return list_of_neighbour       
        

    def getBestNeighbour(self, all_neighbours):
        
        best_neigh_cost = self.getRoutingCost(all_neighbours[0])
        best_routing_path = all_neighbours[0]

        for neighbour in all_neighbours:
            cur_path_cost = self.getRoutingCost(neighbour)
            if cur_path_cost < best_neigh_cost:
                best_neigh_cost = cur_path_cost
                best_routing_path = neighbour
        
        return best_routing_path
    
    def hillClimbing(self):
        cities = list({city for city in self.graph.nodes.keys()})
        bestSolutionPath = self.getRandomSolution(cities)
        bestSolutionCost = self.getRoutingCost(bestSolutionPath)
        # print(f'bestSolutionPath path: {bestSolutionPath}')
        # print(f'this the routing cost:  {bestSolutionCost}' )

        all_neighour = self.getAllneighbours(bestSolutionPath)
        # print(f'all neighbours around : {all_neighour}')

        current_solution_path = self.getBestNeighbour(all_neighour)
        current_solution_cost = self.getRoutingCost(current_solution_path)
        # print(f'this is this the best solution  :  {current_solution_path}' )

        # ans = bestSolutionCost
        while current_solution_cost < bestSolutionCost:
            
            bestSolutionCost = current_solution_cost
            bestSolutionPath = current_solution_path
            # ans += bestSolutionCost
            all_neighour = self.getAllneighbours(bestSolutionPath)

            current_solution_path = self.getBestNeighbour(all_neighour)
            current_solution_cost = self.getRoutingCost(current_solution_path)


        # self.cur_path = bestSolutionPath
        # self.shortest_distance = current_solution_cost
        # print(f'optimal path: {bestSolutionPath}')
        # print(f'distance: {bestSolutionCost}')
        # print(ans)
        return bestSolutionPath, bestSolutionCost
            
    def solve(self, graph):
        self.graph = graph
        pa, co = self.hillClimbing()
        print(pa)
        return co




graph = Graph('data/graph_data.txt')
obj = TravelsMan()

# dijkstra(graph, "Bucharest", "Vaslui")
mina = float('inf')
for i in range(20):

    na = obj.solve(graph)
    print(na)
    if na < mina:
        mina = na

print(f'distance: {mina}')