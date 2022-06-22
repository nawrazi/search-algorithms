import matplotlib.pyplot as plt



def plot_graph(solution, name):
    
    item_list = list()
    item_value = list()

    for item in solution:
        item_list.append(item)
        item_value.append(solution[item])

    print(item_list)
    print(item_value)
    plt.rcParams['figure.figsize'] = (8, 5)
    plt.bar(item_list, item_value,width=0.5, color = "black")
    plt.xlabel("items")
    plt.ylabel("value ")
    plt.title(f'knapsack with {name}')
    plt.show()